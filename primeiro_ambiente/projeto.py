
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
 return render_template("index.html")


@app.route("/LIGADO", methods=["POST"])
def LIGADO():
    mensagem = "LIGADO"
    return render_template("pagON.html")

@app.route("/DESLIGADO", methods=["POST"])
def DESLIGADO():
    meS = "DESLIGADO"
    return render_template("pagOFF.html")


app.run(debug=True)
