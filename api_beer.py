#  Curso de Engenharia de Software - UniEVANGÉLICA 
#  Disciplina de Programação Web 
#  Dev: Thomas Nicholas
#  DATA 12/05

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo (poderiam ser armazenados em um banco de dados)
cervejas = [
    {"id": 1, "Cerveja": "IPA", "sabor": "Amargo", "Avaliacao": "4"},
    {"id": 2, "Cerveja": "Stout", "sabor": "Rico e encorpado", "Avaliacao": "5"},
    {"id": 3, "Cerveja": "Weissbier", "sabor": "Refrescante", "Avaliacao": "3"},
    {"id": 4, "Cerveja": "Pilsner", "sabor": "Amargo moderado", "Avaliacao": "4"},
    {"id": 5, "Cerveja": "Saison", "sabor": "leve acidez", "Avaliacao": "5"}
]

# Endpoint para listar todos os cervejas
@app.route('/listar_cervejas', methods=['GET'])
def listar_cervejas():
    return jsonify(cervejas)

# Endpoint para obter um livro por ID
@app.route('/obter_cerveja/<int:cerveja_id>', methods=['GET'])
def obter_cerveja(cerveja_id):
    cerveja = next((cerveja for cerveja in cervejas if cerveja['id'] == cerveja_id), None)
    if cerveja:
        return jsonify(cerveja)
    return jsonify({"mensagem": "Cerveja não encontrada"}), 404

# Endpoint para adicionar 
@app.route('/adicionar_cerveja', methods=['POST'])
def adicionar_cerveja():
    novo_cerveja = request.json
    cervejas.append(novo_cerveja)
    return jsonify({"mensagem": "Cerveja adicionada com sucesso"}), 201

# Endpoint para excluir 
@app.route('/excluir_cerveja/<int:cerveja_id>', methods=['DELETE'])
def excluir_cerveja(cerveja_id):
    global cervejas
    cervejas = [cerveja for cerveja in cervejas if cerveja['id'] != cerveja_id]
    return jsonify({"mensagem": "Cerveja excluída com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
