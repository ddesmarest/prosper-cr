"""
Common function for the tests
"""
import uuid
from mongoengine import connect
from mongoengine.connection import _get_db


def create_db(db_name):
    """Return dn_name
    Create a new database
    """
    full_name = db_name + '-' + str(uuid.uuid4())
    #print "\nCreate", full_name
    connect(full_name)
    return full_name


def drop_db(db_name):
    """
    Drop the given database
    """
    _get_db().client.drop_database(db_name)
    #print db_name, 'dropped'
