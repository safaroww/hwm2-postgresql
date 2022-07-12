import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='123456c',
    host='localhost',
    port='5432',
    database='company_db'
)

cursor = connection.cursor()

query = """
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary INT NOT NULL DEFAULT 380,
    en_lang BOOLEAN DEFAULT false NOT NULL,
    birth DATE
);
"""

query = """
INSERT INTO employee (name, en_lang, salary, birth)
VALUES 
('Intiqam', TRUE, 2000, '1993-08-12'),
('Vasif', TRUE, 3000, '1990-06-21')
"""

query = '''
SELECT name, salary FROM employee;
'''

query = '''
SELECT * FROM employee;
'''

# print(cursor.fetchall())
# show(cursor)


# rename the table
query = 'ALTER TABLE employee RENAME TO isciler'

def show(cursor):
    print(*[desc[0].ljust(13) for desc in cursor.description], sep='')
    print('-'*80)
    print('\n'.join(''.join(str(z).ljust(13) for z in i) for i in cursor.fetchall()))

# cursor.execute(query)
# connection.commit()



# query = '''
# SELECT name, salary FROM isciler;
# '''
# cursor.execute(query)

# show(cursor)

# query = """
# ALTER TABLE isciler RENAME TO employee
# """

selectall = """
SELECT * FROM employee
"""

# cursor.execute(query)
# connection.commit()

# cursor.execute(query)
# show(cursor)

# query = '''
# ALTER TABLE employee RENAME COLUMN name TO fullname
# '''


# query = '''
# ALTER TABLE employee DROP COLUMN en_lang
# '''


# query = """
# ALTER TABLE employee ADD COLUMN city VARCHAR(50) NOT NULL DEFAULT 'Baku';
# """

# query = """
# DROP TABLE employee
# """


# query = '''
# CREATE TABLE employee(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     salary INT,
#     lang BOOLEAN DEFAULT false,
#     city VARCHAR,
#     birth DATE
# )
# '''

# data = [
#     ['Intiqam', 3000, True, '1993-08-12', 'Quba'],
#     ['Vasif', 4000, True, '1990-06-30', 'Tiflis'],
#     ['Asif', 2500, True, '1994-08-12', 'Bakı'],
#     ['Senan', 1500, False, '1995-04-13', 'Imişli'],
#     ['Ulfet', 2800, True, '1993-08-23', 'Şəmkir'],
#     ['Orxan', 7000, False, '1996-08-07', 'Fuzuli'],
#     ['Cavad', 4500, True, '1970-09-08', 'Kürdəmir'],
# ]

# data = [
#     ['Saide', 3000, True, '1993-05-12', 'Bakı'],
#     ['Eynulla', 1000, True, '1995-03-30', 'Fuzuli'],
#     ['Ayaz', 1300, True, '1996-08-12', 'Bakı'],
#     ['Ayxan', 2800, False, '1994-05-13', 'Imişli'],
#     ['Oguz', 3800, True, '1996-08-23', 'Şəmkir'],
#     ['Altay', 4200, False, '2005-09-07', 'Şəmkir'],
#     ['Aylin', 3500, True, '1970-02-08', 'Bakı'],
# ]

# query = '''
# INSERT INTO employee (name, salary, lang, birth, city) VALUES(%s, %s, %s, %s, %s)
# '''

# for row_data in data:
#     cursor.execute(query, row_data)


query = """
SELECT * FROM employee WHERE city='Bakı';
"""
query = """
SELECT * FROM employee WHERE city!='Bakı';
"""
query = """
SELECT * FROM employee WHERE city!='Bakı' AND lang=TRUE;
"""
query = """
SELECT * FROM employee WHERE (city!='Bakı' AND lang=TRUE) OR salary<3000;
"""
query = """
SELECT * FROM employee WHERE lang=TRUE ORDER BY birth;
"""
query = """
SELECT * FROM employee WHERE lang=TRUE ORDER BY birth DESC;
"""
query = """
SELECT * FROM employee WHERE city IN ('Kürdəmir', 'Imişli', 'Şəmkir') ORDER BY birth DESC;
"""
query = """
SELECT * FROM employee WHERE city IN ('Kürdəmir', 'Imişli', 'Şəmkir') ORDER BY birth DESC LIMIT 3;
"""
# 3-cuden baslayib 3 denesini verdi
query = """
SELECT * FROM employee WHERE city IN ('Kürdəmir', 'Imişli', 'Şəmkir') ORDER BY birth DESC LIMIT 3 OFFSET 2;
"""
# employee.objects.filter(city__in=('Kürdəmir', 'Imişli', 'Şəmkir')).order_by('-birth')[2:5]
query = """
SELECT * FROM employee WHERE salary BETWEEN 3000 AND 4000;
"""
query = """
SELECT * FROM employee WHERE LOWER(name) LIKE 'a%';
"""
query = """
SELECT * FROM employee WHERE name LIKE 'A%';
"""
query = """
SELECT * FROM employee WHERE name LIKE 'Ay%';
"""
query = """
SELECT * FROM employee WHERE name LIKE 'Ay%';
"""
query = """
SELECT * FROM employee WHERE name ~ '^Ay.*n$';
"""
query = """
SELECT * FROM employee WHERE name LIKE 'Ay%n';
"""
query = """
SELECT * FROM employee WHERE name LIKE '%n';
"""
query = """
SELECT * FROM employee WHERE name LIKE '%i%';
"""
query = """
SELECT * FROM employee WHERE name NOT LIKE '%i%';
"""
# with alias
query = """
SELECT 5 * 6 + 3 AS hesab;
"""
query = """
SELECT COUNT(*) FROM employee;
"""
query = """
SELECT COUNT(*) AS say FROM employee;
"""
query = """
SELECT COUNT(*) AS say FROM employee WHERE city='Bakı';
"""
query = """
SELECT COUNT(*) AS say FROM employee WHERE name NOT LIKE '%i%';
"""
query = """
SELECT salary AS eppek_pulu FROM employee;
"""
query = """
SELECT SUM(salary) AS cem FROM employee;
"""
query = """
SELECT SUM(salary) AS cem FROM employee WHERE city!='Bakı';
"""
query = """
SELECT MAX(salary) FROM employee WHERE city!='Bakı';
"""
query = """
SELECT MAX(salary), MIN(SALARY) FROM employee WHERE city!='Bakı';
"""
query = """
SELECT AVG(salary) FROM employee WHERE city!='Bakı';
"""
query = """
SELECT * FROM employee WHERE birth < '1995-1-1';
"""
query = """
SELECT AVG(salary) FROM employee WHERE birth < '1995-1-1';
"""




# cursor.execute(query)
# connection.commit()

# cursor.execute(selectall)
cursor.execute(query)
show(cursor)



