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

@app.route("/blog") 
def blog(): 
    return render_template("blog.html")

@app.route("/cuidados") 
def cuidados(): 
    return render_template("blogs/cuidados.html")

@app.route("/estilo") 
def estilo(): 
    return render_template("blogs/estilo.html")

@app.route("/primeira") 
def primeira(): 
    return render_template("blogs/primeira.html")

@app.route("/vegan") 
def vegan(): 
    return render_template("blogs/vegan.html")

@app.route("/realismo") 
def realismo(): 
    return render_template("blogs/realismo.html")

@app.route("/peleNegra") 
def peleNegra(): 
    return render_template("blogs/peleNegra.html")
