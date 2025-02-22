from app import create_app
import os
from flask import Flask, jsonify


# Configurar o ambiente (default: 'development')
env = os.getenv('FLASK_ENV', 'production')

# Criar a aplicação com base no ambiente
app = create_app()

# Rota para exibir o endereço do servidor e as rotas disponíveis
@app.route('/info', methods=['GET'])
def server_info():
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    server_address = f"http://{host}:{port}"
    routes = [
        {"endpoint": rule.endpoint, "methods": list(rule.methods), "route": rule.rule}
        for rule in app.url_map.iter_rules()
    ]
    return jsonify({
        "server_address": server_address,
        "available_routes": routes
    })

if __name__ == '__main__':
    app.run()
