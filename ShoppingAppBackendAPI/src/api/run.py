import os
import logging

import uvicorn

# PUBLIC_INTERFACE
def get_bind_host() -> str:
    """Return the bind host for the server from env, defaulting to 0.0.0.0."""
    return os.getenv("HOST", os.getenv("BIND_HOST", "0.0.0.0"))

# PUBLIC_INTERFACE
def get_bind_port() -> int:
    """Return the bind port for the server from env, defaulting to 3001."""
    # Accept multiple env var names, default safe
    port_str = os.getenv("PORT") or os.getenv("REACT_APP_PORT") or "3001"
    try:
        return int(port_str)
    except ValueError:
        return 3001

# PUBLIC_INTERFACE
def run() -> None:
    """
    Start the uvicorn ASGI server with the FastAPI app.

    Reads the host/port from environment variables with safe defaults:
    - HOST or BIND_HOST -> default 0.0.0.0
    - PORT or REACT_APP_PORT -> default 3001
    """
    host = get_bind_host()
    port = get_bind_port()

    # Use module:variable string so reload/worker setups can import correctly
    app_path = "src.api.main:app"

    # Log the effective binding for troubleshooting
    logging.basicConfig(level=logging.INFO)
    logging.getLogger(__name__).info("Starting server on %s:%s (app=%s)", host, port, app_path)

    uvicorn.run(
        app_path,
        host=host,
        port=port,
        reload=False,
        proxy_headers=True,
        forwarded_allow_ips="*",
        # http/loop can rely on defaults; uvloop and httptools are available from requirements
    )

if __name__ == "__main__":
    run()
