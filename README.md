# shopping-app-project-49784-49878

This workspace contains the ShoppingAppBackendAPI service.

Preview startup uses:
- uvicorn main:app --host 0.0.0.0 --port 3001 (as documented in ShoppingAppBackendAPI/STARTUP.md)

Quick verification steps:
- Check health: curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3001/health (or the provided preview URL)
- Expected response status: 200

Health endpoints:
- GET /           -> {"message":"Healthy"}
- GET /health     -> {"status":"ok"}

If PORT/host need to be overridden, use env:
- HOST or BIND_HOST (default: 0.0.0.0)
- PORT or REACT_APP_PORT (default: 3001)
- REACT_APP_HEALTHCHECK_PATH (default: /health)