
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Rota(db.Model):
    __tablename__ = 'rota'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    # ROTA DE INICIO E DESTINO
    usuario_id = db.Column(db.Integer, nullable=False)
    inicio = db.Column(db.String(200), nullable=False)
    destino = db.Column(db.String(200), nullable=False)

# CODIGO FUNCIONANDO NÃO MEXER MAIS!!!!
