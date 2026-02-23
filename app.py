from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/identity/<name>/age/<int:age>')
def identity_status(name, age):
    status = "an adult" if age >= 18 else "a minor"
    return jsonify({
        "message": f"Welcome {name}, you are {status}"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)