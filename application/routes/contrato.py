from flask import render_template
from manage import app

@app.route("/contrato")
def contrato():
    return render_template('page/contrato.html',menu='master', submenu='contrato')