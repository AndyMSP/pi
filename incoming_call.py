from flask import Flask
import subprocess
import time
import os

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def incoming_call():
    my_env = os.environ.copy()
    subprocess.Popen(['sudo', '-u', 'andy', 'chromium-browser', '--no-sandbox', 'https://web-01.tacobell.tech/pi/grandma'])
    print('testing')
    return 'f'