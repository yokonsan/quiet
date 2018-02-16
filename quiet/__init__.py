from flask import Flask, render_template

from generate import Generate


app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

gen = Generate()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

from . import main, api, admin
from .api import api
from .admin import admin

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(admin, url_prefix='/admin')
