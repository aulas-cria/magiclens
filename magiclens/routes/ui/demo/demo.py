from flask import Blueprint, render_template

demo_bp = Blueprint('demo', __name__)

@demo_bp.route('/upload-image')
def upload_image():
    return render_template('upload_image.html')


@demo_bp.route('/show-image/<filename>')
def show_image(filename: str):
    return render_template('show_image.html', filename=filename)
