import time
import unittest
import os.path
import inspect
import sys
script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
testUtilDir = '/media/ephemeral0/xad/rti_test/testUtil'
sys.path.insert(0, testUtilDir)
from executeCmd import *
from getRedisOutput import *
from preConditionTest import *
from postConditionTest import *

class genWithGeoTarget(unittest.TestCase):

    g_ExecCmd = executeCmd()
    g_PreConditionTest = preConditionTest()
    g_PostConditionTest = postConditionTest()
    g_getRedisOutput = getRedisOutput()


#################################Running PreConditions################################################
    @classmethod
    def setUpClass(self):
        self.g_PreConditionTest.pre_condition_for_test()

#################################Running PostCondiitons#################################################
    @classmethod
    def tearDownClass(self):
        self.g_PostConditionTest.post_condition_for_test()

    ########################################TEST CASE for CARRIER##########################################################################
    def test_gen_state_ca(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_gen_stateca.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep "gen=m" /home/xad/rti_test/Mqueries_processedManualCheck | grep -c "state=ca"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Gen_StateCA failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for Gen_StateCA passed', passed
        else:
            failed = failed + 1
            print 'Test case for Gen_StateCA failed', failed


    def test_gen_state_e(self):
        # Creating Ad Document
        passed = 0
        failed = 0


        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_gen_statee.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep "gen=f" /home/xad/rti_test/Mqueries_processedManualCheck | grep -c "state=e"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Gen_stateE failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for Gen_stateE passed', passed
        else:
            failed = failed + 1
            print 'Test case for Gen_stateE failed', failed

    def test_gen_country(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_gen_country.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep "gen=m" /home/xad/rti_test/Mqueries_processedManualCheck | grep -c "country=jp"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Gen_Country failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for Gen_Country passed', passed
        else:
            failed = failed + 1
            print 'Test case for Gen_Country failed', failed

    def test_gen_city(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_gen_city.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep "gen=m" /home/xad/rti_test/Mqueries_processedManualCheck | grep -c "city=tampa"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Gen_City failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for Gen_City passed', passed
        else:
            failed = failed + 1
            print 'Test case for Gen_City failed', failed

if __name__ == '__main__':
     unittest.main()
