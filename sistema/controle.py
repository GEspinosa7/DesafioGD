from PyQt5 import uic,QtWidgets

def main():
    nome = cadastro_pessoas.lineEditNome.text()
    sobrenome = cadastro_pessoas.lineEditSobrenome.text()
    cpf = cadastro_pessoas.lineEditCPF.text()

    print("Nome: ", nome)
    print("Sobrenome: ", sobrenome)
    print("CPF: ", cpf)



def call_cadastro_pessoa():
    cadastro_pessoas.show()



app = QtWidgets.QApplication([])

# CARREGA SCREENS
mainScreen = uic.loadUi("screens/main.ui")
cadastro_pessoas = uic.loadUi("screens/cadastroPessoas.ui")

# EVENT LISTENER
mainScreen.pessoasBtnCadastrar.clicked.connect(call_cadastro_pessoa)
cadastro_pessoas.btnCadastrar.clicked.connect(main)

# MOSTRA MAIN SCREEN
mainScreen.show()

# EXECUTA O APP
app.exec()
