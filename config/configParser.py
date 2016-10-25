from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('/Users/anshikajain/PycharmProjects/test/RTI_TESTS/config/config.cfg')

g_neptune_serving_host=parser.get('neptune_serving', 'host')
g_rti_index_host=parser.get('rti_index', 'host')
g_rti_serving_host=parser.get('rti_serving', 'host')
