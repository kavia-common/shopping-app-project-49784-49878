# Backend Startup

This service supports two startup modes:

1) Preview (shim)
   uvicorn main:app --host 0.0.0.0 --port 3001

   Uses ShoppingAppBackendAPI/main.py shim that imports app from src.api.main.

2) Module runner (preferred for local dev)
   python -m src.api.run

Environment variables:
- HOST or BIND_HOST (default: 0.0.0.0)
- PORT or REACT_APP_PORT (default: 3001)
- REACT_APP_HEALTHCHECK_PATH (default: /health)

Health endpoints:
- GET /           -> {"message":"Healthy"}
- GET /health     -> {"status":"ok"} (or custom path via REACT_APP_HEALTHCHECK_PATH)
