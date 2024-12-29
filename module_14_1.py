import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f'User{i}', f'example{i}@gmail.com', 10*i, 1000))

# for i in range(1, 11):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 = ?",
#                    (500, 0))

# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id %3 = ?", (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

data = cursor.fetchall()

for user in data:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


connection.commit()
connection.close()
