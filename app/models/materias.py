from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(128), nullable=False)

    materias = db.relationship('Materia', backref='Usuario', lazy=True)

    def __init__(self, nick, email, senha):
        self.nick = nick
        self.email = email
        self.senha = senha

class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.String, nullable=False)
    criador = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __init__(self, titulo, descricao, conteudo, criador):
        self.titulo = titulo
        self.descricao = descricao
        self.conteudo = conteudo
        self.criador = criador