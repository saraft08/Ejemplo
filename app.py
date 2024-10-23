from flask import Flask, jsonify

app = Flask(_name_)


def home():
    return jsonify(message="Hello from Flask on Vercel!")

