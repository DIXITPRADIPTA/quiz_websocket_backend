from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URI)
db = client["quiz_db"]
collection = db["quiz_attempts"]

#Function to store quiz results in MongoDB
async def store_quiz_result(student_id: str, quiz_id: str, answers: dict, total_correct: int, total_incorrect: int, score_percentage: float, feedback: str):
    new_attempt = {
        "student_id": student_id,
        "quiz_id": quiz_id,
        "answers": answers,
        "total_correct": total_correct,
        "total_incorrect": total_incorrect,
        "score_percentage": score_percentage,
        "feedback": feedback
    }
    await collection.insert_one(new_attempt)


# Function to retrieve quiz attempts for a student
async def get_quiz_attempts(student_id: str):
    attempts = await collection.find({"student_id": student_id}).to_list(length=100)
    return attempts
