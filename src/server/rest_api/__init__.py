import traceback


def create_error_data(message, exception):
    """
    Build dictionary containing the error
    """
    return {'message': message,
            'error': exception.message,
            'stack': traceback.format_exc()}
