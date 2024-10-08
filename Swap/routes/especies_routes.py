from flask import Blueprint
from models.especies import get_especie, get_especies, save_especie, delete_especie

especies_blueprint = Blueprint('especies', __name__)

@especies_blueprint.route('/', methods=['GET'])
def listar_especies():
    return get_especies()

@especies_blueprint.route('/<int:id>', methods=['GET'])
def obter_nave(id):
    return get_especie(id)

@especies_blueprint.route('/<int:id>/save', methods=['POST'])
def salvar_nave(id):
    return save_especie(id)

@especies_blueprint.route('/<int:id>/delete', methods=['DELETE'])
def deletar_nave(id):
    return delete_especie(id)