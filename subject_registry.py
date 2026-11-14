from database import SessionLocal
from models.subject import Subject
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

SUBJECTS = [
    {
        "name": "Обществознание",
        "model": SocietyAnswer,
    },
    {
        "name": "Русский язык",
        "model": RussianAnswer,
    },
    {
        "name": "Английский язык",
        "model": EnglishAnswer,
    },
    {
        "name": "Математика (профиль)",
        "model": MathProfileAnswer,
    },
    {
        "name": "Математика (база)",
        "model": MathBasicAnswer,
    },
    {
        "name": "Физика",
        "model": PhysicsAnswer,
    },
    {
        "name": "Химия",
        "model": ChemistryAnswer,
    },
    {
        "name": "Биология",
        "model": BiologyAnswer,
    },
    {
        "name": "История",
        "model": HistoryAnswer,
    },
    {
        "name": "География",
        "model": GeographyAnswer,
    },
    {
        "name": "Информатика",
        "model": InformaticsAnswer,
    },
    {
        "name": "Литература",
        "model": LiteratureAnswer,
    },
    {
        "name": "Немецкий язык",
        "model": GermanAnswer,
    },
    {
        "name": "Французский язык",
        "model": FrenchAnswer,
    },
    {
        "name": "Испанский язык",
        "model": SpanishAnswer,
    },
    {
        "name": "Китайский язык",
        "model": ChineseAnswer,
    },
]



def create_subjects():
    with SessionLocal() as session:
        for item in SUBJECTS:
            subject = session.query(Subject).filter_by(
                name=item["name"]
            ).first()

            if not subject:
                session.add(Subject(name=item["name"]))

        session.commit()