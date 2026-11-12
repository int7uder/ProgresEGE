from pydantic import BaseModel


class CreateUserSubject(BaseModel):
    subject_id: int