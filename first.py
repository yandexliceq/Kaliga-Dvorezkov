import sqlite3

conn = sqlite3.connect('coffee.sqlite')
cursor = conn.cursor()

cursor.execute("SELECT * FROM coffee")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}")
    print(f"Название сорта: {row[1]}")
    print(f"Степень обжарки: {row[2]}")
    print(f"Молотый/в зернах: {row[3]}")
    print(f"Описание вкуса: {row[4]}")
    print(f"Цена: {row[5]}")
    print(f"Объем упаковки: {row[6]}\n")

conn.close()
