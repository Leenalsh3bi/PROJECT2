from flask import Flask, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from gp1-demo!",
        "status": "ok"
    })

if name == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
