import sqlite3

def conectar_banco():
    return sqlite3.connect('star_wars.db')

def inicializar_banco():
    conn = conectar_banco()
    cursor = conn.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS personagens (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        height TEXT NOT NULL,
        mass TEXT NOT NULL,
        hair_color TEXT NOT NULL,
        skin_color TEXT NOT NULL,
        eye_color TEXT NOT NULL,
        birth_year TEXT NOT NULL,
        gender TEXT NOT NULL,
        homeworld TEXT NOT NULL,
        films TEXT,
        species TEXT,
        vehicles TEXT,
        starships TEXT,
        created TEXT NOT NULL,
        edited TEXT NOT NULL,
        url TEXT NOT NULL
    )''')

    

    cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        episodio_id INTEGER NOT NULL,
        abertura TEXT NOT NULL,
        diretor TEXT NOT NULL,
        produtores TEXT NOT NULL,
        data_lancamento TEXT NOT NULL,
        personagens TEXT,  
        planetas TEXT,      
        naves TEXT,         
        veiculos TEXT,      
        especies TEXT,      
        created TEXT NOT NULL,
        edited TEXT NOT NULL,
        url TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS naves (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        model TEXT NOT NULL,
        manufacturer TEXT NOT NULL,
        cost_in_credits TEXT NOT NULL,
        length TEXT NOT NULL,
        max_atmosphering_speed TEXT NOT NULL,
        crew TEXT NOT NULL,
        passengers TEXT NOT NULL,
        cargo_capacity TEXT NOT NULL,
        consumables TEXT NOT NULL,
        hyperdrive_rating TEXT NOT NULL,
        MGLT TEXT NOT NULL,
        starship_class TEXT NOT NULL,
        pilots TEXT,
        films TEXT,
        created TEXT NOT NULL,
        edited TEXT NOT NULL,
        url TEXT NOT NULL
    )''')
    

    cursor.execute('''CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        model TEXT NOT NULL,
        manufacturer TEXT NOT NULL,
        cost_in_credits TEXT NOT NULL,
        length TEXT NOT NULL,
        max_atmosphering_speed TEXT NOT NULL,
        crew TEXT NOT NULL,
        passengers TEXT NOT NULL,
        cargo_capacity TEXT NOT NULL,
        consumables TEXT NOT NULL,
        vehicle_class TEXT NOT NULL,
        pilots TEXT,
        films TEXT,
        created TEXT NOT NULL,
        edited TEXT NOT NULL,
        url TEXT NOT NULL
    )''')

    

    cursor.execute('''CREATE TABLE IF NOT EXISTS especies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        classification TEXT NOT NULL,
        designation TEXT NOT NULL,
        average_height TEXT NOT NULL,
        skin_colors TEXT NOT NULL,
        hair_colors TEXT NOT NULL,
        eye_colors TEXT NOT NULL,
        average_lifespan TEXT NOT NULL,
        homeworld TEXT,
        language TEXT NOT NULL,
        people TEXT,
        films TEXT,
        created TEXT NOT NULL,
        edited TEXT NOT NULL,
        url TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS planetas (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        rotation_period TEXT NOT NULL,
        orbital_period TEXT NOT NULL,
        diameter TEXT NOT NULL,
        climate TEXT NOT NULL,
        gravity TEXT NOT NULL,
        terrain TEXT NOT NULL,
        surface_water TEXT NOT NULL,
        population TEXT NOT NULL,
        residents TEXT,
        films TEXT NOT NULL,
        created TEXT NOT NULL,
        edited TEXT NOT NULL,
        url TEXT NOT NULL
    )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favoritos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personagem TEXT NOT NULL,
        filme TEXT NOT NULL,
        nave TEXT NOT NULL,
        veiculo TEXT NOT NULL,
        especie TEXT NOT NULL,
        planeta TEXT NOT NULL,
        aluno1_nome TEXT,
        aluno1_matricula TEXT,
        aluno2_nome TEXT,
        aluno2_matricula TEXT,
        curso TEXT,
        universidade TEXT,
        periodo TEXT
    )''')

    conn.commit()
    conn.close()
