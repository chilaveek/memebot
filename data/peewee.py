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
    class Meta:
        database = db
