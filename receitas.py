"""
Aplicação web para gerenciar receitas de uma doceria.

Tecnologias: Flask (backend/web) e SQLite (a ser integrado futuramente).
"""

# Importações necessárias do Flask
from flask import Flask, render_template

# Cria a instância da aplicação Flask
app: Flask = Flask(__name__)


# Rota da página inicial: renderiza templates/index.html
@app.route("/")
def index():
    """Exibe a página inicial da aplicação."""
    return render_template("index.html")


# Rota de cadastro de receita: renderiza templates/cadastro.html
@app.route("/cadastro")
def cadastro():
    """Exibe o formulário de cadastro de uma nova receita.

    Observação: Em uma etapa futura, esta rota poderá aceitar POST para
    salvar dados no SQLite. Por ora, apenas renderiza o HTML.
    """
    return render_template("cadastro.html")


# Rota para listar receitas: renderiza templates/receitas.html
@app.route("/receitas")
def receitas():
    """Exibe a página onde a lista de receitas aparecerá."""
    return render_template("receitas.html")


# Ponto de entrada da aplicação
if __name__ == "__main__":
    # Executa o servidor de desenvolvimento do Flask.
    # Em produção, utilize um servidor WSGI (ex.: gunicorn) e configure variáveis
    # de ambiente de forma adequada.
    app.run(debug=True)


