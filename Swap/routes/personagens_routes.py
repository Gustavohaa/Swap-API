from flask import Blueprint
from models.personagens import get_personagem, get_personagens, save_personagem, delete_personagem

personagens_blueprint = Blueprint('personagens', __name__)

@personagens_blueprint.route('/', methods=['GET'])
def listar_personagem():
    return get_personagens()

@personagens_blueprint.route('/<int:id>', methods=['GET'])
def obter_personagem(id):
    return get_personagem(id)

@personagens_blueprint.route('/<int:id>/save', methods=['POST'])
def salvar_personagem(id):
    return save_personagem(id)

@personagens_blueprint.route('/<int:id>/delete', methods=['DELETE'])
def deletar_personagem(id):
    return delete_personagem(id)