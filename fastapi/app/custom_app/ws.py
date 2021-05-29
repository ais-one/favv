from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.ws import ConnectionManager

router_custom_app_ws = APIRouter()

wsManager = ConnectionManager()

@router_custom_app_ws.websocket("/ws/{client_id}")
# ws_custom_app = APIRouter()
# @ws_custom_app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
  # await websocket.accept()
  # await websocket.send_text("hi")
  # await websocket.close()
  await wsManager.connect(websocket)
  try:
    while True:
      data = await websocket.receive_text()
      await wsManager.send_message(f"You wrote: {data}", websocket)
      await wsManager.broadcast(f"Client #{client_id} says: {data}")
  except WebSocketDisconnect:
    wsManager.disconnect(websocket)
    await wsManager.broadcast(f"Client #{client_id} left the chat")
