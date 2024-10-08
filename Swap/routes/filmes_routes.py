from flask import Blueprint
from models.filmes import get_filme, get_filmes, save_filme, delete_filme

filmes_blueprint = Blueprint('filmes', __name__)

@filmes_blueprint.route('/', methods=['GET'])
def listar_filmes():
    return get_filmes()

@filmes_blueprint.route('/<int:id>', methods=['GET'])
def obter_filme(id):
    return get_filme(id)

@filmes_blueprint.route('/<int:id>/save', methods=['POST'])
def salvar_filme(id):
    return save_filme(id)

@filmes_blueprint.route('/<int:id>/delete', methods=['DELETE'])
def deletar_filme(id):
    return delete_filme(id)