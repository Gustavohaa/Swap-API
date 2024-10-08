from flask import jsonify
import requests
from config.database import conectar_banco  

def get_favoritos():
    conn = conectar_banco()
    cursor = conn.cursor()
  
    cursor.execute('SELECT personagem, filme, nave, veiculo, especie, planeta, aluno1_nome, aluno1_matricula, aluno2_nome, aluno2_matricula, curso, universidade, periodo FROM favoritos')
    favoritos = cursor.fetchall()

    favoritos_list = []

    for fav in favoritos:
        personagem, filme, nave, veiculo, especie, planeta, aluno1_nome, aluno1_matricula, aluno2_nome, aluno2_matricula, curso, universidade, periodo = fav

        favoritos_list.append({
            'personagem': personagem,
            'filme': filme,
            'nave': nave,
            'veiculo': veiculo,
            'especie': especie,
            'planeta': planeta,
            'nome_aluno': aluno1_nome,
            'matricula_aluno': aluno1_matricula,
            'nome_aluno2': aluno2_nome,
            'matricula_aluno2': aluno2_matricula,
            'curso': curso,
            'universidade': universidade,
            'periodo': periodo
        })

    conn.close()

    return jsonify(favoritos_list)

def save_favorito(personagem_id, filme_id, nave_id, veiculo_id, especie_id, planeta_id):
    conn = conectar_banco()
    cursor = conn.cursor()

    
    personagem_response = requests.get(f'https://swapi.dev/api/people/{personagem_id}/')
    if personagem_response.status_code != 200:
        return jsonify({'error': 'Personagem não encontrado.'}), 404
    personagem_data = personagem_response.json()

    
    filme_response = requests.get(f'https://swapi.dev/api/films/{filme_id}/')
    if filme_response.status_code != 200:
        return jsonify({'error': 'Filme não encontrado.'}), 404
    filme_data = filme_response.json()

    
    nave_response = requests.get(f'https://swapi.dev/api/starships/{nave_id}/')
    if nave_response.status_code != 200:
        return jsonify({'error': 'Nave não encontrada.'}), 404
    nave_data = nave_response.json()

   
    veiculo_response = requests.get(f'https://swapi.dev/api/vehicles/{veiculo_id}/')
    if veiculo_response.status_code != 200:
        return jsonify({'error': 'Veículo não encontrado.'}), 404
    veiculo_data = veiculo_response.json()

    
    especie_response = requests.get(f'https://swapi.dev/api/species/{especie_id}/')
    if especie_response.status_code != 200:
        return jsonify({'error': 'Espécie não encontrada.'}), 404
    especie_data = especie_response.json()

    
    planeta_response = requests.get(f'https://swapi.dev/api/planets/{planeta_id}/')
    if planeta_response.status_code != 200:
        return jsonify({'error': 'Planeta não encontrado.'}), 404
    planeta_data = planeta_response.json()

    
    cursor.execute('''
        SELECT * FROM favoritos 
        WHERE personagem = ? 
        AND filme = ? 
        AND nave = ? 
        AND veiculo = ? 
        AND especie = ? 
        AND planeta = ? 
        AND aluno1_nome = ? 
        AND aluno1_matricula = ?
    ''', (
        personagem_data['name'],
        filme_data['title'],
        nave_data['name'],
        veiculo_data['name'],
        especie_data['name'],
        planeta_data['name'],
        'Gustavo', '98023041'
    ))
    if cursor.fetchone():
        return jsonify({'error': 'Favorito já salvo no banco de dados.'}), 400

    
    cursor.execute('''
        INSERT INTO favoritos (personagem, filme, nave, veiculo, especie, planeta, aluno1_nome, aluno1_matricula, aluno2_nome, aluno2_matricula, curso, universidade, periodo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        personagem_data['name'],
        filme_data['title'],
        nave_data['name'],
        veiculo_data['name'],
        especie_data['name'],
        planeta_data['name'],
        'Gustavo', '98023041', ' ', ' ', 'Sistemas de Informação', 'Univas ', '7º período'
    ))

    conn.commit()
    conn.close()
    return jsonify({"message": "Favorito salvo com sucesso!"})

    
    

    