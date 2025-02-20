#!/usr/bin/python3
"""
Starts flask web application listening on 0.0.0.0, port 5000
Routes:
/: display Hello HBNB!
/hbnb: display HBNB
/c/<text>: display "C" followed by the value of the text variable
	(replace underscore _ symbols with a space)
"""


from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""displays Hello HBNB"""
	return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""displays HBNB"""
	return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
	"""displays C followed by whatever text is given"""
	return "C {}".format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000) 
