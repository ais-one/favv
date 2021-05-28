from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from main import app

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    await websocket.send_text(f"Message text was: {data}")
