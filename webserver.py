import time

from flask import Flask
import RPi.GPIO as GPIO

focus_pin = 20
picture_pin = 21

app = Flask(__name__)


@app.route('/take_picture', methods=['GET'])
def take_picture():
    print('Take Picture')
    GPIO.output(focus_pin, True)
    time.sleep(0.1)
    GPIO.output(picture_pin, True)
    time.sleep(0.1)
    GPIO.output(focus_pin, False)
    GPIO.output(focus_pin, False)
    return 'Picture Taken!'


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(focus_pin, GPIO.OUT)
    GPIO.setup(picture_pin, GPIO.OUT)

    app.run(host='0.0.0.0', threaded=True, port=5000)
