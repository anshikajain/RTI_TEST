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

class geoTargetTest(unittest.TestCase):

    g_ExecCmd = executeCmd()
    g_PreConditionTest = preConditionTest()
    g_getRedisOutput = getRedisOutput()
    g_PostConditionTest = postConditionTest()


#################################Running PreConditions################################################
    @classmethod
    def setUpClass(self):
        self.g_PreConditionTest.pre_condition_for_test()

#################################Running PostCondiitons#################################################
    @classmethod
    def tearDownClass(self):
        self.g_PostConditionTest.post_condition_for_test()

###########################GEO TARGET TESTS########################################


###########################STATE TEST###########################################



    def test_state_ca(self):

        #Creating Ad Document
        passed = 0
        failed = 0

        COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_state_ca.sh"
        self.g_ExecCmd.execute_command(COMMAND)
        time.sleep(10)
        hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
        hits_from_redis=int(hits_from_redis)
        print 'Number of hits from Redis:',hits_from_redis
        COMMAND = 'grep -ic "state=ca" /home/xad/rti_test/Mqueries_processedManualCheck'
        hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
        hits_from_query_file = int(hits_from_query_file[0])
        print 'Number of hits from query file:',hits_from_query_file
        assert hits_from_redis > hits_from_query_file  * 95/100, "Test case for State_CA failed"
        if hits_from_redis > (hits_from_query_file  * 95)/100:
            passed = passed + 1
            print 'Test case for State_CA passed',passed
        else:
            failed = failed +1
            print 'Test case for State_CA failed',failed

    def test_state_e(self):

         #Creating Ad Document
         passed = 0
         failed = 0

         COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_state_e.sh"
         self.g_ExecCmd.execute_command(COMMAND)
         time.sleep(10)
         hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
         print 'Number of hits from Redis:', hits_from_redis
         hits_from_redis=int(hits_from_redis)
         COMMAND = 'grep -ic "state=e" /home/xad/rti_test/Mqueries_processedManualCheck'
         hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
         hits_from_query_file = int(hits_from_query_file[0])
         print 'Number of hits from query file:', hits_from_query_file
         assert hits_from_redis > (hits_from_query_file * 95) / 100, "Test case for State_E failed"
         print hits_from_query_file * 95 / 100
         if hits_from_redis > hits_from_query_file * 95 / 100:
             passed = passed + 1
             print 'Test case for State_E passed', passed
         else:
             failed = failed + 1
             print 'Test case for State_E failed', failed


######################################### CITY TEST#######################################################
    def test_city(self):
         #Creating Ad Document
         passed = 0
         failed = 0

         COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_city_cincinnati.sh"
         self.g_ExecCmd.execute_command(COMMAND)
         time.sleep(10)
         hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
         hits_from_redis = int(hits_from_redis)
         print 'Number of hits from Redis:', hits_from_redis
         COMMAND = 'grep -ic "city=cincinnati" /home/xad/rti_test/Mqueries_processedManualCheck'
         hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
         hits_from_query_file = int(hits_from_query_file[0])
         print 'Number of hits from query file:', hits_from_query_file
         assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for city_cincinnati failed"

         if hits_from_redis > hits_from_query_file * 95 / 100:
             passed = passed + 1
             print 'Test case for city_cincinnati passed', passed
         else:
             failed = failed + 1
             print 'Test case for city_cincinnati failed', failed

 #########################################ZIP TEST##############################################
    def test_zip_us_03275(self):
         #Creating Ad Document
         passed = 0
         failed = 0

         COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_zip_03275.sh"
         self.g_ExecCmd.execute_command(COMMAND)
         time.sleep(10)
         hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
         hits_from_redis = int(hits_from_redis)
         print 'Number of hits from Redis:', hits_from_redis
         COMMAND = 'grep -c "zip=03275" /home/xad/rti_test/Mqueries_processedManualCheck'
         hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
         hits_from_query_file = int(hits_from_query_file[0])
         print 'Number of hits from query file:', hits_from_query_file
         assert hits_from_redis > hits_from_query_file * 95/ 100, "Test case for zip_03275 failed"
         if hits_from_redis > hits_from_query_file * 95 / 100:
             passed = passed + 1
             print 'Test case for zip_03275 passed', passed
         else:
             failed = failed + 1
             print 'Test case for zip_03275 failed', failed

    def test_zip_in(self):
         #Creating Ad Document
         passed = 0
         failed = 0

         COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_zip_in.sh"
         self.g_ExecCmd.execute_command(COMMAND)
         time.sleep(10)
         hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
         hits_from_redis = int(hits_from_redis)
         print 'Number of hits from Redis:', hits_from_redis
         COMMAND = 'grep -c "zip=380002" /home/xad/rti_test/Mqueries_processedManualCheck'
         hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
         hits_from_query_file = int(hits_from_query_file[0])
         print 'Number of hits from query file:', hits_from_query_file
         assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for zip_in failed"
         if hits_from_redis > hits_from_query_file * 95 / 100:
             passed = passed + 1
             print 'Test case for zip_in passed', passed
         else:
             failed = failed + 1
             print 'Test case for zip_in failed', failed

