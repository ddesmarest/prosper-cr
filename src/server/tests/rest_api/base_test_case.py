"""
This module contain all the classes that are needed to the REST API tests
"""

from server.prosper_cr_server import ProsperCR
import ConfigParser


class BaseTestCase(object):
    """
    This class contains all the rest server initilization needed for
    the tests
    """

    TEST_DATABASE = 'test_prosper_cr_server'

    def init_server(self):
        """
        create a configuration with a test database and start the server
        """
        config = ConfigParser.RawConfigParser()
        config.add_section('db')
        config.set('db', 'name', BaseTestCase.TEST_DATABASE)
        self.server = ProsperCR(config)
        self.app = self.server.test_client()

    def finalize_server(self):
        """
        erase the test database
        """
        self.server.get_db_connection().drop_database(BaseTestCase.TEST_DATABASE)
