import os
from flask import Flask, render_template, request, redirect, session, flash, url_for
from config import db, senha
from app.models.materias import Usuario, Materia


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = senha

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'app', 'dados.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False

db.init_app(app)

@app.route('/')
def index():
    materias = db.session.query(Materia).all()
    return render_template('index.html', titulo='BLOG COXINHAS', topo='Inicio', post=materias)

@app.route('/singup')
def singup():
    return render_template('singup.html', titulo='Criar Conta', topo='Singup')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima=proxima)

@app.route('/nova-postagem')
def novapostagem():
    if not session:
        redirect(url_for('login'))
    return render_template('newpost.html', titulo='Nova Postagem', post='Nova Postagem')

@app.route('/materia/<int:id>', methods=['GET'])
def materia(id):
    materia = Materia.query.get_or_404(id)
    return render_template('materia.html', materia=materia, post=materia.titulo)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    materia = Materia.query.get_or_404(id)

    if request.method == 'POST':
        materia.titulo = request.form['titulo']
        materia.descricao = request.form['descricao']
        materia.conteudo = request.form['conteudo']
        db.session.commit()
        flash('Materia Editada Com Sucesso')
        return redirect(url_for('index'))
    return render_template('editar.html', materia=materia, titulo='Editar', post='Editar')

@app.route('/criar', methods=['POST'])
def criar():
    nick = request.form['nick']
    email = request.form['email']
    senha = request.form['senha']
    novo_usuario = Usuario(nick, email, senha)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect('login')

@app.route('/newpost', methods=['POST'])
def novopost():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    conteudo = request.form['conteudo']
    materia = Materia(titulo, descricao, conteudo, session['usuario_logado'])
    db.session.add(materia)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    materia = Materia.query.get_or_404(id)

    db.session.delete(materia)
    db.session.commit()
    flash('Materia Excluida com sucesso')
    return redirect(url_for('index'))

@app.route('/verificar', methods=['POST'])
def verificar():
    nickoremail = request.form['nickoremail']
    senha = request.form['senha']
    usuario = Usuario.query.filter((Usuario.nick == nickoremail) | (Usuario.email == nickoremail)).first()

    if usuario and usuario.senha == senha:
        session['usuario_logado'] = usuario.nick
        flash('Login Realizado com Sucesso')
        # proxima_pagina = request.form['proxima']
        return redirect(url_for('index'))
    else:
        flash('Não foi possivel realizar o Login.')
        return redirect( url_for('login') )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)