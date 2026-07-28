import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# res = cursor.execute('SELECT name, age FROM user WHERE age=20')
# res = cursor.execute('SELECT name, age FROM user WHERE age BETWEEN 22 AND 26')
# res = cursor.execute('SELECT name, age FROM user WHERE age in (21, 19)')
# res = cursor.execute('SELECT name, age FROM user WHERE name LIKE "%A____"')
# res = cursor.execute("""SELECT name,
# age FROM user WHERE name LIKE '%A____' or  age=20""")
# cursor.execute('''INSERT INTO user (name, age) VALUES ('Рeter', 23)''')
cursor.execute('''INSERT INTO user (name, age) 
VALUES (?,?)''', ('Рeter', 23))
conn.commit()
res = cursor.execute('SELECT * FROM user')
for row in res:
    print(row)