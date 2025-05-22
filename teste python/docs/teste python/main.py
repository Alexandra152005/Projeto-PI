from flask import Flask
from routes import init_routes
from models import db
from myapp import create_app

app = create_app()

app = Flask(__name__)
app.secret_key = 'secreto'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rotas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_routes(app)

if __name__ == '__main__':
    app.run(debug=False)  # debug=True pode duplicar execuções


#CODIGO FUNCIONANDO NÃO MEXER MAIS!!!!