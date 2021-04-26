from peewee import *

db = SqliteDatabase('user.db')

class User(Model):
    name = CharField()
    username = CharField()
    sex = CharField()
    email = CharField()
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    class Meta:
        database = db