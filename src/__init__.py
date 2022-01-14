import uvicorn

from src.events import Events

__all__ = []

if __name__ == "__main__":
    PORT = 8000
    Events.PORT = PORT
    print(f"Events.PORT at __init__.py: {Events.PORT}")
    uvicorn.run(
        "src.listener:app",
        host="0.0.0.0",
        port=PORT,
        reload=True,
        log_level="info",
    )