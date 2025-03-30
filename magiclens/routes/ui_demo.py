from flask import Blueprint, render_template

ui_demo = Blueprint('ui_demo', __name__)

@ui_demo.route('/demo')
def demo():
    return render_template('demo.html')
