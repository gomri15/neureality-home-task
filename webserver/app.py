# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

last_result = None


@app.route('/reverse', methods=['GET'])
def reverse_string():
    global last_result
    input_string = request.args.get('in', '')
    reversed_string = ' '.join(input_string.split()[::-1])
    last_result = reversed_string
    return jsonify({"result": reversed_string})


@app.route('/restore', methods=['GET'])
def restore_last_result():
    return jsonify({"result": last_result if last_result else "No result yet"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
