"""
Common db test function
"""
import uuid
from mongoengine import connect


def create_db(db_name=str(uuid.uuid4())):
    """Return a db connection
    create a new db
    """
    return db_name, connect(db_name)


def drop_db(db_connection, db_name):
    """
    Drop the db
    """
    db_connection.drop_database(db_name)
