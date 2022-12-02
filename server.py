"""Server for coffee mate."""

from flask import (Flask, render_template, request, flash, session, redirect)
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "coffee"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Returns homepage."""

    return render_template('homepage.html')

@app.route('/coffee-types')
def coffee_types():
    """Returns page explaing different coffees."""

    return render_template('coffee-types.html')

@app.route('/secret-menu')
def secret_menu():
    """Returns page that goes over secret menu flavors."""

    return render_template('secret-menu.html')

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)