from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "API Rodando!"

@app.route("/gerar_metas", methods=["POST"])
def gerar_metas():
    dados = request.json
    # Aqui entra o código de cálculo das metas
    return jsonify({"mensagem": "Mensagem formatada para WhatsApp"})  # Ajuste aqui

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
