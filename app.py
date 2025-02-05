from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "API Rodando!"

@app.route("/gerar_metas", methods=["POST"])
def gerar_metas():
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"erro": "Nenhum dado recebido"}), 400

        # Verificar se as chaves obrigatórias estão presentes
        required_keys = ["meta_loja", "meta_pickup", "meta_shipfrom"]
        for key in required_keys:
            if key not in dados:
                return jsonify({"erro": f"Falta a chave obrigatória: {key}"}), 400

        mensagem = f"Meta Loja: R${dados['meta_loja']:.2f}\n"
        mensagem += f"Meta Pick-Up: R${dados['meta_pickup']:.2f}\n"
        mensagem += f"Meta Ship-From: R${dados['meta_shipfrom']:.2f}\n"

        return jsonify({"mensagem": mensagem})

    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
