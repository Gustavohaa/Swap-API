from flask import jsonify, request
import requests
from config.database import conectar_banco  


def get_personagens():
    response = requests.get('https://swapi.dev/api/people/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Não foi possível recuperar os personagens.'}), 500


def get_personagem(id):
    response = requests.get(f'https://swapi.dev/api/people/{id}/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Personagem não encontrado.'}), 404


def save_personagem(id):
    response = requests.get(f'https://swapi.dev/api/people/{id}/')
    if response.status_code == 200:
        data = response.json()
        conn = conectar_banco()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM personagens WHERE id = ?', (id,))
        if cursor.fetchone():
            return jsonify({'error': 'Personagem já salvo no banco de dados.'}), 400

        cursor.execute('''INSERT INTO personagens (
        id, name, height, mass, hair_color, skin_color, eye_color, 
        birth_year, gender, homeworld, films, species, vehicles, 
        starships, created, edited, url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (
        id, data['name'], data['height'], data['mass'], 
        data['hair_color'], data['skin_color'], data['eye_color'], 
        data['birth_year'], data['gender'], data['homeworld'],str(data['films'])
        ,str(data['species']),str(data['vehicles']),str(data['starships']), 
        data['created'], data['edited'], data['url']
        
))

        conn.commit()
        conn.close()
        return jsonify({'message': 'Personagem salvo com sucesso.'})
    else:
        return jsonify({'error': 'Personagem não encontrado.'}), 404


def delete_personagem(id):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM personagens WHERE id = ?', (id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({'error': 'Personagem não encontrado no banco de dados.'}), 404

    cursor.execute('DELETE FROM personagens WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Personagem deletado com sucesso.'})
