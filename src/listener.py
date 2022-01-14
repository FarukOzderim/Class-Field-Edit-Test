from fastapi import FastAPI
from src.events import Events

app = FastAPI()


@app.get("/")
async def root():
    print(f"Events.PORT at listener.py: {Events.PORT}")
    return {"Events.PORT at listener.py": Events.PORT}
