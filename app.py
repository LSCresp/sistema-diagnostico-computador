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
    febre = data.get("febre")
    if febre == 's':
        tosse = data.get("tosse")
        if tosse == 's':
            return jsonify({"resposta": "🩺 Recomendação: Você pode estar com uma infecção respiratória, como gripe ou resfriado. Consulte um médico para avaliação."})
        else:
            return jsonify({"resposta": "🩺 Recomendação: Febre sem tosse pode indicar uma infecção ou outra condição. Monitore sua temperatura e consulte um médico."})

    dor = data.get("dor")
    if dor == 's':
        return jsonify({"resposta": "🩺 Recomendação: Dor localizada pode indicar lesão ou inflamação. Descanse a área afetada e procure um médico se persistir."})

    fadiga = data.get("fadiga")
    if fadiga == 's':
        sono = data.get("sono")
        if sono == 's':
            return jsonify({"resposta": "🩺 Recomendação: Fadiga com sono adequado pode indicar anemia ou outra condição. Consulte um médico para exames."})
        else:
            return jsonify({"resposta": "🩺 Recomendação: Melhore a qualidade do sono e hidrate-se. Se a fadiga persistir, procure um médico."})

    return jsonify({"resposta": "✅ Não foram detectados sintomas graves com base nas respostas. Mantenha um estilo de vida saudável."})

if __name__ == "__main__":
    app.run(debug=True)