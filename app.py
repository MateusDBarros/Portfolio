from flask import Flask, render_template

app = Flask(__name__)

# Dados do portfólio (pode vir de um banco de dados no futuro)
projects = [
    {
        "title": "Sistema de Agendamento Médico",
        "description": "Aplicação desenvolvida em Java com Spring Boot. Banco de Dados criado no PostgreSQL.",
        "image": "projeto1.jpg",
        "link": "https://github.com/MateusDBarros/SAM"  # Link do GitHub
    },
    {
        "title": "Watcher",
        "description": "Aplicação que integra Java com Spring Boot e Python para criar uma API REST que gerencia finanças pessoais",
        "image": "projeto2.jpg",
        "link": "https://github.com/MateusDBarros/Watcher"  # Link do GitHub
    },
    {
        "title": "NetflixScrapping",
        "description": "Este projeto é um script em Python que acessa uma página da Netflix e extrai informações sobre filmes ou séries de mistério, coletando os títulos e as descrições dos itens listados.",
        "image": "projeto3.jpg",
        "link": "https://github.com/MateusDBarros/NetflixScrapping"  # Link do GitHub
    },
    {
        "title": "Java - TicTacToe",
        "description": "Um simples e divertido jogo da velha, feito utilizando Java Puro",
        "image": "projeto4.jpg",
        "link": "https://github.com/MateusDBarros/java-tictactoe"  # Link do GitHub
    },
    {
        "title": "TaskManagerPy",
        "description": "Uma API RESTful desenvolvida em Python utilizando Flask e SQLAlchemy para persistência de dados. A API permite operações CRUD (Criar, Ler, Atualizar e Deletar) para gerenciar tarefa.",
        "image": "projeto5.jpg",
        "link": "https://github.com/MateusDBarros/TaskManagerPy"  # Link do GitHub
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)