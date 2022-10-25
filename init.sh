#!/usr/bin/bash
# Run this script as andy every time pi is started up -> "bash init.py"
# Place link to this script on desktop
cd /home/andy/pi
pkill gunicorn
/home/andy/.local/bin/gunicorn --workers 2 --bind 0.0.0.0:5001 dispatcher:app --daemon
sudo service nginx restart
