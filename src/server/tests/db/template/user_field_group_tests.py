"""
User field tests
"""
import unittest
import json
from mongoengine import connect
from server.db.template.field import UserFieldGroup, UserField, EmbeddedDocumentField


class UserFieldTests(unittest.TestCase):
    """
    Basic types tests
    """

    def setUp(self):
        self.db_ = connect('test_user_field_group')

    def tearDown(self):
        self.db_.drop_database('test_user_field_group')

    def test_user_field_group(self):
        """
        Basic field group test
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
        json_group = group.to_json()
        dictionary = json.loads(json_group)
        self.assertEquals(str(group.id), dictionary['id'])
        self.assertEquals(group.name, dictionary['name'])
        self.assertEquals('', dictionary['tooltip'])
        self.assertEquals(str(group.fields[0].uuid), dictionary['fields'][0]['id'])
        group.tooltip = "Help !!!"
        json_group = group.to_json()
        dictionary = json.loads(json_group)
        self.assertEquals(group.name, dictionary['name'])
        self.assertEquals(group.tooltip, dictionary['tooltip'])
        group.save()
        