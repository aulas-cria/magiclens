from flask import Flask, request, jsonify
from magiclens.routes.ui_demo import ui_demo

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
    filename = file.filename

    if file.filename == '':
            return jsonify({"error": "Nome do arquivo vazio"}), 400
    

    # o codigo para receber o arquivo e salvar na pasta storage
    # seguir o padrao de nome do arquivo
    # o path passado na url deve ser o path do arquivo
    # deve ficar aqui dentro 
    return {'message': 'Arquivo enviado com sucesso'}

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


