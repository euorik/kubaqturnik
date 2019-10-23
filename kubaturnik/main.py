import sys # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design # Это наш конвертированный файл дизайна
import pandas as pd

base = pd.read_excel('asset/kubatura.xlsx', index_col='id')#Загружаем данные с кубатурника
diametr = list(base.index)#Список размера диаметра
dlina = list(base.columns)#Список длин
zem = str(diametr)


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        for x in dlina:
            self.comboBox_3.addItem(x)
        for xx in diametr:
            self.comboBox_2.addItem(str(xx))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

