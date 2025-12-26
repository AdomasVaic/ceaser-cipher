import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from caeser_cipher import caeser_decrypt, caeser_encrypt

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.plain_text = QtWidgets.QLineEdit()
        self.cipher_text = QtWidgets.QLineEdit()
        self.encrypt_btn = QtWidgets.QPushButton("encrypt")
        self.decrypt_btn = QtWidgets.QPushButton("decrypt")
        self.key_slider = QtWidgets.QSlider()
        self.key_slider.setRange(0, 25)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.encrypt_btn)
        self.layout.addWidget(self.decrypt_btn)
        self.layout.addWidget(self.plain_text)
        self.layout.addWidget(self.cipher_text)
        self.layout.addWidget(self.key_slider)

        self.encrypt_btn.clicked.connect(self.encrypt)
        self.decrypt_btn.clicked.connect(self.decrypt)

    @QtCore.Slot()
    def encrypt(self):
        encrypted_text = caeser_encrypt(self.key_slider.value(), self.plain_text.text())
        self.cipher_text.setText(encrypted_text)
    
    @QtCore.Slot()
    def decrypt(self):
        decrypted_text = caeser_decrypt(self.key_slider.value(), self.cipher_text.text())
        self.plain_text.setText(decrypted_text)

    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())