"""
User field tests
"""
import unittest
import uuid
from mongoengine import connect
from server.db.template.field import UserFieldGroup, UserField, EmbeddedDocumentField
import server.tests

class UserFieldGroupTests(unittest.TestCase):
    """
    Test UserFieldGroup
    """

    def setUp(self):
        self.db_name = server.tests.create_db(self.__class__.__name__)
       
    def tearDown(self):
        server.tests.drop_db(self.db_name)

    def test_user_field_group(self):
        """
        * Test UserFieldGroup 
        """
        group = UserFieldGroup(name='Group 1')
        group.fields = []
        group.fields.append(
            UserField(name='Int field', container='int').initialize())
        group.save()
        uuid = group.fields[0].uuid
        group_load = UserFieldGroup.objects.all()
        self.assertEquals(1, len(group_load))
        self.assertEquals(uuid, group_load[0].fields[0].uuid)
        dictionary = group.to_dict()
        self.assertEquals(str(group.id), dictionary['id'])
        self.assertEquals(group.name, dictionary['name'])
        self.assertEquals('', dictionary['tooltip'])
        self.assertEquals(
            str(group.fields[0].uuid), dictionary['fields'][0]['id'])
        group.tooltip = "Help !!!"
        dictionary = group.to_dict()
        self.assertEquals(group.name, dictionary['name'])
        self.assertEquals(group.tooltip, dictionary['tooltip'])
        group.save()
