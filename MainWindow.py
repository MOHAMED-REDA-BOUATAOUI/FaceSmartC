# This Python file uses the following encoding: utf-8
# Importer les modules nécessaires de PyQt
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QFile, QTextStream

# Fonction pour charger et appliquer le style CSS
def charger_style():
    # Créer une instance de l'application Qt
    app = QApplication([])

    # Créer un bouton
    button = QPushButton("Cliquez-moi")

    # Donner à ce bouton un ID pour le styliser ultérieurement
    button.setObjectName("b1")

    # Charger le fichier de style CSS
    style_file = QFile("style.css")  # Assurez-vous que le fichier CSS est dans le même répertoire que votre script
    style_file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(style_file)
    app.setStyleSheet(stream.readAll())

    # Afficher le bouton
    button.show()

    # Exécuter l'application Qt
    app.exec_()

# Appeler la fonction pour charger et appliquer le style
charger_style()



