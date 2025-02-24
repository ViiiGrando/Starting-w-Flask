import mysql.connector
from mysql.connector import errorcode

print("Connecting...")
conn = None
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('There is something wrong with the username or password')
    else:
        print(err)

if conn:
    cursor = conn.cursor()
else:
    print("Connection failed.")
    exit(1)

cursor.execute("DROP DATABASE IF EXISTS `libragames`;")

cursor.execute("CREATE DATABASE `libragames`;")

cursor.execute("USE `libragames`;")

# creating tables
TABLES = {}
TABLES['Games'] = ('''
    CREATE TABLE `games` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    `category` varchar(40) NOT NULL,
    `console` varchar(20) NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
    CREATE TABLE `users` (
    `name` varchar(20) NOT NULL,
    `nickname` varchar(8) NOT NULL,
    `password` varchar(100) NOT NULL,
    PRIMARY KEY (`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
    table_sql = TABLES[table_name]
    try:
        print('Creating table {}:'.format(table_name), end=' ')
        cursor.execute(table_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Already exists')
        else:
            print(err.msg)
    else:
        print('OK')

# inserting users
user_sql = 'INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)'
users = [
    ("Bruno Divino", "BD", "alohomora"),
    ("Camila Ferreira", "Mila", "paozinho"),
    ("Guilherme Louro", "Cake", "python_is_life")
]
cursor.executemany(user_sql, users)

cursor.execute('select * from libragames.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserting games
games_sql = 'INSERT INTO games (name, category, console) VALUES (%s, %s, %s)'
games = [
    ('Tetris', 'Puzzle', 'Atari'),
    ('God of War', 'Hack n Slash', 'PS2'),
    ('Mortal Kombat', 'Fighting', 'PS2'),
    ('Valorant', 'FPS', 'PC'),
    ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
    ('Need for Speed', 'Racing', 'PS2'),
]
cursor.executemany(games_sql, games)

cursor.execute('select * from libragames.games')
print(' -------------  Games:  -------------')
for game in cursor.fetchall():
    print(game[1])

# committing so that changes take effect
conn.commit()

cursor.close()
conn.close()