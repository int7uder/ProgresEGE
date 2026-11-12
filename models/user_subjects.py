from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class UserSubject(Base):
    __tablename__ = "user_subjects"
    __table_args__ = (UniqueConstraint('user_id', 'subject_id'),)
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    is_active: Mapped[bool] = mapped_column(default=True)
