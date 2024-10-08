from flask import Blueprint
from models.planetas import get_planetas, get_planeta, save_planeta, delete_planeta

planetas_blueprint = Blueprint('planetas', __name__)

@planetas_blueprint.route('/', methods=['GET'])
def listar_planetas():
    return get_planetas()

@planetas_blueprint.route('/<int:id>', methods=['GET'])
def obter_planeta(id):
    return get_planeta(id)

@planetas_blueprint.route('/<int:id>/save', methods=['POST'])
def salvar_planeta(id):
    return save_planeta(id)

@planetas_blueprint.route('/<int:id>/delete', methods=['DELETE'])
def deletar_planeta(id):
    return delete_planeta(id)