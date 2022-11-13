from peewee import *

db = SqliteDatabase('bot.db', pragmas={'foreign_keys': 1})


class User(Model):
    id = PrimaryKeyField(unique=True)
    username = CharField()
    count = IntegerField()
    lastbuy = CharField()

    class Meta():
        database = db
        order_by = 'id'


class Liquid(Model):
    id = PrimaryKeyField(unique=True)
    flavor = CharField()
    price = IntegerField()
    line_id = ForeignKeyField(Line, backref='products')

    class Meta():
        database = db
        order_by = 'id'


if __name__ == '__main__':
    db.create_tables([User, Liquid])
