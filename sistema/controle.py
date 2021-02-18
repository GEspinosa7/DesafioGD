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

    cadastro_pessoas.close()



def call_cadastro_pessoa():
    cadastro_pessoas.show()


def call_lista_pessoas():
    lista_pessoas.show()

    cursor = db.cursor()
    sql = "SELECT * FROM pessoas"
    cursor.execute(sql)
    rdata = cursor.fetchall()

    lista_pessoas.tableWidget.setRowCount(len(rdata))
    lista_pessoas.tableWidget.setColumnCount(3)

    for i in range(0, len(rdata)):
        for j in range(0, 3):
            lista_pessoas.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))


def deletar_pessoa():
    line = lista_pessoas.tableWidget.currentRow()
    lista_pessoas.tableWidget.removeRow(line)

    cursor = db.cursor()
    cursor.execute("SELECT id FROM pessoas")
    rdata = cursor.fetchall()
    id = rdata[line][0]
    cursor.execute("DELETE FROM pessoas WHERE id=" + str(id))

    print(line)


app = QtWidgets.QApplication([])

# CARREGA SCREENS
mainScreen = uic.loadUi("sistema/screens/main.ui")
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")

# EVENT LISTENER
mainScreen.pessoasBtnCadastrar.clicked.connect(call_cadastro_pessoa)
mainScreen.pessoasBtnConsultar.clicked.connect(call_lista_pessoas)
cadastro_pessoas.btnCadastrar.clicked.connect(cadastrar_pessoa)
lista_pessoas.btnDeletar.clicked.connect(deletar_pessoa)

# MOSTRA MAIN SCREEN
mainScreen.show()

# EXECUTA O APP
app.exec()
