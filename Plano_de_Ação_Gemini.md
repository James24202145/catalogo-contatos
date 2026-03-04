**Solicitação:** 
> Eu gostaria de fazer uma aplicação Web. Um catalogo de contatos com: *nome*, *endereço* e *telefone* utilizando **MySQL** com o **Framework Flask** e a aparência dele moldada com o **Framework Bootstrap**. A principio as versões serão deixadas no <https://github.com/> e no final o aplicativo será hospedado no site <https://www.pythonanywhere.com>.
> Já criei as contas no *GitHub* e no *PythonAnywhere*, não faço idéia de como começar. Portanto eu gostaria que fosse elaborado um plano de ação para desenvolvimento desse aplicativo fazendo o versionamento no GitHub, para que cada dia eu faça uma parte até que finalmente seja hospedado no pythonanywhere. O plano de ação deve ter muitos passos com tarefas simples para que eu consiga entender cada uma.

**Resposta Gemini:**

Excelente iniciativa! Construir um CRUD (Create, Read, Update, Delete) é o rito de passagem perfeito para qualquer desenvolvedor web. Flask e MySQL formam uma dupla poderosa, e o PythonAnywhere facilita muito o deploy.

Como você quer algo bem passo a passo, dividi o plano em 7 dias. Se sentir que está fácil, pode acelerar, mas o foco aqui é a consistência.

---

### 📅 Dia 1: Preparação do Terreno
O objetivo hoje é deixar seu ambiente pronto e o GitHub conectado.

1. **Instale o Python e o VS Code** (ou seu editor favorito) no seu computador.
2. **Crie uma pasta para o projeto** no seu PC (ex: catalogo-contatos).
3. **Crie um Ambiente Virtual (venv):** Isso mantém as bibliotecas do projeto isoladas.
   * No terminal, dentro da pasta: `python -m venv venv`
   * Ative-o: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Mac/Linux).
4. **Inicie o Git**: No terminal, digite `git init`.
5. **Crie o Repositório no GitHub:** Siga as instruções que aparecem lá para "push an existing repository" e conecte sua pasta local ao GitHub.

---

### 📅 Dia 2: A Estrutura Básica do Flask
Hoje vamos fazer o "Hello World" e organizar as pastas.

1. **Instale o Flask**: `pip install Flask`.
2. **Crie o arquivo** `app.py`: O coração do seu código
3. **Crie as pastas de Front-end**: Dentro da pasta do projeto, crie uma pasta chamada `templates` (para o HTML) e outra chamada `static` (para o CSS/Imagens).
4. **Codifique a rota principal**: No `app.py`, configure o Flask para rodar e exibir uma página simples.
5. **Commit e Push**: Mande essas mudanças para o GitHub.

---

### 📅 Dia 3: O Banco de Dados (MySQL)
Vamos desenhar onde os nomes e telefones ficarão guardados.

1. **Instale o conector**: `pip install flask-sqlalchemy mysql-connector-python`.
2. **Desenhe a Tabela**: Imagine uma planilha com as colunas: `id, nome, endereco, telefone`.
3. **Configure a conexão**: No `app.py`, adicione as linhas que conectam o Flask ao MySQL (inicialmente você pode usar SQLite para facilitar o teste local, ou já apontar para um banco MySQL local se tiver instalado).
4. **Crie o Modelo**: Defina a classe Contato no código.

---

### 📅 Dia 4: O Visual com Bootstrap
Deixe o aplicativo com cara de profissional sem precisar ser um expert em design.

1. **Crie o** `base.html`: Use o CDN do Bootstrap (um link que você coloca no `<head>`) para carregar o CSS do framework.
2. **Crie a Tabela de Exibição**: No seu arquivo HTML principal, use as classes do Bootstrap como `table` e `table-striped`.
3. **Crie o Formulário**: Um formulário bonito com `form-control` para digitar os dados.
4. **Commit**: Não esqueça de subir as atualizações para o GitHub.

---

### 📅 Dia 5: Funcionalidades (O "C" e o "R" do CRUD)
Faremos o app salvar e listar os contatos.

1. **Função Adicionar**: Crie a rota no Flask que recebe os dados do formulário e salva no banco.
2. **Função Listar**: Altere a página inicial para buscar todos os contatos do banco e exibi-los na tabela do Bootstrap.
3. **Teste exaustivamente**: Adicione uns 5 contatos fictícios para ver se está tudo funcionando.

---

### 📅 Dia 6: Finalizando o CRUD (Update e Delete)
Um catálogo precisa permitir correções e exclusões.

