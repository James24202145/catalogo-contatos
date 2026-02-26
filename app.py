from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do Banco de Dados (Cria um arquivo chamado contatos.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Modelo do Banco de Dados ---
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    #email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Contato {self.nome}>'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Cria o banco de dados e as tabelas automaticamente
    with app.app_context():
        db.create_all()
    app.run(debug=True)
