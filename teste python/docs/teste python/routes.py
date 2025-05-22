from flask import render_template, request, redirect
from models import db, Rota

def init_routes(app):
    @app.route('/')
    def index():
        rotas = Rota.query.all()  # Buscar rotas para exibir
        return render_template('inicio.html', rotas=rotas)

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/cadastro')
    def cadastro():
        return render_template('cadastro.html')

    @app.route('/buscar_rota', methods=['POST'])  # Rota de início e destino
    def buscar_rota():
        inicio = request.form['inicio']
        destino = request.form['destino']

        nova_rota = Rota(inicio=inicio, destino=destino, usuario_id=1)
        db.session.add(nova_rota)
        db.session.commit()

        return redirect('/')

#CODIGO FUNCIONANDO NÃO MEXER MAIS!!!!