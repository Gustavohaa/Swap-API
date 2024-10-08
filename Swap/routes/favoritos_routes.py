from flask import Blueprint, request, jsonify
from models.favoritos import get_favoritos, save_favorito


favoritos_blueprint = Blueprint('favoritos', __name__)

@favoritos_blueprint.route('/', methods=['GET'])
def listar_favoritos():
    return get_favoritos()

@favoritos_blueprint.route('<int:personagem_id>/<int:filme_id>/<int:nave_id>/<int:veiculo_id>/<int:especie_id>/<int:planeta_id>/save', methods=['POST'])
def salvar_favorito_route(personagem_id, filme_id, nave_id, veiculo_id, especie_id, planeta_id):
    return save_favorito(personagem_id, filme_id, nave_id, veiculo_id, especie_id, planeta_id)