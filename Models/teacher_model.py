from tortoise.models import Model
from tortoise import fields

class Teacher(Model):
    __tablename__ = "teachers"
    
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20, min_length=5)
    username = fields.CharField(max_length=20, unique=True, min_length=5)
    password = fields.CharField(max_length=100, min_length=5)

    class Config():
        orm_mode = True