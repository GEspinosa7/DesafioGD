from PyQt5 import uic,QtWidgets
import mysql.connector


#BANCO DE DADOS
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CHL8xXHp5AfZC8AV",
    database="desafio_gd"
)

def cadastrar_pessoa():
    nome = cadastro_pessoas.lineEditNome.text()
    sobrenome = cadastro_pessoas.lineEditSobrenome.text()

    print("Nome: ", nome)
    print("Sobrenome: ", sobrenome)

    #SALVANDO DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    sql = "INSERT INTO pessoas (nome, sobrenome) VALUES (%s,%s)"
    data = (str(nome), str(sobrenome))
    cursor.execute(sql,data)
    db.commit()



def call_cadastro_pessoa():
    cadastro_pessoas.show()


# insert into pessoas (nome,sobrenome) values (nome,sobrenome);



app = QtWidgets.QApplication([])

# CARREGA SCREENS
mainScreen = uic.loadUi("sistema/screens/main.ui")
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")

# EVENT LISTENER
mainScreen.pessoasBtnCadastrar.clicked.connect(call_cadastro_pessoa)
cadastro_pessoas.btnCadastrar.clicked.connect(cadastrar_pessoa)

# MOSTRA MAIN SCREEN
mainScreen.show()

# EXECUTA O APP
app.exec()
