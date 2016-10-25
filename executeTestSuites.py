import unittest
import os.path
import inspect
import sys
script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
testDir = '/media/ephemeral0/xad/rti_test/tests'
sys.path.insert(0, testDir)
from geoTargetTest import *
from targetProfileTest import *
from genWithGeoTarget import *



##############################RUNNING ALL TEST SUITES################################################################
if __name__ == '__main__':
    test_classes_to_run = [geoTargetTest,targetProfileTest,genWithGeoTarget]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)


