from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    data = request.get_json()
    nome = data.get('nome', '')
    email = data.get('email', '')
    mensagem = data.get('mensagem', '')
    # Aqui poderia integrar com e-mail ou banco de dados
    return jsonify({'status': 'success', 'message': f'Obrigado, {nome}! Entraremos em contato em breve.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
