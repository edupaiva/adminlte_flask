from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contrato")
def contrato():
    return render_template('page/contrato.html',menu='master', submenu='contrato')

@app.route("/veiculo")
def veiculo():
    return render_template('page/veiculo.html',menu='master', submenu='veiculo')

@app.route("/documentos")
def documentos():
    return render_template('page/documentos.html',menu='master', submenu='documentos')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)