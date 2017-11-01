"""
This module contains all the basic type
that can be used for template field creation
"""


class BasicType(object):
    """
    represent a basic type
    """

    def __init__(self, id, name):
        self.name_ = name
        self.id_ = id

    def get_id(self):
        """
        id of the type
        """
        return self.id_

    def get_name(self):
        """
        name of the type
        """
        return self.name_

    def create_instance(self):
        """
        Create an instance of this type. Should be implemented by
        inherited classes
        """
        raise Exception('Should be implemented by subclass')

    def create_configuration(self):
        """
        Create an instance of the configuration for this type. Should be implemented by
        inherited classes if needed
        """
        return {}

    def validate_configuration(self, configuration):
        """
        Validate the configuration dictionary. Should be implemented by
        inherited classes
        """
        if configuration == {}:
            return True, ''
        else:
            return False, 'Configuration should be an empty dictionary'


class StringType(BasicType):
    """
    represent a string
    """

    def __init__(self):
        super(StringType, self).__init__('string', 'String')

    def create_instance(self):
        return ""


class IntType(BasicType):
    """
    represent a int
    """

    def __init__(self):
        super(IntType, self).__init__('int', 'Integer')

    def create_instance(self):
        return 0

def validate_choice_type(choice):
    """Return bool, message
    verify that all the object type in the choice are valid
    """
    if not (isinstance(choice, list) and len(choice) == 2
            and isinstance(choice[0], int) and isinstance(choice[1], str)):
        return False, "Each choice should be : [int,string]" + str(choice)
    else:
        return True, None


def validate_choice_values(choice, keys, values, last_index):
    """Return bool,message
    verify that the key and the value of the choice are valid and not
    duplicated
    """
    if choice[0] in keys:
        return False, str(choice) + " contains a duplicated index"
    if choice[1] in values:
        return False, str(choice) + " contains a duplicated value"
    if choice[0] > last_index:
        return False, str(choice) + " has an index greater than the last_index: " + str(last_index)
    return True, None


def validate_choices(choices, last_index):
    """
    Validator for choices. Example of valid choices:
    [ [0,'Choice 1'],[1,'Choice 2'] ]
    """
    if not isinstance(last_index,int):
        return False, 'last_index should be an int'
    keys = {}
    values = {}
    for choice in choices:
        valid, message = validate_choice_type(choice)
        if not valid:
            return False, message
        valid, message = validate_choice_values(
            choice, keys, values, last_index)
        if not valid:
            return False, message
        keys[choice[0]] = None
        values[choice[1]] = None
    return True, None



class ChoiceType(BasicType):
    """
    represent a value that can be selected in a list of choices
    """

    def __init__(self):
        super(ChoiceType, self).__init__('choice', 'Choice')

    def create_instance(self):
        return -1

    def create_configuration(self):
        return {'last_index': 0, 'choices': []}

    def validate_configuration(self, configuration):
        if 'last_index' not in configuration:
            return False, 'last_index is missing'
        if 'choices' not in configuration:
            return False, 'choices is missing'
        if not isinstance(configuration['choices'], list):
            return False, 'choices should be a list'
        return validate_choices(configuration['choices'], configuration['last_index'])


class BasicTypeFactory(object):
    """
    This factory allows to manage basic types
    """

    def __init__(self):
        self.types_ = {}

    def register_type(self, new_type):
        """
        Register a type in the factory
        """
        assert new_type.get_id() not in self.types_
        self.types_[new_type.get_id()] = new_type

    def get_types(self):
        """ returns all the registered type ids
        """
        return self.types_.keys()

    def get_type(self, type_id):
        """ returns a type given its id
        """
        return self.types_[type_id]
