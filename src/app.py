from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! <3',
        'deployed_on': 'hello bro how are you !!! Ashish soni'
    })

@app.route('/api/v1/healthz')

def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

@app.route('/api/v1/dvj')

def sulekha():
    return jsonify({
        "Message": "Hello Sulekha Singh how are you doing, 🤷‍♂️"
    })

if __name__ == '__main__':

    app.run(host="0.0.0.0")

