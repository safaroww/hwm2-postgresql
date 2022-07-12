import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='123456c',
    host='localhost',
    port='5432',
    database='movie_db'
)

cursor = connection.cursor()

query = '''
CREATE TABLE film ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    desc TEXT,
    watch_count INT DEFAULT 0,
    genre_id INT,
    date DATE,
    has_fragman BOOLEAN
);
'''


query2 = '''
CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    product_count INT DEFAULT 0,
    is_new BOOLEAN NOT NULL,
    seller_id INT,
    date DATE,
    time TIME,
    last_usage DATE,
    price INT NOT NULL,
);
'''