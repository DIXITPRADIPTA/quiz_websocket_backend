from app.database import store_quiz_result

# Predefined correct answers
CORRECT_ANSWERS = {
    "q1": "A",
    "q2": "B",
    "q3": "A",
    "q4": "D",
    "q5": "A"
}

async def evaluate_quiz(student_id: str, quiz_id: str, answers: dict):
    """
    Evaluate the quiz responses and store the result in MongoDB.
    """
    total_questions = len(CORRECT_ANSWERS)
    total_correct = sum(1 for q, ans in answers.items() if CORRECT_ANSWERS.get(q) == ans)
    total_incorrect = total_questions - total_correct
    score_percentage = (total_correct / total_questions) * 100

    # Generate feedback
    if score_percentage >= 90:
        feedback = "Excellent performance! Keep it up!"
    elif score_percentage >= 60:
        feedback = "Good job! Revise the missed topics."
    else:
        feedback = "Needs improvement. Consider reviewing key concepts."

    # Chart Data
    chart_data = {"correct": total_correct, "incorrect": total_incorrect}

    # Store in MongoDB
    await store_quiz_result(student_id, quiz_id, answers, total_correct, total_incorrect, score_percentage, feedback)

    return {
        "student_id": student_id,
        "quiz_id": quiz_id,
        "total_correct": total_correct,
        "total_incorrect": total_incorrect,
        "score_percentage": score_percentage,
        "feedback": feedback,
        "chart_data": chart_data
    }
