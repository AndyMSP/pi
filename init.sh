#!/usr/bin/bash
# Run this script as sudo every time pi is started up -> "sudo bash init.py"
cd /home/andy/pi
pkill gunicorn
/home/andy/.local/bin/gunicorn --workers 2 --bind 0.0.0.0:5001 incoming_call:app
service nginx restart
