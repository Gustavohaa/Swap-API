# Star Wars API

Este projeto consiste em uma API desenvolvida em Python usando Flask, integrada com um banco de dados SQLite para gerenciar dados relacionados ao universo de Star Wars, como personagens, filmes, naves, veículos, espécies e planetas, utilizando a SWAPI (Star Wars API). A aplicação inclui rotas para obter, salvar e deletar dados do banco de dados, além de funcionalidades de favoritos.

Estrutura do Projeto
O projeto está dividido em módulos e rotas da seguinte forma:

config/database.py: Funções de conexão e inicialização do banco de dados SQLite.

models/: Funções para manipulação dos dados (personagens, filmes, espécies, naves, etc.).

routes/: Blueprints para definir as rotas de cada categoria de dados (ex.: filmes, personagens, naves, etc.).

Tecnologias Utilizadas

Insomnia: Ferramenta utilizada para testar as requisições POST e DELETE das rotas da API.

Flask: Framework web para criar a API e gerenciar rotas.

SQLite3: Banco de dados relacional para armazenar as informações localmente.

SWAPI: API externa utilizada para obter informações sobre o universo de Star Wars.

requests: Biblioteca para realizar requisições HTTP à SWAPI.

Configuração do Ambiente

Instalação das dependências:

Flask: pip install Flask

requests: pip install requests

sqlite3: Nativo no Python

Inicialização do Banco de Dados: No início da execução, o banco de dados SQLite é inicializado e as tabelas necessárias são criadas se não existirem.

Funcionalidades
Tabelas Criadas
personagens: Armazena informações dos personagens de Star Wars.

filmes: Armazena detalhes sobre os filmes.

naves: Armazena informações sobre as naves espaciais.

veiculos: Armazena dados de veículos.

especies: Armazena informações das espécies.

planetas: Armazena detalhes dos planetas.

favoritos: Tabela para salvar itens favoritos, como personagem, filme, nave, etc.
Rotas

Abaixo estão algumas rotas principais implementadas:

GET /especies : Retorna todas as espécies da SWAPI.

GET /especies/<id>: Retorna detalhes de uma espécie específica pelo id.

POST /especies/<id>/save: Salva uma espécie no banco de dados local.

DELETE /especies/<id>/delete: Remove uma espécie do banco de dados.

GET /favoritos

para o post nós passamos primeiramente o id do personagem,id do filme, id da nave, id do veiculo,id da especie e por fim o id do planeta
POST /favoritos/4/3/5/6/7/2/save
