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

class bsizeTest(unittest.TestCase):

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
    def test_bsize_320x480(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_bsize_320x480.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep -ic "bsize=320x480" /home/xad/rti_test/Mqueries_processedManualCheck'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for bsize 320x480 failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for bsize 320x480 passed', passed
        else:
            failed = failed + 1
            print 'Test case for bsize 320x480 failed', failed


    def test_bsize_320x50(self):
        # Creating Ad Document
        passed = 0
        failed = 0


        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_bsize_320x50.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep -ic "bsize=320x50" /home/xad/rti_test/Mqueries_processedManualCheck'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for bsize 320x50 failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for bsize 320x50 passed', passed
        else:
            failed = failed + 1
            print 'Test case for bsize 320x50 failed', failed

    def test_bsize_728x90(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_bsize_728x90.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        COMMAND = 'grep -ic "bsize=728x90" /home/xad/rti_test/Mqueries_processedManualCheck'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for bsize 728x90 failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for bsize 728x90 passed', passed
        else:
            failed = failed + 1
            print 'Test case for bsize 728x90 failed', failed

if __name__ == '__main__':
     unittest.main()
