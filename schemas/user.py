from pydantic import BaseModel

class UserLogReg(BaseModel):
    name: str
    password: str