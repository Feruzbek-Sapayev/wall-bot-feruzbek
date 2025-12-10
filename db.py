from peewee import *

db = SqliteDatabase('test.db')

class User(Model):
    telegram_id = IntegerField()
    name = CharField(null=True)

    class Meta:
        database = db


class Theme(Model):
    name = CharField()
    link = CharField()

    class Meta:
        database = db



# # create
# User.create(name="Ali", age=20)

# read
# users = User.select()
# for u in users:
#     print(u.name, u.age)

db.connect()
db.create_tables([User])
db.create_tables([Theme])