from peewee import *
from data import config
import psycopg2

db = PostgresqlDatabase(
    'humans',
    port=5432,
    user=config.PG_USER,
    password=config.PG_PASS,
    host=config.ip
)


class Human(Model):
    id_primary = PrimaryKeyField(primary_key=1)
    id = IntegerField()
    username = CharField(null=True)
    name = CharField(default='none')
    age = IntegerField(null=True)
    mode = CharField(default='Шакализатор')
    void = IntegerField(null=True)
    memes = IntegerField(default=0)
    class Meta:
        database = db

class Words(Model):
    id_primary = PrimaryKeyField(primary_key=1)
    phrase = CharField()
    class Meta:
        database = db