from flask import Blueprint
from models.veiculos import get_veiculo, get_veiculos, save_veiculo, delete_veiculo

veiculos_blueprint = Blueprint('veiculos', __name__)

@veiculos_blueprint.route('/', methods=['GET'])
def listar_veiculos():
    return get_veiculos()

@veiculos_blueprint.route('/<int:id>', methods=['GET'])
def obter_veiculo(id):
    return get_veiculo(id)

@veiculos_blueprint.route('/<int:id>/save', methods=['POST'])
def salvar_veiculo(id):
    return save_veiculo(id)

@veiculos_blueprint.route('/<int:id>/delete', methods=['DELETE'])
def deletar_veiculo(id):
    return delete_veiculo(id)