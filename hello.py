import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<a href="hello">Hello World!</a>'

@app.route('/hello/')
def hello():
	return 'HELLO'

if __name__ == '__main__':
	app.run()