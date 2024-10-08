from flask import Flask
from config.database import inicializar_banco
from routes.filmes_routes import filmes_blueprint
from routes.personagens_routes import personagens_blueprint
from routes.naves_routes import naves_blueprint
from routes.planetas_routes import planetas_blueprint
from routes.especies_routes import especies_blueprint
from routes.favoritos_routes import favoritos_blueprint
from routes.veiculos_routes import veiculos_blueprint

app = Flask(__name__)

inicializar_banco()

app.register_blueprint(filmes_blueprint, url_prefix='/filmes')
app.register_blueprint(personagens_blueprint, url_prefix='/personagens')
app.register_blueprint(naves_blueprint, url_prefix='/naves')
app.register_blueprint(planetas_blueprint, url_prefix='/planetas')
app.register_blueprint(veiculos_blueprint, url_prefix='/veiculos')
app.register_blueprint(especies_blueprint, url_prefix='/especies')
app.register_blueprint(favoritos_blueprint, url_prefix='/favoritos')

@app.route('/')
def status():
    return {'status': 'Ok'}

if __name__ == '__main__':
    app.run(debug=True)