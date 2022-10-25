from flask import Flask
import subprocess
import time

app = Flask(__name__)


@app.route('/incoming_call', strict_slashes=False)
def incoming_call():
    subprocess.Popen(['chromium-browser', '--new-window', '--start-fullscreen', 'https://everybodysweb.com/call/pi/demo'])
    subprocess.run(['bash', 'tv_on.sh'])
    return 'received'


@app.route('/end_call', strict_slashes=False)
def end_call():
    subprocess.run(['pkill', 'chromium'])
    subprocess.run(['bash', 'tv_off.sh'])
    return 'complete'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)