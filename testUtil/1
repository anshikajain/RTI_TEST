import time
import unittest
import os.path
import inspect
import sys
script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
testUtilDir = '/media/ephemeral0/xad/rti_test/testUtil'
sys.path.insert(0, testUtilDir)
from executeCmd import *

class getRedisOutput:

    mExecCmd = executeCmd()

    #Read from Redis Client
    def read_from_redis(self):
        COMMAND ="sh /home/xad/rti_test/set_up_scripts/read_redis_client.sh"
        return self.mExecCmd.execute_command(COMMAND)

    #Get Output from Redis Client
    def parse_redis_output(self, output):
        print 'Output from Redis Client:', output
        if output != ['\n']:
            hits = output[0].split(" ")[3].split(':')[1].split(',')[0]
            return hits
        else:
            print 'Redis Output is null'


