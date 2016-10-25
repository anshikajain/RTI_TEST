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
    def test_age_state_country_bsize_ctype_gen(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_coun_state_gen_bsize_ctype.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        str1 = "'{print $2;}'"
        str2 = "'{print $1}'"
        str3 = "'s/.&//'"
        COMMAND = 'grep "bsize=320x480" /home/xad/rti_test/Mqueries_processedManualCheck | grep -i "country=us" | grep "age=[2][5-9]\|age=[3][0-4]" | grep "gen=m" | grep "state=tx" | grep -Po "o_fmt=.*?&" | awk -F= ' + str1 + '| awk -F\& ' + str2 +' | sed ' + str3 + ' | grep -ic "html5"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for test_age_state_country_bsize_ctype_gen failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for test_age_state_country_bsize_ctype_gen  passed', passed
        else:
            failed = failed + 1
            print 'Test case for test_age_state_country_bsize_ctype_gen failed', failed

########################################TEST CASE for GENDER##########################################################################
    def test_age_country_bsize_ctype_gen(self):
        # Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_coun_gen_bsize_ctype.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis = int(hits_from_redis)
        print 'Number of hits from Redis:', hits_from_redis
        str1 = "'{print $2;}'"
        str2 = "'{print $1}'"
        str3 = "'s/.&//'"
        COMMAND = 'grep "bsize=320x480" /home/xad/rti_test/Mqueries_processedManualCheck | grep -i "country=us" | grep "age=[2][5-9]\|age=[3][0-4]" | grep "gen=m" | grep -Po "o_fmt=.*?&" | awk -F= ' + str1 + '| awk -F\& ' + str2 +' | sed ' + str3 + ' | grep -ic "html5"'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:', hits_from_query_file
        assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for test_age_country_bsize_ctype_gen failed"

        if hits_from_redis > hits_from_query_file * 95 / 100:
            passed = passed + 1
            print 'Test case for test_age_country_bsize_ctype_gen  passed', passed
        else:
            failed = failed + 1
            print 'Test case for test_age_country_bsize_ctype_gen failed', failed

if __name__ == '__main__':
    unittest.main()
