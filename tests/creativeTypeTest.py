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
    def test_type_html5(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_type_html5.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        str1 = "'{print $2;}'"
        str2 = "'{print $1}'"
        str3 = "'s/.&//'"
        COMMAND = 'grep -Po "o_fmt=.*?&" /home/xad/rti_test/Mqueries_processedManualCheck | awk -F= ' + str1 + ' | awk -F\& ' + str2 +' | sed ' + str3 + ' | grep -ic "html5"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis >= hits_from_query_file * 95 / 100, "Test case for type html5 failed"

        if hits_from_redis >= hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for type html5 passed', passed
        else:
            failed = failed + 1
            print 'Test case for type html5 failed', failed


    def test_type_video(self):
        # Creating Ad Document
        passed = 0
        failed = 0


        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_type_video.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        str1 = "'{print $2;}'"
        str2 = "'{print $1}'"
        str3 = "'s/.&//'"
        COMMAND = 'grep -Po "o_fmt=.*?&" /home/xad/rti_test/Mqueries_processedManualCheck | awk -F= ' + str1 + ' | awk -F\& ' + str2 +' | sed ' + str3 + ' | grep -ic "video"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis >= hits_from_query_file * 95 / 100, "Test case for type video failed"

        if hits_from_redis >= hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for type video passed', passed
        else:
            failed = failed + 1
            print 'Test case for type video failed', failed

    def test_type_script(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_type_script.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        str1 = "'{print $2;}'"
        str2 = "'{print $1}'"
        str3 = "'s/.&//'"
        COMMAND = 'grep -Po "o_fmt=.*?&" /home/xad/rti_test/Mqueries_processedManualCheck | awk -F= ' + str1 + ' | awk -F\& ' + str2 +' | sed ' + str3 +' | grep -ic "exp"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis >= hits_from_query_file * 95 / 100, "Test case for type script failed"

        if hits_from_redis >= hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for type script passed', passed
        else:
            failed = failed + 1
            print 'Test case for type script failed', failed

    def test_type_native(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_type_native.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        str1 = "'{print $2;}'"
        str2 = "'{print $1}'"
        str3 = "'s/.&//'"
        COMMAND = 'grep -Po "o_fmt=.*?&" /home/xad/rti_test/Mqueries_processedManualCheck | awk -F= ' + str1 + ' | awk -F\& ' + str2 +' | sed ' + str3 +' | grep -ic "native"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis >= hits_from_query_file * 95 / 100, "Test case for type native failed"

        if hits_from_redis >= hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for type native passed', passed
        else:
            failed = failed + 1
            print 'Test case for type native failed', failed


    def test_type_hero(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_type_hero.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        str1 = "'{print $2;}'"
        str2 = "'{print $1}'"
        str3 = "'s/.&//'"
        COMMAND = 'grep -Po "o_fmt=.*?&" /home/xad/rti_test/Mqueries_processedManualCheck | awk -F= ' + str1 + ' | awk -F\& ' + str2 +' | sed ' + str3 +' | grep -ic "hero"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis >= hits_from_query_file * 95 / 100, "Test case for type hero failed"

        if hits_from_redis >= hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for type hero passed', passed
        else:
            failed = failed + 1
            print 'Test case for type hero failed', failed

if __name__ == '__main__':
     unittest.main()
