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
                # "id": exam.id,

            }
        ]
    }