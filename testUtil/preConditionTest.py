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


class preConditionTest:

    mExecCmd = executeCmd()
    mRTIBrokerThread = None

    def pre_condition_for_test(self):
        self.rti_broker_worker()

    def rti_broker_worker(self):
        mExecCmd = executeCmd()
        print "Starting rti broker"
        """thread worker function"""
        COMMAND ="sh /home/xad/rti_test/set_up_scripts/rti_broker_consume.sh"
        mExecCmd.execute_command_background(COMMAND)
        print 'started rti broker thread'

    def start_rti_broker(self):
        self.mRTIBrokerThread =  threading.Thread(target=self.rti_broker_worker())
        self.mRTIBrokerThread.setDaemon(True)
        self.mRTIBrokerThread.start()
        print 'Starting rti broker thread'

    # Start the Redis Server
    def start_redis_server(self):
        COMMAND ="sh /home/xad/rti_test/set_up_scripts/redis_rti_start.sh"
        self.mExecCmd.execute_command(COMMAND)

    # Start RTI Serving Server
    def start_redis_server(self):
        COMMAND ="sh /home/xad/rti_test/set_up_scripts/server_start.sh"
        self.mExecCmd.execute_command(COMMAND)
