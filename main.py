import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class CoffeeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Coffee App')
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.show()

        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()

        output = ''
        for row in rows:
            output += f"ID: {row[0]}\n"
            output += f"Название сорта: {row[1]}\n"
            output += f"Степень обжарки: {row[2]}\n"
            output += f"Молотый/в зернах: {row[3]}\n"
            output += f"Описание вкуса: {row[4]}\n"
            output += f"Цена: {row[5]}\n"
            output += f"Объем упаковки: {row[6]}\n\n"

        self.label.setText(output)

        conn.close()

if __name__ == '__main__':
    app = QApplication([])
    window = CoffeeApp()
    app.exec_()
