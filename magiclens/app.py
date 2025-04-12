import os

from flask import Flask, request, jsonify, render_template

from magiclens.config import Settings
from magiclens.routes.ui_demo import ui_demo
from magiclens.storage.local_handler import LocalHandler

app = Flask(__name__)

UPLOAD_FOLDER = f'magiclens/static/{Settings().bucket_name}'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(ui_demo)
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
    height = request.args.get('h')
    width = request.args.get('w')
    flip = request.args.get('flip')

    # deve verificar se o imagem existe
    # deve verificar se o imagem existe com as caracteristicas do arquivo
    # como tamanho, tipo, etc
    # deve ficar aqui dentro
    return { 'imagem': {} }


