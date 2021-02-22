from PyQt5 import uic,QtWidgets
import mysql.connector
from functools import partial


#BANCO DE DADOS
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CHL8xXHp5AfZC8AV",
    database="desafio"
)

    # line = lista_pessoas.tableWidget.currentRow()
    # cursor = db.cursor()
    # cursor.execute("SELECT idPessoa FROM pessoas")
    # rdata = cursor.fetchall()
    # id = rdata[line][0]
    # cursor.execute("SELECT nome, sobrenome FROM pessoas WHERE idPessoa=" + str(id))
    # pessoa = cursor.fetchall()

    # alterar_dados_pessoa.show()

    # alterar_dados_pessoa.lblNome_disabled.setText(str(pessoa[0][0]))
    # alterar_dados_pessoa.lblSobrenome_disabled.setText(str(pessoa[0][1]))

    # alterar_dados_pessoa.btnSalvarAlteracao.clicked.connect(partial(update, id))

def cadastrar_pessoa():
    nome = cadastro_pessoas.lineEditNome.text()
    sobrenome = cadastro_pessoas.lineEditSobrenome.text()
    line_sala = cadastro_pessoas.tableWidget_sala.currentRow()
    line_sala_cafe = cadastro_pessoas.tableWidget_cafe.currentRow()

    #SALVANDO DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    
    cursor.execute("SELECT idSala FROM salas")
    s_data = cursor.fetchall()

    cursor.execute("SELECT idCafe FROM cafes")
    sc_data = cursor.fetchall()

    id_sala = s_data[line_sala][0]
    id_sala_cafe = sc_data[line_sala_cafe][0] 

    sql = "INSERT INTO pessoas (nome, sobrenome, idSala, idCafe) VALUES (%s, %s, %s, %s)"
    data = (str(nome), str(sobrenome), str(id_sala), str(id_sala_cafe))
    cursor.execute(sql,data)
    db.commit()

    cadastro_pessoas.close()


def call_cadastro_pessoa():
    call_lista_salas()
    call_lista_salas_cafe()
    cadastro_pessoas.show()


def call_lista_salas():
    cursor = db.cursor()
    sql = "SELECT * FROM salas"
    cursor.execute(sql)
    rdata = cursor.fetchall()

    cadastro_pessoas.tableWidget_sala.setRowCount(len(rdata))
    cadastro_pessoas.tableWidget_sala.setColumnCount(3)


    for i in range(0, len(rdata)):
        for j in range(0, 3):
            cadastro_pessoas.tableWidget_sala.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))

def call_lista_salas_cafe():
    cursor = db.cursor()
    sql = "SELECT * FROM cafes"
    cursor.execute(sql)
    rdata = cursor.fetchall()

    cadastro_pessoas.tableWidget_cafe.setRowCount(len(rdata))
    cadastro_pessoas.tableWidget_cafe.setColumnCount(3)

    for i in range(0, len(rdata)):
        for j in range(0, 3):
            cadastro_pessoas.tableWidget_cafe.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))

def call_lista_pessoas():
    lista_pessoas.show()

    cursor = db.cursor()
    sql = "SELECT * FROM pessoas"
    cursor.execute(sql)
    rdata = cursor.fetchall()

    lista_pessoas.tableWidget.setRowCount(len(rdata))
    lista_pessoas.tableWidget.setColumnCount(5)

    for i in range(0, len(rdata)):
        for j in range(0, 5):
            lista_pessoas.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))


def deletar_pessoa():
    line = lista_pessoas.tableWidget.currentRow()
    lista_pessoas.tableWidget.removeRow(line)

    cursor = db.cursor()
    cursor.execute("SELECT idPessoa FROM pessoas")
    rdata = cursor.fetchall()
    id = rdata[line][0]
    cursor.execute("DELETE FROM pessoas WHERE idPessoa=" + str(id))
    db.commit()

def update(id):
    nome = alterar_dados_pessoa.lineEditNome.text()
    sobrenome = alterar_dados_pessoa.lineEditSobrenome.text()

    #AUALIZANDO OS DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    sql = "UPDATE pessoas SET nome = %s, sobrenome = %s WHERE idPessoa = %s"
    data = (str(nome), str(sobrenome), str(id))
    cursor.execute(sql, data)
    db.commit()
    alterar_dados_pessoa.close()

def editar_pessoa():
    line = lista_pessoas.tableWidget.currentRow()
    cursor = db.cursor()
    cursor.execute("SELECT idPessoa FROM pessoas")
    rdata = cursor.fetchall()
    id = rdata[line][0]
    cursor.execute("SELECT nome, sobrenome FROM pessoas WHERE idPessoa=" + str(id))
    pessoa = cursor.fetchall()

    alterar_dados_pessoa.show()

    alterar_dados_pessoa.lblNome_disabled.setText(str(pessoa[0][0]))
    alterar_dados_pessoa.lblSobrenome_disabled.setText(str(pessoa[0][1]))

    alterar_dados_pessoa.btnSalvarAlteracao.clicked.connect(partial(update, id))


app = QtWidgets.QApplication([])

# CARREGA SCREENS
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")
alterar_dados_pessoa = uic.loadUi("sistema/screens/alterarDadosPessoa.ui")

# EVENT LISTENER
cadastro_pessoas.btnCadastrar.clicked.connect(cadastrar_pessoa)
lista_pessoas.btnDeletar.clicked.connect(deletar_pessoa)
lista_pessoas.btnEditar.clicked.connect(editar_pessoa)
