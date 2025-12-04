from main import app
from flask import render_template

#rotas
@app.route("/") 
def home(): 
    return render_template("index.html")

@app.route("/galeria") 
def galeria(): 
    return render_template("galeria.html")

@app.route("/estudio") 
def estudio(): 
    return render_template("estudio.html")

@app.route("/atendimento") 
def atendimento(): 
    return render_template("atendimento.html")