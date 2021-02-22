from PyQt5 import uic,QtWidgets
from pessoa import  call_cadastro_pessoa, call_lista_pessoas
from salas import call_lista_salas, call_cadastro_sala

app = QtWidgets.QApplication([])

# CARREGA SCREENS
mainScreen = uic.loadUi("sistema/screens/main.ui")

## PESSOAS
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")
lista_salas = uic.loadUi("sistema/screens/listaSalas.ui")

# EVENT LISTENERS
mainScreen.pessoasBtnCadastrar.clicked.connect(call_cadastro_pessoa)
mainScreen.pessoasBtnConsultar.clicked.connect(call_lista_pessoas)
mainScreen.salasBtnCadastrar.clicked.connect(call_cadastro_sala)
mainScreen.salasBtnConsultar.clicked.connect(call_lista_salas)

mainScreen.show()

# EXECUTA O APP
app.exec()
