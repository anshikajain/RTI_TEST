import time
import unittest
import os.path
import inspect
import sys
script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
testUtilDir = '/media/ephemeral0/xad/rti_test/testUtil'
sys.path.insert(0, testUtilDir)
from executeCmd import *
import threading


class postConditionTest:

    mExecCmd = executeCmd()

    def post_condition_for_test(self):

        #Stop RTI Broker
        COMMAND = "sh /home/xad/rti_test/set_up_scripts/rti_broker_stop.sh"
        self.mExecCmd.execute_command(COMMAND)

