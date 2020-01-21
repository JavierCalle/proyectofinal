from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask (__name__)


db = pymysql.connect(host='localhost',user='root',password='',db='Sismos_Ecuador')
cursor = db.cursor()
app.secret_key='mysecretkey'    

@app.route('/')
def home():
    cursor.execute('select * from sismos_historicos_ecuador order by fecha')
    datos = cursor.fetchall()
    return render_template('index.html',sismos=datos)

@app.route('/verprediccion')
def verprediccion():
    return render_template('prediccion.html')

@app.route('/vercontexto')
def vercontexto():
    return render_template('contexto.html')

@app.route('/verredesneuronales')
def verredesneuronales():
    return render_template('redesneuronales.html')

@app.route('/verregresionlogistica')
def verregresionlogistica():
    return render_template('regresionlogistica.html')

@app.route('/verdatosregresion')
def verdatosregresion():
    cursor.execute('select * from regresion')
    dato = cursor.fetchall()
    return render_template('datos_regresion.html',sismos=dato)

@app.route('/verdatosredes')
def verdatosredes():
    cursor.execute('select * from redes_neuronales_LSTM')
    dato = cursor.fetchall()
    return render_template('datos_redes.html',sismos=dato)

@app.route('/verdatoscodificados')
def verdatoscodificados():
    cursor.execute('select * from datos_codificados order by codificacion')
    dato = cursor.fetchall()
    return render_template('datos_codificados.html',sismos=dato)

if __name__ == '__main__':
    app.run (port=5000, debug=True)
