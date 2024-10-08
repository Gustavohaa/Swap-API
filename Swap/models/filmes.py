from flask import jsonify, request
import requests
from config.database import conectar_banco  


def get_filmes():
    response = requests.get('https://swapi.dev/api/films/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Não foi possível recuperar os filmes.'}), 500


def get_filme(id):
    response = requests.get(f'https://swapi.dev/api/films/{id}/')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Filme não encontrado.'}), 404


def save_filme(id):
    response = requests.get(f'https://swapi.dev/api/films/{id}/')
    if response.status_code == 200:
        data = response.json()
        conn = conectar_banco()
        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM filmes WHERE id = ?', (id,))
        if cursor.fetchone():
            return jsonify({'error': 'Filme já salvo no banco de dados.'}), 400

        
        cursor.execute('''
        INSERT INTO filmes (id, titulo, episodio_id, abertura, diretor, produtores, data_lancamento, personagens, planetas, naves, veiculos, especies, created, edited, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id, data['title'], data['episode_id'], data['opening_crawl'], data['director'], data['producer'], 
              data['release_date'], str(data['characters']), str(data['planets']), str(data['starships']), 
              str(data['vehicles']), str(data['species']), data['created'], data['edited'], data['url']))

        conn.commit()
        conn.close()
        return jsonify({'message': 'Filme salvo com sucesso.'})
    else:
        return jsonify({'error': 'Filme não encontrado.'}), 404


def delete_filme(id):
    conn = conectar_banco()
    cursor = conn.cursor()

   
    cursor.execute('SELECT * FROM filmes WHERE id = ?', (id,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({'error': 'Filme não encontrado no banco de dados.'}), 404

   
    cursor.execute('DELETE FROM filmes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Filme deletado com sucesso.'})