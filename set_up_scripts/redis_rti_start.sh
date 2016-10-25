#!/bin/bash
if ps aux | grep -v "grep" | grep "redis"
then
    echo "Server is still running"
    # Getting the PID of the process
    PID=`pgrep redis`
    kill $PID
    echo "Process has been killed"
    redis-server --daemonize yes
else
    echo "No Process to kill"
    redis-server --daemonize yes
fi   
