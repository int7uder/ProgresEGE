from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class ExamAnswer(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    exam_id: Mapped[int] = mapped_column(
        ForeignKey("exams.id"),
        unique=True,
        nullable=False
    )


def create_answer_model(class_name: str, table_name: str, task_count: int):
    attributes = {
        "__tablename__": table_name,
        "__module__": __name__,
    }

    for number in range(1, task_count + 1):
        attributes[f"task_number_{number}"] = mapped_column(
            Integer,
            default=0,
            nullable=False
        )

    return type(class_name, (ExamAnswer,), attributes)


SocietyAnswer = create_answer_model(
    "SocietyAnswer", "society_answers", 25
)

RussianAnswer = create_answer_model(
    "RussianAnswer", "russ_answers", 27
)

EnglishAnswer = create_answer_model(
    "EnglishAnswer", "english_answers", 42
)

MathProfileAnswer = create_answer_model(
    "MathProfileAnswer", "math_profile_answers", 19
)

MathBasicAnswer = create_answer_model(
    "MathBasicAnswer", "math_basic_answers", 21
)

PhysicsAnswer = create_answer_model(
    "PhysicsAnswer", "physics_answers", 26
)

ChemistryAnswer = create_answer_model(
    "ChemistryAnswer", "chemistry_answers", 34
)

BiologyAnswer = create_answer_model(
    "BiologyAnswer", "biology_answers", 28
)

HistoryAnswer = create_answer_model(
    "HistoryAnswer", "history_answers", 21
)

GeographyAnswer = create_answer_model(
    "GeographyAnswer", "geography_answers", 29
)

InformaticsAnswer = create_answer_model(
    "InformaticsAnswer", "informatics_answers", 27
)

LiteratureAnswer = create_answer_model(
    "LiteratureAnswer", "literature_answers", 11
)

GermanAnswer = create_answer_model(
    "GermanAnswer", "german_answers", 42
)

FrenchAnswer = create_answer_model(
    "FrenchAnswer", "french_answers", 42
)

SpanishAnswer = create_answer_model(
    "SpanishAnswer", "spanish_answers", 42
)

ChineseAnswer = create_answer_model(
    "ChineseAnswer", "chinese_answers", 32
)