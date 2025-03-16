from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, JSON

Base = declarative_base()

class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id = Column(String(50), index=True)
    quiz_id = Column(String(50))
    answers = Column(JSON)
    total_correct = Column(Integer)
    total_incorrect = Column(Integer)
    score_percentage = Column(Float)
    feedback = Column(String(255))
