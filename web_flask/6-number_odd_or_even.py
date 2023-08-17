#!/usr/bin/python3
"""
Starts flask web application listening on 0.0.0.0, port 5000
Routes:
/: display Hello HBNB!
/hbnb: display HBNB
/c/<text>: display "C" followed by the value of the text variable
/python/(<text>): display "Python", followed by the value of text variable
        (replace underscore _ symbols with a space)
/number/<n>: display "n is a number" only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer
/number_odd_or_even/<n>: display a HTML page only if n is an integer
"""


from flask import Flask, escape, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
        """displays Python followed by whatever text is given"""
        return "Python {}".format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        """displays n only if n is an integer"""
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
        """display a HTML page only if n is an integer"""
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
	"""displays a HTML page only if n is an integer"""
	return render_template('6-number_odd_or_even.html', number=n, odd_even='odd' if n % 2 != 0 else 'even')


@app.route('/airbnb-dynamic/number_odd_or_even/<int:n>', strict_slashes=False)
def airbnb_odd_or_even(n):
        """displays a HTML page only if n is an integer"""
        return render_template('6-number_odd_or_even.html', number=n, odd_even='odd' if n % 2 != 0 else 'even')


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001)
