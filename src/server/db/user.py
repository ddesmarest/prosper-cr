from mongoengine import Document, EmailField,StringField


class User(Document):
    email = EmailField(required=True, unique=True)
    first_name = StringField()
    last_name = StringField()
