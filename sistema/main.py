from PyQt5 import uic,QtWidgets
from pessoa import  call_cadastro_pessoa, call_lista_pessoas

app = QtWidgets.QApplication([])

# CARREGA SCREENS
mainScreen = uic.loadUi("sistema/screens/main.ui")

## PESSOAS
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")

# EVENT LISTENERS
mainScreen.pessoasBtnCadastrar.clicked.connect(call_cadastro_pessoa)
mainScreen.pessoasBtnConsultar.clicked.connect(call_lista_pessoas)

mainScreen.show()

# EXECUTA O APP
app.exec()
