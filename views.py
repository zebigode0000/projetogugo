from main import app
from flask import render_template

#rotas
@app.route("/home") 
def home(): 
    return render_template("home.html")

@app.route("/galeria") 
def galeria(): 
    return render_template("galeria.html")

@app.route("/estudio") 
def estudio(): 
    return render_template("estudio.html")

@app.route("/atendimento") 
def atendimento(): 
    return render_template("atendimento.html")