python /home/xad/rti_test/ad_document_scripts/rti.py -a 901178 -j /home/xad/rti_test/ad_document_scripts/config.json | tee /home/xad/rti_test/test_scripts/rti_test.txt | tr -d '\000' | grep session | cut -d ' ' -f2>/home/xad/rti_test/test_scripts/key1.txt
