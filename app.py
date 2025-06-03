from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/diagnostico", methods=["POST"])
def diagnostico():
    data = request.json
    energia = data.get("energia")
    if energia == 'n':
        cabo = data.get("cabo")
        if cabo == 'n':
            return jsonify({"resposta": "🔧 Solução: Conecte o cabo de energia corretamente."})
        else:
            return jsonify({"resposta": "🔧 Solução: Verifique a fonte de energia ou leve o computador a um técnico."})

    tela = data.get("tela")
    if tela == 'n':
        return jsonify({"resposta": "🔧 Solução: Verifique a conexão do monitor ou troque o cabo de vídeo."})

    internet = data.get("internet")
    if internet == 'n':
        wifi = data.get("wifi")
        if wifi == 's':
            senha = data.get("senha")
            if senha == 'n':
                return jsonify({"resposta": "🔧 Solução: Corrija a senha do Wi-Fi."})
            else:
                return jsonify({"resposta": "🔧 Solução: Reinicie o roteador ou verifique com o provedor."})
        else:
            return jsonify({"resposta": "🔧 Solução: Verifique o cabo de rede ou a porta de conexão."})

    return jsonify({"resposta": "✅ O sistema não detectou nenhum problema com o computador."})

if __name__ == "__main__":
    app.run(debug=True)

