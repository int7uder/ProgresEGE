from fastapi import APIRouter, Depends
from database import SessionLocal
from dependencies import get_current_user
from models.subject import Subject
from models.user_subjects import UserSubject
from schemas.user_subject import CreateUserSubject
from models.user import User

router = APIRouter()

@router.get("/subjects/available")
def get_available_subjects():
    with SessionLocal() as session:
        subjects = session.query(Subject).all()
    return {
        "subjects": [
            {
                "id": subject.id,
                "name": subject.name
            } for subject in subjects
        ]
    }


@router.get("/subjects")
def get_subjects(
        current_user: User = Depends(get_current_user)
):
    with (SessionLocal() as session):
        subjects = session.query(Subject).join(UserSubject, Subject.id == UserSubject.subject_id).filter(UserSubject.user_id == current_user.id, UserSubject.is_active == True).all()
    return {
        "subjects": [
            {"id": subject.id, "name": subject.name}
            for subject in subjects
        ]
    }

@router.post("/subjects")
def create_subject(
    subject: CreateUserSubject,
    current_user: User = Depends(get_current_user),
):
    with SessionLocal() as session:
        add_subject = UserSubject(
            user_id = current_user.id,
            subject_id = subject.subject_id
        )
        session.add(add_subject)
        session.commit()
        return {
            "subject_added": "Subject add successfully",
            "subject": subject.subject_id
        }