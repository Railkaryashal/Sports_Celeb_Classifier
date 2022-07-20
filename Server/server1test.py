from flask import Flask, request, jsonify

app = Flask(__name__)


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    app.run(port=5000)