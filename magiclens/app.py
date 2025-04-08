from flask import Flask, request, jsonify, redirect, url_for
from magiclens.routes.iu.demo.ui_demo import ui_demo

app = Flask(__name__)

app.register_blueprint(ui_demo, url_prefix='/ui/demo')

@app.route('/api/status')
def index():
    return {'message': 'Ok'}

@app.route('/api/image', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']
    filename = file.filename

    if file.filename == '':
            return jsonify({"error": "Nome do arquivo vazio"}), 400

   
    return { 'message': 'URL da imagem' }

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


