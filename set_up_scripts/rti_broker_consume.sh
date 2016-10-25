#!/bin/sh
if ps aux | grep -v "grep" | grep "rtibroker"
then
    echo "Server is still running"
    # Getting the PID of the process
    PID=`pgrep rtibroker`
    kill -9 $PID
    echo "Process has been killed"
    /home/xad/neptune/bin/rtibroker -k /home/xad/neptune/conf/serving/RTIInventoryKafka.conf -c RTIFastBitBroker -s 127.0.0.1 -p 6379 -g 1
else
    echo "No Process to kill"
    /home/xad/neptune/bin/rtibroker -k /home/xad/neptune/conf/serving/RTIInventoryKafka.conf -c RTIFastBitBroker -s 127.0.0.1 -p 6379 -g 1
fi


















