from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from contextlib import asynccontextmanager
from app.websocket_manager import websocket_manager
from app.quiz_service import evaluate_quiz
from app.database import get_quiz_attempts

@asynccontextmanager
async def app_lifespan(_app: FastAPI):
    yield  # No explicit database initialization needed for MongoDB

app = FastAPI(lifespan=app_lifespan)

@app.websocket("/ws/{student_id}")
async def websocket_endpoint(websocket: WebSocket, student_id: str):
    await websocket_manager.connect(student_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            quiz_id = data.get("quiz_id")
            answers = data.get("answers")

            if not quiz_id or not answers:
                await websocket.send_json({"error": "Invalid request format."})
                continue

            # Evaluate quiz (db parameter removed)
            result = await evaluate_quiz(student_id, quiz_id, answers)

            # Send results back to the frontend
            await websocket_manager.send_message(student_id, result)
    except WebSocketDisconnect:
        websocket_manager.disconnect(student_id)

@app.get("/quiz_attempts/{student_id}")
async def get_attempts(student_id: str):
    """Retrieve all quiz attempts for a student from MongoDB"""
    attempts = await get_quiz_attempts(student_id)
    return {"student_id": student_id, "attempts": attempts}
