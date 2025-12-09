import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# PUBLIC_INTERFACE
def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    - Adds CORS middleware
    - Registers root and health endpoints
    - Configures OpenAPI metadata and tags

    Returns:
        FastAPI: Configured FastAPI app instance.
    """
    app = FastAPI(
        title="Shopping App Backend API",
        description="FastAPI backend for the Shopping App. Provides APIs for lists, items, reminders, and notifications.",
        version="0.1.0",
        openapi_tags=[
            {"name": "health", "description": "Service health and readiness checks"},
        ],
    )

    # CORS configured to allow all in preview; restrict in production via env later
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    health_path: str = os.getenv("REACT_APP_HEALTHCHECK_PATH", "/health")

    # Root responds 200 for simple checks
    @app.get("/", tags=["health"], summary="Root", description="Root endpoint for quick health verification.")
    # PUBLIC_INTERFACE
    def root() -> dict:
        """Root endpoint for quick health verification returning a JSON message."""
        return {"message": "Healthy"}

    # Dedicated health endpoint responds 200
    @app.get(health_path, tags=["health"], summary="Health", description="Kubernetes/preview health endpoint that returns 200 OK.")
    # PUBLIC_INTERFACE
    def health() -> dict:
        """Dedicated health endpoint for readiness/liveness probes."""
        return {"status": "ok"}

    return app


# Expose app for ASGI servers and OpenAPI generation scripts
app: FastAPI = create_app()
