from database import SessionLocal
from models.exam import Exam

def f():
    with SessionLocal() as session:
        exams = session.query(Exam).all()
        # return {
        #     "exams": [
        #         {
        #             "id": exam.id,
        #             "user_id": exam.user_id,
        #
        #         } for exam in exams
        #     ]
        # }
    return {
        "exams": [
            {
                "id": exam.id,
                "user_id": exam.user_id,
                "subject_id": exam.subject_id,
                "primary_score": exam.primary_score,
                "test_score": exam.test_score,
                "created_at": exam.created_at,
                "runtime": exam.runtime,
            } for exam in exams
        ]
    }
print(f())