1. **Botão Deletar**: Adicione um botão ao lado de cada contato que remove o registro do banco.
2. **Botão Editar**: Crie uma página simples que carrega os dados atuais e permite salvar por cima.
3. **Mensagens de Feedback**: Use o flash do Flask para mostrar mensagens como "Contato adicionado com sucesso!".

---

### 📅 Dia 7: Hospedagem no PythonAnywhere
A hora da verdade: colocar o site no ar.

1. **No PythonAnywhere**: ~~Vá na aba "Databases" e crie seu banco de dados MySQL~~. *Infelizmente o apenas a versão paga do PythonAnywhere permite carregar banco de dados MySQL, portanto continuamos usando o banco de dados SQLite.*
2. **Clone o Código**: Use o console do PythonAnywhere para dar um git clone no seu repositório do GitHub.
3. **Configuração Web**: Na aba "Web", aponte para o seu arquivo app.py e configure o caminho do diretório.

**Reload**: Clique no botão verde de "Reload" e acesse seu link!

---

> A seguir cada um dos passos, a partir do dia 2, são detalhados com o código utilizado:

---

### Dia 2

O Dia 2 é fundamental porque é aqui que o seu projeto ganha vida e deixa de ser apenas uma pasta vazia para se tornar um servidor web funcional.

Hoje o foco é instalar o Flask, criar a estrutura de pastas que ele exige e fazer a primeira página aparecer no seu navegador.

Aqui está o detalhamento do plano de ação para hoje:

🛠️ **Passo 1: Preparar o Ambiente (Terminal)**

Certifique-se de que seu ambiente virtual (venv) criado ontem está ativo. Você saberá que está ativo se aparecer (venv) antes do caminho no seu terminal.

Instale o Flask:
1. No terminal, digite:

> Bash

`pip install Flask`

2. Crie um arquivo de dependências:
    Isso é importante para o PythonAnywhere saber o que instalar depois.

> Bash

`pip freeze > requirements.txt`

📁 **Passo 2: Organizar a Estrutura de Pastas**

O Flask é exigente com nomes de pastas. Dentro da sua pasta catalogo-contatos, crie esta estrutura manualmente:

* `app.py` (Arquivo principal)
* `templates/` (Pasta para arquivos HTML)
  * `index.html` (Sua página inicial)
* `static/` (Pasta para arquivos CSS/JS/Imagens - vazia por enquanto)

🐍 **Passo 3: Criar o Código do Servidor (`app.py`)**

Abra o arquivo `app.py` no seu editor e cole este código básico:

> Python


```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Isso diz ao Flask para carregar o arquivo index.html da pasta templates
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

```

📄 **Passo 4: Criar o Visual Inicial (`templates/index.html`)**

Abra o arquivo `index.html` e coloque um HTML simples para testar:

> HTML

```￼
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Meu Catálogo de Contatos</title>
</head>
<body>
    <h1>Olá! O Flask está funcionando.</h1>
    <p>Em breve, aqui teremos nossa lista de contatos.</p>
</body>
</html>
```

🚀 **Passo 5: Rodar e Testar**
No terminal, execute o comando:

> Bash

`python app.py`

O terminal vai dizer que o site está rodando em `http://127.0.0.1:5000`.

Abra seu navegador e cole esse endereço. Se aparecer a mensagem **"Olá! O Flask está funcionando"**, sucesso!

📤 **Passo 6: Versionar no GitHub**

Agora que algo está funcionando, vamos salvar o progresso:

No terminal, pare o servidor (aperte `Ctrl + C`).

Adicione os arquivos: `git add .`

Crie a "nota" do que foi feito: `git commit -m "Dia 2: Estrutura inicial do Flask e primeira rota"`

Envie para o GitHub: `git push origin main` (ou master, dependendo da sua branch).

---

### Dia 3

O Dia 3 é um dos mais importantes, pois é quando transformamos um site estático (que esquece tudo quando fecha) em uma aplicação real que armazena dados.

Hoje o foco é o Banco de Dados (MySQL). No PythonAnywhere o MySQL já está disponível, mas para desenvolver no seu computador, vamos usar uma biblioteca chamada Flask-SQLAlchemy. Ela permite que você gerencie o banco de dados usando código Python, o que facilita muito a vida.

Aqui está o plano detalhado para hoje:

🛠️ **Passo 1: Instalar as "Pontes" (Bibliotecas)**

No seu terminal (com a venv ativa), instale as ferramentas que fazem o Flask conversar com o MySQL:

> Bash

`pip install flask-sqlalchemy mysql-connector-python`

(Lembre-se de atualizar seu arquivo de requisitos logo depois: `pip freeze > requirements.txt`)

