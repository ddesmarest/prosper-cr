"""
Temporary user creation tool
"""
from mongoengine import connect
from server.db.user import User

connect('prosper-cr')
User(email='ddesmarest@gmail.com', first_name='David',
     last_name='Desmarest').set_password('david').save()
