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
>> A seguir cada um dos passos, a partyir do dia 2, são detalhados com o código utilizado:
>>

---

### Dia2

O Dia 2 é fundamental porque é aqui que o seu projeto ganha vida e deixa de ser apenas uma pasta vazia para se tornar um servidor web funcional.

Hoje o foco é instalar o Flask, criar a estrutura de pastas que ele exige e fazer a primeira página aparecer no seu navegador.

Aqui está o detalhamento do plano de ação para hoje:

🛠️ **Passo 1: Preparar o Ambiente (Terminal)**

Certifique-se de que seu ambiente virtual (venv) criado ontem está ativo. Você saberá que está ativo se aparecer (venv) antes do caminho no seu terminal.

Instale o Flask:
1. No terminal, digite:

> Bash
>
> `pip install Flask`

2. Crie um arquivo de dependências:
    Isso é importante para o PythonAnywhere saber o que instalar depois.

> Bash
>
> `pip freeze > requirements.txt`

📁 **Passo 2: Organizar a Estrutura de Pastas**

O Flask é exigente com nomes de pastas. Dentro da sua pasta catalogo-contatos, crie esta estrutura manualmente:

* `app.py` (Arquivo principal)
* `templates/` (Pasta para arquivos HTML)
  * `index.html` (Sua página inicial)
* `static/` (Pasta para arquivos CSS/JS/Imagens - vazia por enquanto)

🐍 **Passo 3: Criar o Código do Servidor (`app.py`)**

Abra o arquivo `app.py` no seu editor e cole este código básico:

> Python
>
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
￼
`python app.py`

O terminal vai dizer que o site está rodando em `http://127.0.0.1:5000`.

Abra seu navegador e cole esse endereço. Se aparecer a mensagem **"Olá! O Flask está funcionando"**, sucesso!

📤 **Passo 6: Versionar no GitHub**

Agora que algo está funcionando, vamos salvar o progresso:

No terminal, pare o servidor (aperte `Ctrl + C`).

Adicione os arquivos: `git add .`

Crie a "nota" do que foi feito: `git commit -m "Dia 2: Estrutura inicial do Flask e primeira rota"`

Envie para o GitHub: `git push origin main` (ou master, dependendo da sua branch).



