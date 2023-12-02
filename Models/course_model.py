from tortoise.models import Model
from tortoise import fields

class Course(Model):
    __tablename__ = "courses"
    
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=20, min_length=5)
    description = fields.CharField(max_length=100, min_length=5)
    instructor = fields.CharField(max_length=20, min_length=5)