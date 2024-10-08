from flask import jsonify, request
import requests
from config.database import conectar_banco  


def get_especies():
    response = requests.get('https://swapi.dev/api/species/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Não foi possível recuperar as espécies.'}), 500


def get_especie(id):
    response = requests.get(f'https://swapi.dev/api/species/{id}/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Espécie não encontrada.'}), 404


def save_especie(id):
    response = requests.get(f'https://swapi.dev/api/species/{id}/')
    if response.status_code == 200:
        data = response.json()
        conn = conectar_banco()
        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM especies WHERE id = ?', (id,))
        if cursor.fetchone():
            return jsonify({'error': 'Espécie já salva no banco de dados.'}), 400

        
        cursor.execute('''INSERT INTO especies (
        id, name, classification, designation, average_height, skin_colors, 
        hair_colors, eye_colors, average_lifespan, homeworld, language, 
        people, films, created, edited, url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (
            id, data['name'], data['classification'], data['designation'], 
            data['average_height'], data['skin_colors'], data['hair_colors'], 
            data['eye_colors'], data['average_lifespan'], data['homeworld'], 
            data['language'], str(data['people']), str(data['films']), 
            data['created'], data['edited'], data['url']
        ))

        conn.commit()
        conn.close()
        return jsonify({'message': 'Espécie salva com sucesso.'})
    else:
        return jsonify({'error': 'Espécie não encontrada.'}), 404


def delete_especie(id):
    conn = conectar_banco()
    cursor = conn.cursor()

    
    cursor.execute('SELECT * FROM especies WHERE id = ?', (id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({'error': 'Espécie não encontrada no banco de dados.'}), 404
    
    
    cursor.execute('DELETE FROM especies WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Espécie deletada com sucesso.'})
