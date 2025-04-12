import os

from flask import Flask, request, jsonify, render_template, redirect, url_for

from magiclens.config import Settings
from magiclens.routes.ui.demo.demo import demo_bp
from magiclens.storage.local_handler import LocalHandler
from magiclens.transform.transform_handler import TransformHandler
app = Flask(__name__)

UPLOAD_FOLDER = f'magiclens/static/{Settings().bucket_name}'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(demo_bp)

@app.route('/api/status')
def index():
    return {'message': 'Ok'}

@app.route('/api/image', methods=['POST'])
@app.route('/api/image', methods=['POST'])
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

    storage = LocalHandler(base_path=app.config['UPLOAD_FOLDER'])
    
    storage.save(
        filename=filename,
        content=file.read()
    )

    return render_template('demo_show_image.html', filename='imagens/'+filename)

@app.route('/api/image/<path:filename>', methods=['GET'])
def process(filename: str):
    height = request.args.get('h', type=int)
    width = request.args.get('w', type=int)
    flip = request.args.get('flip')
    
    path_list = [str(part) for part in [f'w{width}', f'h{height}', filename] if part not in [None, 'hNone', 'wNone']]

    storage = LocalHandler(base_path=app.config['UPLOAD_FOLDER'])
    
    # verifica se a imagem original existe
    if storage.get(filename) is None:
        return jsonify({"error": "Imagem não encontrada"}), 404

    full_path = os.path.join(*path_list)
    
    # deve verificar se o imagem existe com as caracteristicas do arquivo
    if storage.get(full_path) is None:
        transform = TransformHandler()
        
        path_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_bytes =transform.change_size(
            filename=path_filename,
            width=width,
            height=height,
        )
        storage.save(
            filename=full_path,
            content=image_bytes
        )

    return redirect(
        location=url_for(
            endpoint='static', 
            filename=os.path.join(
                Settings().bucket_name,
                full_path
            )
        ),
        code=302
    )


