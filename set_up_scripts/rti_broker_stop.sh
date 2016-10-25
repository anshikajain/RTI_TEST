#!/bin/bash
if ps aux | grep -v "grep" | grep "rtibroker"
then
    echo "Server is still running"
    # Getting the PID of the process
    PID=`pgrep rtibroker`
    kill $PID
    echo "Process has been killed"
else
    echo "No Process to kill"
fi   
