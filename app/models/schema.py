from pydantic import BaseModel

class Task(BaseModel):
    id: int
    status: str
