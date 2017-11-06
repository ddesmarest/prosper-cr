"""
This module configures and runs a ProsperCR server
"""
from optparse import OptionParser
import ConfigParser
from server.prosper_cr_server import ProsperCR


def run_server():
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config_file", default="default.cfg",
                      help="where FILE is the name of the configuration file", metavar="FILE")
    (options,args) = parser.parse_args()
    config = ConfigParser.RawConfigParser()
    config.read(options.config_file)
    server = ProsperCR(config)
    debug = False
    if config.get('server','debug') == 'true':
        debug = True
    server.run( debug=debug, host=config.get('server','address'), port=int(config.get('server','port')))


if __name__ == "__main__":
    run_server()