from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QLabel,QFileDialog
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon
import sys

class Settings(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")  # Set your window title
        self.setGeometry(100,100,300,200)
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        # Create buttons

        # Define the size of the buttons
        button_size = QSize(50, 20)  # Adjust the size as needed
        icon_size = QSize(10, 10)

        self.path_label = QLabel("Select recording Path:")
        self.input_select = QLineEdit()
        # Create buttons and set their size
        self.save_button = QPushButton('Save')
        self.save_button.setIcon(QIcon('icons/user.png'))
        self.save_button.setFixedSize(button_size)
        self.save_button.setIconSize(icon_size)

        layout.addWidget(self.path_label, 0, 0)
        layout.addWidget(self.input_select, 1, 0)
        layout.addWidget(self.save_button, 2, 0)
        self.setLayout(layout)

    def save_as_excel(self):
        # Prompt user for location and name of the Excel file
        options = QFileDialog.Options()                 

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    
    ex = Settings()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()