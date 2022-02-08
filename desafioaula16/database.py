import MySQLdb 
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306)


# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `models`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `models` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `restaurant`;
    CREATE TABLE `restaurant` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `plate` varchar(50) COLLATE utf8_bin NOT NULL,
      `category` varchar(40) COLLATE utf8_bin NOT NULL,
      `price` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `user` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `password` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO user (id, name, password) VALUES (%s, %s, %s)',
      [
            ('allan', 'Allan Machado', '1234'),
            ('lorena', 'Lorena Machado', '5678'),
      ])

cursor.execute('select * from user')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo prato, categoria e preços
cursor.executemany(
      'INSERT INTO restaurant (plate, category, price) VALUES (%s, %s, %s)',
      [
            ('Moqueca de Camarao', 'Frutos do Mar', '150,00'),
            ('Moqueca de Peixe', 'Frutos do Mar', '120,00'),
            ('Lasanha', 'Massas', '95,00'),
      ])

cursor.execute('select * from restaurant')
print(' -------------  Restaurants:  -------------')
for restaurant in cursor.fetchall():
    print(restaurant[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()