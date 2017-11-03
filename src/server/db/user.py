from mongoengine import Document, EmailField, StringField


class User(Document):
    email = EmailField(required=True, unique=True)
    password = StringField()
    first_name = StringField()
    last_name = StringField()

    def get_hexdigest(self, algo, message, salt):
        """
        Encrypt a message
        """
        import hashlib
        import binascii
        return binascii.hexlify(hashlib.pbkdf2_hmac(algo, message, salt, 100000))

    def set_password(self, raw_password):
        """
        set the password
        """
        import random
        algo = 'sha256'
        salt = self.get_hexdigest(
            algo, str(random.random()), str(random.random()))[:5]
        hsh = self.get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%s' % (algo, salt, hsh)
        return self

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        encryption formats behind the scenes.
        """
        if self.password is None:
            return False
        algo, salt, hsh = self.password.split('$')
        return hsh == self.get_hexdigest(algo, salt, raw_password)
