"""
User field tests
"""
import unittest
import json
from server.db.template.field import UserField


class UserFieldTests(unittest.TestCase):
    """
    Basic types tests
    """

    def test_user_field(self):
        """
        Test all the feature for UserField
        """
        field = UserField(name="test_int", container="int").initialize()
        container = field.get_containter_type()
        self.assertIsNotNone(container)
        self.assertEquals(field.configuration,
                          container.create_configuration())

    def test_choice_field(self):
        """
        Test feature for choice field
        """
        field = UserField(name="test_choice", container="choice").initialize()
        field.tooltip = "Please help me !!!"
        field.validate_configuration()
        field.configuration = {'last_index': 1,
                               'choices': [[1, 'Choice 1']]}
        field.validate_configuration()
        json_field = field.to_json()
        dictionary = json.loads(json_field)
        self.assertEquals(str(field.uuid), dictionary['id'])
        self.assertEquals(field.name, dictionary['name'])
        self.assertEquals(field.container, dictionary['container'])
        self.assertEquals(field.tooltip, dictionary['tooltip'])
        self.assertEquals(field.configuration, dictionary['configuration'])
        