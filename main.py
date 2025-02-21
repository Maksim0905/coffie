from PyQt6 import QtCore, QtSql
from PyQt6.QtWidgets import QMainWindow, QTableView, QApplication, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Information")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.tableView = QTableView()
        self.layout.addWidget(self.tableView)
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffee.sqlite")
        self.db.open()
        self.model = QtSql.QSqlTableModel(self, self.db)
        self.model.setTable("coffee")
        self.model.setEditStrategy(
            QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)
        headers = ["ID", "Variety", "Roasting Degree", "Form",
                   "Taste Description", "Price", "Package Volume"]
        for i, header in enumerate(headers):
            self.model.setHeaderData(
                i, QtCore.Qt.Orientation.Horizontal, header)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
