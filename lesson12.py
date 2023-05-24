from sqlite3 import connect


conn = connect('db.sqlite3')
cur = conn.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) NOT NULL UNIQUE
    );
''')
conn.commit()

# cur.executemany('''
#     INSERT INTO category (name)
#     VALUES (?);
# ''', (('Coffe', ), ('Tea', )))
# conn.commit()

# cur.execute('''
#     DELETE FROM category
#     WHERE id >= ? OR name = ?;
# ''', (3, 'Tea'))
# conn.commit()


# cur.execute('''
#     UPDATE category SET name = ? WHERE id = ?;
# ''', ('Кофе', 1))
# conn.commit()

# cur.execute('''
#     SELECT * FROM category
#     ORDER BY id ASC;
# ''')
# print(cur.fetchall())
