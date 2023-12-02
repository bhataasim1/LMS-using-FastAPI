from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator
from Models.teacher_model import Teacher

getTeacherSchema = pydantic_model_creator(Teacher, name="Teacher")

class createTeacher(BaseModel):
    name: str = Field(..., min_length=5, max_length=20, unique=True, example="aasim")
    username: str = Field(..., min_length=5)
    password: str = Field(..., min_length=5, example="aasim123")

class loginTeacher(BaseModel):
    username: str = Field(..., example="aasim")
    password: str = Field(..., example="aasim123")
