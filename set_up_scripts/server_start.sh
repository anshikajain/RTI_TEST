/usr/sbin/httpd -f /media/ephemeral0/xad/neptune//conf/marketplace/httpd.conf -k stop
sleep 2
/usr/sbin/httpd -f /media/ephemeral0/xad/neptune//conf/marketplace/httpd.conf -k start
