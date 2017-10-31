"""
Basic types tests
"""
import unittest
from server.db.template.types import FACTORY
from server.db.template.types.basic_types import IntType, BasicType


class BasicTypeTests(unittest.TestCase):
    """
    Basic types tests
    """

    def setUp(self):
        pass

    def test_factory(self):
        """
        Test all the feature for the type factory
        """
        basic_type = BasicType('dummy', 'Dummy')
        self.assertRaises(Exception, FACTORY.register_type, (IntType()))
        self.assertRaises(Exception, basic_type.create_instance)
        self.assertEquals(3, len(FACTORY.get_types()))
        int_t = FACTORY.get_type('int')
        self.assertEquals(int, type(int_t.create_instance()))
        self.assertEquals({}, int_t.create_configuration())
        self.assertEquals('Integer', int_t.get_name())
        is_valid, message = int_t.validate_configuration({})
        self.assertTrue(is_valid)
        self.assertEquals('', message)
        str_t = FACTORY.get_type('string')
        self.assertEquals(str, type(str_t.create_instance()))
        self.assertEquals({}, str_t.create_configuration())
        self.assertEquals('String', str_t.get_name())
        choice_t = FACTORY.get_type('choice')
        self.assertEquals(-1, choice_t.create_instance())
        self.assertEquals({'last_index': 0, 'choices': []},
                          choice_t.create_configuration())
        self.assertEquals('Choice', choice_t.get_name())
        is_valid, message = int_t.validate_configuration(
            {'last_index': 0, 'choices': []})
        self.assertFalse(is_valid)
        self.assertNotEquals('', message)

    def test_choice(self):
        """
        Test choice type
        """
        choice_t = FACTORY.get_type('choice')
        is_valid, message = choice_t.validate_configuration(
            {'last_index': 0, 'choices': []})
        self.assertTrue(is_valid)
        self.assertEquals('', message)
        is_valid, message = choice_t.validate_configuration(
            {'choices': []})
        self.assertFalse(is_valid)
        is_valid, message = choice_t.validate_configuration(
            {'last_index': 0})
        self.assertFalse(is_valid)
        is_valid, message = choice_t.validate_configuration(
            {'last_index': 0, 'choices': 0})
        self.assertFalse(is_valid)
        is_valid, message = choice_t.validate_configuration(
            {'last_index': 1, 'choices': [[0, 'A'], [1, 'B']]})
        self.assertTrue(is_valid)
        to_be_tested = [[['A'], [1, 'B']],
                        [[0, 'A'], [0, 'B']],
                        [[0, 'A'], [1, 'A']]]
        for test in to_be_tested:
            is_valid, message = choice_t.validate_configuration(
                {'last_index': 1, 'choices': test})
            self.assertFalse(is_valid)
        is_valid, message = choice_t.validate_configuration(
            {'last_index': 0, 'choices': [[0, 'A'], [1, 'B']]})
        self.assertFalse(is_valid)
