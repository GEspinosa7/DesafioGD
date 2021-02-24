from PyQt5 import uic,QtWidgets
from pessoa import  call_cadastro_pessoa, call_lista_pessoas
from salas import call_lista_salas, call_cadastro_sala
from salas_cafe import call_lista_salas_cafe, call_cadastro_sala_cafe

import images


app = QtWidgets.QApplication([])

# CARREGA SCREENS
mainScreen = uic.loadUi("sistema/screens/main.ui")

## PESSOAS
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")
lista_salas = uic.loadUi("sistema/screens/listaSalas.ui")
lista_salas_cafe = uic.loadUi("sistema/screens/listaSalasCafe.ui")

# EVENT LISTENERS
mainScreen.pessoasBtnCadastrar_3.clicked.connect(call_cadastro_pessoa)
mainScreen.pessoasBtnConsultar_3.clicked.connect(call_lista_pessoas)
mainScreen.salasBtnCadastrar_2.clicked.connect(call_cadastro_sala)
mainScreen.salasBtnConsultar_2.clicked.connect(call_lista_salas)
mainScreen.salasCafeBtnCadastrar_2.clicked.connect(call_cadastro_sala_cafe)
mainScreen.salasCafeBtnConsultar_2.clicked.connect(call_lista_salas_cafe)

mainScreen.show()

# EXECUTA O APP
app.exec()