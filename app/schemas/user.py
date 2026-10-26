from pydantic import BaseModel

class CreateUser(BaseModel):
    Name: str
    Age: str