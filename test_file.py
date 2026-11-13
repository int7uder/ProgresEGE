from database import SessionLocal
from models.exam import Exam

with SessionLocal() as session:
    exams = session.query(Exam).filter().all()
    print(exams)