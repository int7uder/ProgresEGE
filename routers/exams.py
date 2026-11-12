from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError

from models.exam_answer import (
    SocietyAnswer,
    RussianAnswer,
    EnglishAnswer,
    MathProfileAnswer,
    MathBasicAnswer,
    PhysicsAnswer,
    ChemistryAnswer,
    BiologyAnswer,
    HistoryAnswer,
    GeographyAnswer,
    InformaticsAnswer,
    LiteratureAnswer,
    GermanAnswer,
    FrenchAnswer,
    SpanishAnswer,
    ChineseAnswer,
)

from schemas.exam import ExamCreate

from schemas.exam_answer import (
    SocietyAnswerCreate,
    RussianAnswerCreate,
    EnglishAnswerCreate,
    MathProfileAnswerCreate,
    MathBasicAnswerCreate,
    PhysicsAnswerCreate,
    ChemistryAnswerCreate,
    BiologyAnswerCreate,
    HistoryAnswerCreate,
    GeographyAnswerCreate,
    InformaticsAnswerCreate,
    LiteratureAnswerCreate,
    GermanAnswerCreate,
    FrenchAnswerCreate,
    SpanishAnswerCreate,
    ChineseAnswerCreate,
)
from database import SessionLocal
from dependencies import get_current_user
from models.exam import Exam
from models.subject import Subject
from models.user_subjects import UserSubject
from models.user import User
from services.scoring import SCORE_TABLES

router = APIRouter()


ANSWER_MODELS = {
    "Обществознание": (SocietyAnswer, SocietyAnswerCreate),
    "Русский язык": (RussianAnswer, RussianAnswerCreate),
    "Английский язык": (EnglishAnswer, EnglishAnswerCreate),
    "Математика профильная": (MathProfileAnswer, MathProfileAnswerCreate),
    "Математика базовая": (MathBasicAnswer, MathBasicAnswerCreate),
    "Физика": (PhysicsAnswer, PhysicsAnswerCreate),
    "Химия": (ChemistryAnswer, ChemistryAnswerCreate),
    "Биология": (BiologyAnswer, BiologyAnswerCreate),
    "История": (HistoryAnswer, HistoryAnswerCreate),
    "География": (GeographyAnswer, GeographyAnswerCreate),
    "Информатика": (InformaticsAnswer, InformaticsAnswerCreate),
    "Литература": (LiteratureAnswer, LiteratureAnswerCreate),
    "Немецкий язык": (GermanAnswer, GermanAnswerCreate),
    "Французский язык": (FrenchAnswer, FrenchAnswerCreate),
    "Испанский язык": (SpanishAnswer, SpanishAnswerCreate),
    "Китайский язык": (ChineseAnswer, ChineseAnswerCreate),
}

@router.get("/exams")
def get_exams(
        current_user: User = Depends(get_current_user),
):
    pass

@router.post("/exams")
def create_exam(
    data: ExamCreate,
    current_user: User = Depends(get_current_user)
):
    with SessionLocal() as session:
        with session.begin():

            subject = session.query(Subject).filter(
                Subject.id == data.subject_id
            ).first()

            if subject is None:
                raise HTTPException(
                    status_code=404,
                    detail="Subject not found"
                )

            user_subject = session.query(UserSubject).filter(
                UserSubject.user_id == current_user.id,
                UserSubject.subject_id == data.subject_id,
                UserSubject.is_active.is_(True)
            ).first()

            if user_subject is None:
                raise HTTPException(
                    status_code=403,
                    detail="You have not selected this subject"
                )

            answer_config = ANSWER_MODELS.get(subject.name)

            if answer_config is None:
                raise HTTPException(
                    status_code=400,
                    detail="Answer model for this subject is not configured"
                )

            answer_model, answer_schema = answer_config

            try:
                validated_answers = answer_schema.model_validate(
                    data.answers
                )
            except ValidationError as error:
                raise HTTPException(
                    status_code=422,
                    detail=error.errors()
                )

            primary_score = sum(validated_answers.model_dump().values())

            score_table = SCORE_TABLES.get(subject.name)

            if score_table is None:
                raise ValueError("Не найдена таблица перевода баллов")

            test_score = score_table.get(primary_score)

            if test_score is None:
                raise ValueError("Недопустимое количество первичных баллов")

            exam = Exam(
                user_id=current_user.id,
                subject_id=data.subject_id,
                runtime=data.runtime,
                primary_score=primary_score,
                test_score=test_score
            )

            session.add(exam)
            session.flush()

            answers = answer_model(
                exam_id=exam.id,
                **validated_answers.model_dump()
            )

            session.add(answers)
            session.flush()

            result = {
                "message": "Exam created successfully",
                "exam_id": exam.id,
                "subject": subject.name,
                "runtime": exam.runtime
            }

        # Здесь автоматически выполняется COMMIT

    return result