🐍 **Passo 2: Configurar a Conexão no `app.py`**

Abra o seu `app.py` e adicione as configurações do banco. No início, usaremos um banco local simples (SQLite) para você testar sem precisar instalar o servidor MySQL pesado no seu PC, ~~e no Dia 7 mudaremos para o MySQL do PythonAnywhere apenas alterando uma linha~~.

Modifique seu `app.py` para ficar assim:

> Python

```￼
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do Banco de Dados (Cria um arquivo chamado contatos.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODELO DO BANCO DE DADOS ---
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200))
    telefone = db.Column(db.String(20))

    def __repr__(self):
        return f'<Contato {self.nome}>'

# Suas rotas continuam aqui embaixo...
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Cria o banco de dados e as tabelas automaticamente
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

🔍 **Passo 3: Entendendo o que fizemos**

`db.Model`: Criamos uma "Classe" chamada Contato. Ela diz ao banco de dados: "Ei, crie uma tabela com as colunas `ID`, `Nome`, `Endereço` e `Telefone`".

`db.create_all()`: Esse comando verifica se o arquivo do banco existe. Se não existir, ele cria o arquivo `contatos.db` e a tabela automaticamente para você.

🚀 **Passo 4: Testar a criação**

Rode o comando `python app.py`.

Verifique se apareceu um novo arquivo chamado `contatos.db` na pasta do seu projeto (ou dentro de uma pasta chamada instance).

Se o site abriu sem erros, seu banco de dados está "vivo"!

📤 **Passo 5: Versionar no GitHub**

Não esqueça de salvar o progresso de hoje:

No terminal: `git add .`

`git commit -m "Dia 3: Configuração do SQLAlchemy e criação do modelo Contato"`

`git push origin main`

---

### Dia 4:

Dia 4, hoje o seu projeto vai deixar de ser uma página em branco com apenas um texto e vai ganhar "cara" de aplicativo profissional. O objetivo de hoje é integrar o Bootstrap (o framework visual mais famoso do mundo) para criar o layout do seu catálogo.

O segredo do Bootstrap é que você não precisa escrever quase nada de CSS; você apenas usa "classes" prontas no HTML.

Aqui está o seu plano de ação detalhado para hoje:

🎨 **Passo 1: Criar o Layout Base (`templates/base.html`)**

Em vez de repetir o menu e o estilo em todas as páginas, o Flask permite criar um "molde". Crie um arquivo chamado `base.html` dentro da pasta `templates`:


> HTML

```￼
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo de Contatos</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

    <nav class="navbar navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">📞 Meus Contatos</a>
        </div>
    </nav>

    <div class="container">
        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

```

📝 **Passo 2: Atualizar a Página Inicial (`templates/index.html`)**

Agora, vamos fazer o `index.html` "herdar" o visual do `base.html` e criar o formulário e a tabela (mesmo que ainda vazia). Substitua o conteúdo do seu `index.html` por este:


> HTML

```
￼
{% extends 'base.html' %}

{% block content %}
<div class="row">
    <div class="col-md-4">
        <div class="card card-body">
            <h5>Novo Contato</h5>
            <form action="/add" method="POST">
                <div class="mb-3">
                    <input type="text" name="nome" placeholder="Nome Completo" class="form-control" required>
                </div>
                <div class="mb-3">
                    <input type="text" name="endereco" placeholder="Endereço" class="form-control">
                </div>
                <div class="mb-3">
                    <input type="text" name="telefone" placeholder="Telefone" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Salvar Contato</button>
            </form>
        </div>
    </div>

    <div class="col-md-8">
        <table class="table table-striped table-hover bg-white shadow-sm">
            <thead class="table-dark">
                <tr>
                    <th>Nome</th>
                    <th>Endereço</th>
                    <th>Telefone</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Exemplo de Nome</td>
                    <td>Rua de Teste, 123</td>
                    <td>(11) 99999-9999</td>
                    <td>
                        <a href="#" class="btn btn-sm btn-warning">Editar</a>
                        <a href="#" class="btn btn-sm btn-danger">Excluir</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

```

🚀 **Passo 3: Visualizar o Resultado**

Rode o seu `app.py`.

Acesse `http://127.0.0.1:5000`.

Você verá um layout dividido em duas colunas: à esquerda o formulário azul e à direita a tabela organizada.

Atenção: Se você clicar no botão "Salvar", dará um erro "404 Not Found" porque ainda não criamos a rota /add no Python. Faremos isso amanhã!

📤 **Passo 4: Salvar no GitHub**

Vamos registrar esse grande salto visual:

`git add .`

