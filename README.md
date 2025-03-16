# Quiz WebSocket Backend 
This is a FastAPI-based backend that allows real-time quiz evaluation via WebSockets and stores quiz results in MongoDB.

## 📦 Project Setup

### Prerequisites:

- Python 3.10+
- MongoDB (running locally on default port 27017)
- Git

### Install dependencies:

```bash
# Clone the repository
git clone https://github.com/your-username/quiz_websocket_backend.git
cd quiz_websocket_backend

# Install required packages
pip install -r requirements.txt

###Running the FastAPI App Locally
# From the root project folder
uvicorn app.main:app –reload


###Testing the WebSocket with Postman
1.	Open Postman.
2.	Go to New → WebSocket Request.
3.	Connect to:
ws://127.0.0.1:8000/ws/{student_id}
Replace {student_id} with any student ID, e.g., student_001.
4.	Send this sample JSON payload:
{
  "quiz_id": "quiz_001",
  "answers": {
    "q1": "A",
    "q2": "C",
    "q3": "A",
    "q4": "D",
    "q5": "B"
  }
}
	
5.	Expected output
{
    "student_id": "3",
    "quiz_id": "quiz_001",
    "total_correct": 3,
    "total_incorrect": 2,
    "score_percentage": 60.0,
    "feedback": "Good job! Revise the missed topics.",
    "chart_data": {
        "correct": 3,
        "incorrect": 2
    }
}


