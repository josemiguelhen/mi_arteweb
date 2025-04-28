from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/dibujos')
def dibujos():
    return render_template('dibujos.html')

@app.route('/poesia')
def poesia():
    return render_template('poesia.html')

@app.route('/musica')
def musica():
    return render_template('musica.html')

if __name__ == '__main__':
    app.run(debug=True)
