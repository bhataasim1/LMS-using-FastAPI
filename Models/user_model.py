from tortoise.models import Model
from tortoise import fields

class User(Model):
    __tablename__ = "users"
    
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True, min_length=5)
    password = fields.CharField(max_length=100, min_length=5)

    class Config():
        orm_mode = True