from flask import jsonify, request
import requests
from config.database import conectar_banco  


def get_veiculos():
    response = requests.get('https://swapi.dev/api/vehicles/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Não foi possível recuperar os veículos.'}), 500


def get_veiculo(id):
    response = requests.get(f'https://swapi.dev/api/vehicles/{id}/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Veículo não encontrado.'}), 404


def save_veiculo(id):
    response = requests.get(f'https://swapi.dev/api/vehicles/{id}/')
    if response.status_code == 200:
        data = response.json()
        conn = conectar_banco()
        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM veiculos WHERE id = ?', (id,))
        if cursor.fetchone():
            return jsonify({'error': 'Veículo já salvo no banco de dados.'}), 400

        
        cursor.execute('''INSERT INTO veiculos (
        id, name, model, manufacturer, cost_in_credits, length, 
        max_atmosphering_speed, crew, passengers, cargo_capacity, 
        consumables, vehicle_class, pilots, films, created, edited, url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (
            id, data['name'], data['model'], data['manufacturer'], 
            data['cost_in_credits'], data['length'], 
            data['max_atmosphering_speed'], data['crew'], data['passengers'], 
            data['cargo_capacity'], data['consumables'], data['vehicle_class'], 
            str(data['pilots']), str(data['films']), data['created'], 
            data['edited'], data['url']
        ))

        conn.commit()
        conn.close()
        return jsonify({'message': 'Veículo salvo com sucesso.'})
    else:
        return jsonify({'error': 'Veículo não encontrado.'}), 404


def delete_veiculo(id):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM veiculos WHERE id = ?', (id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({'error': 'Veículo não encontrado no banco de dados.'}), 404
    
    cursor.execute('DELETE FROM veiculos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Veículo deletado com sucesso.'})
