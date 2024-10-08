from flask import jsonify, request
import requests
from config.database import conectar_banco  


def get_naves():
    response = requests.get('https://swapi.dev/api/starships/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Não foi possível recuperar as naves.'}), 500


def get_nave(id):
    response = requests.get(f'https://swapi.dev/api/starships/{id}/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Nave não encontrada.'}), 404


def save_nave(id):
    response = requests.get(f'https://swapi.dev/api/starships/{id}/')
    if response.status_code == 200:
        data = response.json()
        conn = conectar_banco()
        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM naves WHERE id = ?', (id,))
        if cursor.fetchone():
            return jsonify({'error': 'Nave já salva no banco de dados.'}), 400

        
        cursor.execute('''
        INSERT INTO naves (id, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, hyperdrive_rating, MGLT, starship_class, pilots, films, created, edited, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id, data['name'], data['model'], data['manufacturer'], data['cost_in_credits'], data['length'],
              data['max_atmosphering_speed'], data['crew'], data['passengers'], data['cargo_capacity'], 
              data['consumables'], data['hyperdrive_rating'], data['MGLT'], data['starship_class'], 
              str(data['pilots']), str(data['films']), data['created'], data['edited'], data['url']))

        conn.commit()
        conn.close()
        return jsonify({'message': 'Nave salva com sucesso.'})
    else:
        return jsonify({'error': 'Nave não encontrada.'}), 404


def delete_nave(id):
    conn = conectar_banco()
    cursor = conn.cursor()

   
    cursor.execute('SELECT * FROM naves WHERE id = ?', (id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({'error': 'Nave não encontrada no banco de dados.'}), 404

    
    cursor.execute('DELETE FROM naves WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Nave deletada com sucesso.'})