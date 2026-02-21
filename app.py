
from flask import Flask, jsonify
from house_name import return_arnold

app = Flask(__name__)


@app.route('/')
def arnold():
    house = return_arnold("kannamkulath")
    return jsonify({"message": f"Welcome to {house}"})



@app.route('/api/status/<name>')
def status(name):
    return jsonify({"status": f"welcome to {name} house"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
