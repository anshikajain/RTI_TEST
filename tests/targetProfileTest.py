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


class targetProfileTest(unittest.TestCase):

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
    def test_carrier_att(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_carrier_att.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep -ic "carrier=att" /home/xad/rti_test/Mqueries_processedManualCheck'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Carrier ATT failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for Carrier ATT passed', passed
        else:
            failed = failed + 1
            print 'Test case for Carrier ATT failed', failed

########################################TEST CASE for GENDER##########################################################################
    def test_gen_m(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_gen_m.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep -ic "gen=m" /home/xad/rti_test/Mqueries_processedManualCheck'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Gen M failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for Gen M passed', passed
        else:
            failed = failed + 1
            print 'Test case for Gen M failed', failed

    def test_gen_f(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_gen_f.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep -ic "gen=f" /home/xad/rti_test/Mqueries_processedManualCheck'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Gen F failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for Gen F passed', passed
        else:
            failed = failed + 1
            print 'Test case for Gen F failed', failed

    def test_age_13_17(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_age_13-17.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'more /home/xad/rti_test/Mqueries_processedManualCheck | grep -c "age=[1][3-7]" -o'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for age 13-17 failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for age 13-17 passed', passed
        else:
            failed = failed + 1
            print 'Test case for age 13-17 failed', failed

    def test_age_25_34(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_age_25-34.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'more /home/xad/rti_test/Mqueries_processedManualCheck | grep -c "age=[2][5-9]\|age=[3][0-4]" -o'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for age 25-34 failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for age 25-34 passed', passed
        else:
            failed = failed + 1
            print 'Test case for age 25-34 failed', failed


    def test_age_55_64(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_age_55-64.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'more /home/xad/rti_test/Mqueries_processedManualCheck | grep -c "age=[5][5-9]\|age[6][0-5]" -o'
        print COMMAND
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for age 55-64 failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for age 55-64 passed', passed
        else:
            failed = failed + 1
            print 'Test case for age 55-64 failed', failed

if __name__ == '__main__':
    unittest.main()
