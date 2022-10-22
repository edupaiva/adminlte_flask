from flask import render_template
from manage import app

@app.route("/documentos")
def documentos():
    return render_template('page/documentos.html',menu='master', submenu='documentos')