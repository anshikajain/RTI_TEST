import subprocess
import sys
import os
from threading import Timer

class executeCmd:

    def execute_command_background(self, COMMAND):
        ssh = subprocess.Popen(COMMAND,
                               shell=True)

    def execute_command(self,COMMAND):
        #kill = lambda process: process.kill()
        ssh = subprocess.Popen(COMMAND,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

        # killing the process after 20 seconds
        # my_timer = Timer(60, kill, [ssh])
        #
        # try:
        #     my_timer.start()
        #     stdout, stderr = ssh.communicate()
        # finally:
        #     my_timer.cancel()

        result = ssh.stdout.readlines()
        if result == []:
             error = ssh.stderr.readlines()
             print >> sys.stderr, "NO OUTPUT FROM STDOUT: %s" % error
        else:
             print result
             return result

