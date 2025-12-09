"""
Main ASGI application shim for Uvicorn.

This module exists to support environments that start the server with:
    uvicorn main:app --host 0.0.0.0 --port 3001

It re-exports the FastAPI application instance defined in src.api.main.
"""
from src.api.main import app as app  # noqa: F401

# PUBLIC_INTERFACE
def get_app():
    """Return the FastAPI app instance for ASGI servers."""
    return app
