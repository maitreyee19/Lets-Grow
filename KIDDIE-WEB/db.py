import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    db = mysql.connector.connect(
        host='localhost',
        user='lony',
        password='lony',
        database='KIDDIE'
    )
    return db


def init_db():
    db = get_db()
    cursor = db.cursor()
    for line in open('schema.sql'):
        if len(line) > 0:
            cursor.execute(line)


@click.command('init-db')
@with_appcontext
def init_db_commnd():
    init_db()
    click.echo('initialzied dba')


if '__main__' == __name__:
    init_db()
