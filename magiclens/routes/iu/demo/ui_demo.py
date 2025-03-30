from flask import Blueprint, render_template

ui_demo = Blueprint('ui_demo', __name__)

@ui_demo.route('/upload-image')
def demo():
    return render_template('show_image.html')


@ui_demo.route('/show-image/<filename>')
def show_image(filename: str):
    return render_template('show_image.html', filename=filename)
