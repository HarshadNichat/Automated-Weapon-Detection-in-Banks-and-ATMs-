from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import webbrowser
import requests
import json
from settings_window import SettingsWindow

# LoginWindow class that manages login and opening the setting window
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi('UI/login_window.ui', self)

        self.register_button.clicked.connect(self.go_to_register_page)
        self.login_button.clicked.connect(self.login)

        self.popup = QMessageBox()
        self.popup.setWindowTitle("Failed")

        self.show()

    # Open registration page
    def go_to_register_page(self):
        webbrowser.open('http://127.0.0.1:8000/register/')

    # Login function that manages the token authentication
    def login(self):
        demo_token = "your_demo_token_here"
        location = "default_location"  # Provide default location
        receiver = "default_receiver"  # Provide default receiver
        self.open_settings_window(demo_token, location, receiver)

    # Opens settings window, passes the received token and closes login window
    def open_settings_window(self, token, location, receiver):
        self.settings_window = SettingsWindow(token, location, receiver)
        self.settings_window.displayInfo()
        self.close()
