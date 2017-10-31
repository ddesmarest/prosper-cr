"""
Basic types module
"""
import basic_types

FACTORY = basic_types.BasicTypeFactory()
FACTORY.register_type(basic_types.IntType())
FACTORY.register_type(basic_types.StringType())
FACTORY.register_type(basic_types.ChoiceType())