`git commit -m "Dia 4: Implementação do Bootstrap e layout base com Jinja2"`

`git push origin main`

💡 **O que aprendemos hoje?**

Jinja2 ({% %}): É o motor do Flask que permite reutilizar pedaços de HTML (o extends e o block).

Grid do Bootstrap: Usamos row e col-md-4/8 para dividir a tela.

Classes do Bootstrap: card, table, btn, form-control – são elas que dão o estilo sem precisarmos de CSS próprio.

---

### Dia 5:

O Dia 5 é o momento da "mágica" acontecer. Até ontem, tínhamos um visual bonito, mas que não fazia nada. Hoje, vamos conectar os fios: o formulário do HTML vai enviar dados para o Python, e o Python vai salvar no Banco de Dados.

Hoje o foco é o "C" (Create) e o "R" (Read) do CRUD.

🛠️ **Passo 1: Preparar as Rotas no `app.py`**

Precisamos criar a função que recebe os dados do formulário. Abra o seu app.py e adicione esta nova rota:

> Python

```
￼
@app.route('/add', methods=['POST'])
def add_contato():
    # Pegando os dados vindos do formulário HTML
    nome = request.form.get('nome')
    endereco = request.form.get('endereco')
    telefone = request.form.get('telefone')

    # Criando um novo objeto do tipo Contato
    novo_contato = Contato(nome=nome, endereco=endereco, telefone=telefone)

    # Salvando no Banco de Dados
    db.session.add(novo_contato)
    db.session.commit()

    return redirect(url_for('index'))

```

📝 **Passo 2: Exibir os Dados Reais no `index.html`**

Agora, em vez de mostrar aquele "Exemplo de Nome" que escrevemos ontem, vamos buscar os contatos reais do banco.

Primeiro, no `app.py`, altere a sua rota principal (index) para buscar os dados:

> Python

```￼
@app.route('/')
def index():
    # Busca todos os contatos do banco de dados
    lista_contatos = Contato.query.all()
    return render_template('index.html', contatos=lista_contatos)
```

Agora, no `index.html`, vamos usar um "loop" do Flask para repetir as linhas da tabela. Substitua a parte do `<tbody>` por esta:

> HTML

```￼
<tbody>
    {% for contato in contatos %}
    <tr>
        <td>{{ contato.nome }}</td>
        <td>{{ contato.endereco }}</td>
        <td>{{ contato.telefone }}</td>
        <td>
            <a href="#" class="btn btn-sm btn-warning">Editar</a>
            <a href="#" class="btn btn-sm btn-danger">Excluir</a>
        </td>
    </tr>
    {% endfor %}
</tbody>
```

🚀 **Passo 3: Teste de Fogo**

Salve tudo e rode o comando `python app.py`.

Acesse o site no navegador.

Preencha o formulário com um nome e telefone real e clique em "Salvar Contato".

A página deve recarregar e o contato deve aparecer instantaneamente na tabela à direita!

📤 **Passo 4: Registrar o Progresso no GitHub**

Agora que seu app já é funcional (ele já guarda informações!), vamos versionar:

`git add .`

`git commit -m "Dia 5: Implementação de criação e listagem de contatos (C e R do CRUD)"`

`git push origin main`

💡 O que você conquistou hoje:

**Request**: Aprendeu como o Python "pega" o que o usuário digitou.

**Commit**: Aprendeu a salvar mudanças permanentes no banco de dados.

**Jinja2 Loops**: Aprendeu a usar o {% for %} para gerar tabelas dinâmicas.

---

### Dia 6:

Se o seu aplicativo já está salvando e listando contatos, você já passou da parte mais difícil. Hoje vamos finalizar o ciclo de vida dos dados com o "U" (Update) e o "D" (Delete) do CRUD.

Isso permitirá que você corrija erros de digitação ou apague contatos que não quer mais.

🛠️ **Passo 1: A Função de Deletar (Mais simples)**

Primeiro, vamos criar a rota no `app.py` que apaga um contato usando o ID dele. Adicione este código abaixo das suas outras rotas:

> Python

```
@app.route('/delete/<int:id>')
def delete_contato(id):
    contato = Contato.query.get_or_404(id) # Busca o contato ou dá erro 404 se não existir
    db.session.delete(contato)
    db.session.commit()
    return redirect(url_for('index'))
```

Agora, no seu `index.html`, procure o botão de "Excluir" e atualize o link (href):

> HTML

```￼
<a href="/delete/{{ contato.id }}" class="btn btn-sm btn-danger">Excluir</a>
```

📝 **Passo 2: A Função de Editar**

