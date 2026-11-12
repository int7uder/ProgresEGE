from pydantic import BaseModel, Field


class ExamCreate(BaseModel):
    subject_id: int
    runtime: int = Field(ge=0)
    answers: dict[str, int]