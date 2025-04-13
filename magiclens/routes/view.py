from flask import Blueprint, render_template

view_image_bp = Blueprint('view_image_bp', __name__)

@view_image_bp.route('/image/upload')
def upload_image():
    return render_template('upload_image.html')


@view_image_bp.route('/image/<filename>')
def show_image(filename: str):
    return render_template('show_image.html', filename=filename)
