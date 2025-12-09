"""
Package initializer for the Shopping App Backend API's source code.

This file ensures that 'src' is recognized as a Python package so that
absolute imports like 'src.api.main' work reliably in environments that
launch the app via the preview shim (uvicorn main:app).
"""

# PUBLIC_INTERFACE
def package_info() -> str:
    """Return a short description of the 'src' package."""
    return "Shopping App Backend API source package"