Editar é um processo de dois passos: primeiro você vê os dados atuais em um formulário e depois salva as alterações.

Adicione a rota de edição no `app.py`:

> Python

```￼
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contato(id):
    contato = Contato.query.get_or_404(id)
    
    if request.method == 'POST':
        contato.nome = request.form.get('nome')
        contato.endereco = request.form.get('endereco')
        contato.telefone = request.form.get('telefone')
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('edit.html', contato=contato)
```

Crie um novo arquivo em `templates/edit.html`:

> HTML
￼
```
{% extends 'base.html' %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card card-body">
            <h5>Editar Contato</h5>
            <form action="/edit/{{ contato.id }}" method="POST">
                <div class="mb-3">
                    <input type="text" name="nome" value="{{ contato.nome }}" class="form-control" required>
                </div>
                <div class="mb-3">
                    <input type="text" name="endereco" value="{{ contato.endereco }}" class="form-control">
                </div>
                <div class="mb-3">
                    <input type="text" name="telefone" value="{{ contato.telefone }}" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-success w-100">Atualizar</button>
                <a href="/" class="btn btn-secondary w-100 mt-2">Cancelar</a>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

Atualize o link de "Editar" no seu index.html:

> HTML

```￼
<a href="/edit/{{ contato.id }}" class="btn btn-sm btn-warning">Editar</a>
```

**🚀 Passo 3: Teste Final Local**

Rode o `python app.py`.

Tente deletar um contato de teste.

Tente editar o nome de outro contato.

Tudo funcionando? Parabéns! Seu software está pronto.

**📤 Passo 4: Subir para o GitHub**

Hoje é o último commit antes do deploy no servidor real!

No terminal: `git add .`

`git commit -m "Dia 6: CRUD completo - Funcionalidades de editar e excluir adicionadas"`

`git push origin main`

---

### Dia 7
Nesse dia descobri que o plano gratuíto do PythonAnywhere não dava direito a utilização do MySql, por isso tive que pedir para continuar usando o SQLite, que dispensa o uso de um servidor de banco de dados.

Vamos recomeçar o Dia 7 do zero, focando exclusivamente no uso do SQLite, que é o caminho mais garantido e gratuito para o seu projeto no PythonAnywhere.

Aqui está o seu novo mapa de navegação:

🛠️ **Passo 1: Ajustar o Código no seu PC (`app.py`)**

No seu computador, precisamos garantir que o Flask saiba exatamente onde o arquivo de banco de dados (.db) está.

Abra o `app.py` e altere a parte inicial para:

> Python

```

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configura o caminho absoluto para o banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'contatos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# ... restante do seu código (Modelos e Rotas)
```

📤 **Passo 2: Enviar a mudança para o GitHub**

Salve o arquivo e, no terminal do seu computador, execute:

`git add app.py`

`git commit -m "Ajuste do caminho do banco para SQLite"`

`git push origin main`

📥 **Passo 3: Baixar o código no PythonAnywhere**

Agora, vá para o site do PythonAnywhere:

Clique na aba Consoles e abra um console Bash.

Clone seu projeto (se ainda não fez isso):

> Bash

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta (substitua pelo nome real da sua pasta):

> Bash
￼
`cd nome-do-seu-repositorio`


Crie e ative o ambiente virtual lá dentro:

> Bash

```
python3 -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy
```

🌐 **Passo 4: Configurar a Aba "Web"**

Saia do console e vá para a aba Web no menu superior do PythonAnywhere:

Clique em Add a new web app (siga o assistente: clique em Next, selecione Manual Configuration e escolha o Python 3.10 ou superior).

Code Section:

Source code: Coloque o caminho da sua pasta (ex: /home/seuusuario/seu-repositorio).

Working directory: O mesmo caminho acima.

Virtualenv Section:

Coloque o caminho da pasta venv que você criou (ex: /home/seuusuario/seu-repositorio/venv).

📄 **Passo 5: Editar o arquivo WSGI**

Ainda na aba Web, procure o link para o WSGI configuration file (é um arquivo .py). Clique nele, apague tudo o que estiver escrito e cole apenas isto:

> Python

```￼
import sys
import os

# Ajuste para o caminho da sua pasta no servidor
path = '/home/seuusuario/seu-repositorio'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

(Substitua seuusuario e seu-repositorio pelos seus nomes reais).


Volte na aba Web e clique no botão verde Reload.

✅ Pronto!
Agora é só acessar <http://24202145.pythonanywhere.com> (meu site). O site deve carregar limpo, e quando você adicionar o primeiro contato, o arquivo contatos.db será criado automaticamente na pasta do projeto no servidor.

