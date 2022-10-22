from flask import render_template
from manage import app

@app.route("/veiculo")
def veiculo():
    return render_template('page/veiculo.html',menu='master', submenu='veiculo')