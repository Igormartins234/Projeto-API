from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_ENDPOINT = "https://apiJ.dicionario-aberto.net/word/"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    palavra = request.form.get('palavra', None)

    if not palavra:
        return render_template('index.html', error='Por favor, digite uma palavra.')

    response = requests.get(f"{API_ENDPOINT}{palavra}")

    if response.status_code == 200:
        dados = response.json()
        return render_template('index.html', palavra=palavra, dados=dados)
    else:
        return render_template('index.html', error='Erro ao buscar a palavra.')

if __name__ == '__main__':
    app.run(debug=True)