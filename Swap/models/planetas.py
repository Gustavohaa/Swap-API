from flask import jsonify, request
import requests
from config.database import conectar_banco  


def get_planetas():
    response = requests.get('https://swapi.dev/api/planets/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Não foi possível recuperar os planetas.'}), 500

def get_planeta(id):
    response = requests.get(f'https://swapi.dev/api/planets/{id}/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Planeta não encontrado.'}), 404

def save_planeta(id):
    response = requests.get(f'https://swapi.dev/api/planets/{id}/')
    if response.status_code == 200:
        data = response.json()
        conn = conectar_banco()
        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM planetas WHERE id = ?', (id,))
        if cursor.fetchone():
            return jsonify({'error': 'Planeta já salvo no banco de dados.'}), 400

        
        cursor.execute('''INSERT INTO planetas (
            id, name, rotation_period, orbital_period, diameter, 
            climate, gravity, terrain, surface_water, population, 
            residents, films, created, edited, url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (
            id, data['name'], data['rotation_period'], data['orbital_period'], 
            data['diameter'], data['climate'], data['gravity'], data['terrain'], 
            data['surface_water'], data['population'], 
            str(data['residents']), str(data['films']), data['created'], 
            data['edited'], data['url']
        ))

        conn.commit()
        conn.close()
        return jsonify({'message': 'Planeta salvo com sucesso.'})
    else:
        return jsonify({'error': 'Planeta não encontrado.'}), 404

def delete_planeta(id):
    conn = conectar_banco()
    cursor = conn.cursor()

    
    cursor.execute('SELECT * FROM planetas WHERE id = ?', (id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({'error': 'Planeta não encontrado no banco de dados.'}), 404
    
   
    cursor.execute('DELETE FROM planetas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Planeta deletado com sucesso.'})