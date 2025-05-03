import os

from flask import Blueprint, request, jsonify, redirect, url_for

from magiclens.storage.local_handler import LocalHandler
from magiclens.transform.transform_handler import TransformHandler

api_image_bp = Blueprint('api_image_bp', __name__)

@api_image_bp.route('/status')
def index():
    return {'message': 'Ok'}

@api_image_bp.route('/image', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']
    filename = file.filename

    if file.filename == '':
            return jsonify({"error": "Nome do arquivo vazio"}), 400
    
    filename = request.form.get('filename')
    if filename:
        filename = '.'.join([
            filename.split('.')[0],
            file.filename.split('.')[-1]
        ])
    else:
        filename = file.filename

    storage = LocalHandler()
    
    image_path = storage.save(
        filename=filename,
        content=file.read()
    )

    return redirect(
        location=url_for(
            endpoint='static', 
            filename=image_path
        ),
        code=302
    )


@api_image_bp.route('/image/<path:filename>', methods=['GET'])
def process(filename: str):
    height = request.args.get('h', type=int)
    width = request.args.get('w', type=int)
    flip = request.args.get('flip')
    
    path_list = [str(part) for part in [f'w{width}', f'h{height}', filename] if part not in [None, 'hNone', 'wNone']]

    storage = LocalHandler()
    
    image_default_path= storage.get_path(filename)

    if image_default_path is None:
        return jsonify({"error": "Imagem original não encontrada"}), 404

    full_path = os.path.join(*path_list)
    
    image_modified_path = storage.get_path(full_path)

    # deve verificar se o imagem existe com as caracteristicas do arquivo
    if  image_modified_path is None:
        transform = TransformHandler()
        
        image_bytes = storage.get(filename)
        image_modified_bytes = transform.change_size(
            image_content=image_bytes,
            width=width,
            height=height,
        )
        image_modified_path = storage.save(
            filename=full_path,
            content=image_modified_bytes
        )

        return redirect(
            location=url_for(
                endpoint='static', 
                filename=image_modified_path
            ),
            code=302
        )
    
    return redirect(
        location=url_for(
            endpoint='static', 
            filename=image_modified_path
        ),
        code=302
    )