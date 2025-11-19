from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Nwoke ECS Container. Version 2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
