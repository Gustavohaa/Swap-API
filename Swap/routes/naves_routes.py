from flask import Blueprint
from models.naves import get_nave, get_naves, save_nave, delete_nave

naves_blueprint = Blueprint('naves', __name__)

@naves_blueprint.route('/', methods=['GET'])
def listar_naves():
    return get_naves()

@naves_blueprint.route('/<int:id>', methods=['GET'])
def obter_nave(id):
    return get_nave(id)

@naves_blueprint.route('/<int:id>/save', methods=['POST'])
def salvar_nave(id):
    return save_nave(id)

@naves_blueprint.route('/<int:id>/delete', methods=['DELETE'])
def deletar_nave(id):
    return delete_nave(id)