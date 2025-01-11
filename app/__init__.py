from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import api
from config import get_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())  # Usa a configuração baseada no ambiente
    
    # Configurar o CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Inicializa o banco de dados
    db.init_app(app)
    
    # Registra o Blueprint da API
    app.register_blueprint(api, url_prefix='/api')

    # Cria as tabelas do banco de dados (caso necessário)
    with app.app_context():
        db.create_all()


#    print("\nRotas disponíveis:")
#    for rule in app.url_map.iter_rules():
#       print(rule)
        
        
    return app