from typing import Optional
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator
from Models.course_model import Course

getCourseSchema = pydantic_model_creator(Course, name="course")

class createCourse(BaseModel):
    title: str = Field(..., min_length=5, max_length=50, example="Learn Python")
    description: str = Field(..., min_length=5, example="This is the Course where you learn Python")
    instructor: str = Field(..., min_length=5, example="aasim")

class updateCourse(BaseModel):
    title:  Optional[str] = Field(..., example="Learn Python")
    description:  Optional[str] = Field(..., example="This is the Course where you learn Python")
    instructor:  Optional[str] = Field(..., example="Aasim")