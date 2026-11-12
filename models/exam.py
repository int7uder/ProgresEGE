from database import Base
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Exam(Base):
    __tablename__ = 'exams'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'))
    primary_score: Mapped[int]
    test_score: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    runtime: Mapped[int] = mapped_column(default=0)