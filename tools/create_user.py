"""
Temporary user creation tool
"""
from mongoengine import connect
from server.db.user import User

connect('prosper-cr')
User(email='ddesmarest@gmail.com').set_password('david').save()