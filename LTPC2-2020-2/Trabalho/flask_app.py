
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/muelsa")
def inicio_da_pagina():
    return render_template("pg1.html")

@app.route("/amarelinha")
def b1():
    return render_template("pg2.html")

@app.route("/pega-pega")
def b2():
    return render_template("pg3.html")

@app.route("/esconde-esconde")
def b3():
    return render_template("pg4.html")

@app.route("/chuta-lata")
def b4():
    return render_template("pg5.html")

@app.route("/pula-corda")
def b5():
    return render_template("pg6.html")

@app.route("/cv")
def mostrar_curriculo():
    return render_template("cv.html")
