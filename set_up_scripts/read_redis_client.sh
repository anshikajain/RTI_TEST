paste -d "" /home/xad/rti_test/test_scripts/key2.txt /home/xad/rti_test/test_scripts/key1.txt > /home/xad/rti_test/test_scripts/key3.txt
cat /home/xad/rti_test/test_scripts/key3.txt | redis-cli -h 127.0.0.1 -p 6379
rm /home/xad/rti_test/test_scripts/key3.txt /home/xad/rti_test/test_scripts/key1.txt
rm /home/xad/rti_test/test_scripts/rti_test.txt
