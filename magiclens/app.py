import os

from flask import Flask, redirect

from magiclens.routes.view import view_image_bp
from magiclens.routes.api import api_image_bp


app = Flask(__name__)

app.register_blueprint(view_image_bp, url_prefix='/view')
app.register_blueprint(api_image_bp, url_prefix='/api')

@app.route('/')
def index():
    return redirect(location='/view/image/upload', code=302)
