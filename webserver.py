from flask import Flask

app = Flask(__name__)


@app.route('/take_picture', methods=['GET'])
def take_picture():
    print('Take Picture')
    return 'Picture Taken!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000)