##################################### COUNTRY TEST################################################
    def test_country_not_us(self):
         #Creating Ad Document
         passed = 0
         failed = 0

         COMMAND ="sh /home/xad/rti_test/test_scripts/ad_document_consume_country_de.sh"
         self.g_ExecCmd.execute_command(COMMAND)
         time.sleep(10)
         hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
         hits_from_redis = int(hits_from_redis)
         print 'Number of hits from Redis:', hits_from_redis
         COMMAND = 'grep -ic "country=de" /home/xad/rti_test/Mqueries_processedManualCheck'
         hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
         hits_from_query_file = int(hits_from_query_file[0])
         print 'Number of hits from query file:', hits_from_query_file
         assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Country_DE failed"

         if hits_from_redis > hits_from_query_file * 95 / 100:
             passed = passed + 1
             print 'Test case for Country_DE passed', passed
         else:
             failed = failed + 1
             print 'Test case for Country_DE failed', failed



    def test_country_us(self):
        #Creating Ad Document
         passed = 0
         failed = 0

         COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_country_us.sh"
         self.g_ExecCmd.execute_command(COMMAND)
         time.sleep(10)
         hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
         hits_from_redis = int(hits_from_redis)
         print 'Number of hits from Redis:', hits_from_redis
         COMMAND = 'grep -c "country=us" /home/xad/rti_test/Mqueries_processedManualCheck'
         hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
         hits_from_query_file = int(hits_from_query_file[0])
         print 'Number of hits from query file:', hits_from_query_file
         assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for Country_US failed"

         if hits_from_redis > hits_from_query_file * 95 / 100:
             passed = passed + 1
             print 'Test case for Country_US passed', passed
         else:
             failed = failed + 1
             print 'Test case for Country_US failed', failed

#########################################DMA_TEST###########################################
    def test_dma(self):
         #Creating Ad Document
         passed = 0
         failed = 0

         COMMAND = "sh /home/xad/rti_test/test_scripts/ad_document_consume_dma.sh"
         self.g_ExecCmd.execute_command(COMMAND)
         time.sleep(10)
         hits_from_redis = self.g_getRedisOutput.parse_redis_output(self.g_getRedisOutput.read_from_redis())
         hits_from_redis = int(hits_from_redis)
         print 'Number of hits from Redis:', hits_from_redis
         COMMAND = 'grep -c "dma=501" /home/xad/rti_test/Mqueries_processedManualCheck'
         hits_from_query_file = self.g_ExecCmd.execute_command(COMMAND)
         hits_from_query_file = int(hits_from_query_file[0])
         print 'Number of hits from query file:', hits_from_query_file
         hits_from_redis = int(hits_from_redis)
         assert hits_from_redis > hits_from_query_file * 95 / 100, "Test case for DMA failed"

         if hits_from_redis > hits_from_query_file * 95 / 100:
             passed = passed + 1
             print 'Test case for DMA passed', passed
         else:
             failed = failed + 1
             print 'Test case for DMA failed', failed



if __name__ == '__main__':
     unittest.main()
