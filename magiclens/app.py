from flask import Flask, request, jsonify
from magiclens.routes.ui_demo import ui_demo
from magiclens.storage import S3Handler
from magiclens.config import Settings

app = Flask(__name__)

app.register_blueprint(ui_demo)
@app.route('/api/status')
def index():
    return {'message': 'Ok'}

@app.route('/api/image/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']

    if file.filename == '':
            return jsonify({"error": "Nome do arquivo vazio"}), 400
    
    filename = request.form.get('filename')
    
    if filename:
        print(filename.split('.')[0],file.filename.split('.')[-1])
        filename = '.'.join([
            filename.split('.')[0],
            file.filename.split('.')[-1]
        ])
    else:
        filename = file.filename
    

    storage = S3Handler()

    if storage.get(filename):
        return jsonify({"error": "Arquivo já existe"}), 400

    storage.save(filename, file)

    return { 'url': f'{Settings().ENDPOINT_URL}/{Settings().BUCKET_NAME}/{filename}' }

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


