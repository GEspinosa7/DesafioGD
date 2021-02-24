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

def cadastrar_sala_cafe():
    nome = cadastro_salas_cafe.lineEditNome.text()
    capacidade = cadastro_salas_cafe.spinBoxCapacidade.text()
    
    cursor = db.cursor()
    sql = "INSERT INTO cafes (nome, capacidade) VALUES (%s,%s)"
    data = (str(nome), str(capacidade))
    cursor.execute(sql,data)
    db.commit()

    cadastro_salas_cafe.close()


def call_cadastro_sala_cafe():
    cadastro_salas_cafe.show()

def call_lista_salas_cafe():
    lista_salas_cafe.show()

    cursor = db.cursor()
    sql = "SELECT * FROM cafes"
    cursor.execute(sql)
    rdata = cursor.fetchall()

    lista_salas_cafe.tableWidget.setRowCount(len(rdata))
    lista_salas_cafe.tableWidget.setColumnCount(3)

    for i in range(0, len(rdata)):
        for j in range(0, 3):
            lista_salas_cafe.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))


def deletar_sala_cafe():
    line = lista_salas_cafe.tableWidget.currentRow()
    lista_salas_cafe.tableWidget.removeRow(line)

    cursor = db.cursor()
    cursor.execute("SELECT idCafe FROM cafes ")
    rdata = cursor.fetchall()
    id = rdata[line][0]

    cursor.execute("DELETE FROM cafes WHERE idCafe=" + str(id))
    db.commit()

def update(id):
    nome = alterar_dados_sala_cafe.lineEditNome.text()
    capacidade = alterar_dados_sala_cafe.spinBoxCapacidade.text()

    cursor = db.cursor()
    sql = "UPDATE cafes SET nome = %s, capacidade = %s WHERE idCafe = %s"
    data = (str(nome), str(capacidade), str(id))
    cursor.execute(sql, data)
    db.commit()

    alterar_dados_sala_cafe.close()

def editar_sala_cafe():
    line = lista_salas_cafe.tableWidget.currentRow()

    cursor = db.cursor()
    cursor.execute("SELECT idCafe FROM cafes")
    rdata = cursor.fetchall()
    id = rdata[line][0]
    
    cursor.execute("SELECT nome, capacidade FROM cafes WHERE idCafe =" + str(id))
    sala_cafe = cursor.fetchall()

    alterar_dados_sala_cafe.show()

    alterar_dados_sala_cafe.lblNome_disabled.setText(str(sala_cafe[0][0]))
    alterar_dados_sala_cafe.lblCapacidade_disabled.setText(str(sala_cafe[0][1]))

    alterar_dados_sala_cafe.btnSalvarAlteracao.clicked.connect(partial(update, id))

def call_lista_pessoas_sala(id):
    lista_pessoas.show()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM pessoas p INNER JOIN cafes c ON p.idCafe = c.idCafe WHERE c.idCafe = " + str(id))
    rdata = cursor.fetchall()

    lista_pessoas.tableWidget.setRowCount(len(rdata))
    lista_pessoas.tableWidget.setColumnCount(5)

    for i in range(0, len(rdata)):
        for j in range(0, 5):
            lista_pessoas.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))

def call_sala_cafe_detalhada():
    line = lista_salas_cafe.tableWidget.currentRow()
    cursor = db.cursor()

    cursor.execute("SELECT idCafe FROM cafes")
    rdata = cursor.fetchall()
    id = rdata[line][0]

    cursor.execute("SELECT nome, capacidade FROM cafes WHERE idCafe =" + str(id))
    sala_d = cursor.fetchall()

    cursor.execute("SELECT p.idPessoa FROM pessoas p INNER JOIN cafes c ON p.idCafe = c.idCafe WHERE c.idCafe = " + str(id))
    pessoas = cursor.fetchall()

    sala_detalhada_cafe.show()
    sala_detalhada_cafe.lblNome.setText(str(sala_d[0][0]))
    sala_detalhada_cafe.lblCapacidade.setText(str(sala_d[0][1]))
    sala_detalhada_cafe.lblPessoasQtd.setText(str(len(pessoas)))
    sala_detalhada_cafe.btnVerPessoas.clicked.connect(partial(call_lista_pessoas_sala, id)) 


app = QtWidgets.QApplication([])


# CARREGA SCREENS
cadastro_salas_cafe = uic.loadUi("sistema/screens/cadastroSalasCafe.ui")
lista_salas_cafe = uic.loadUi("sistema/screens/listaSalasCafe.ui")
alterar_dados_sala_cafe = uic.loadUi("sistema/screens/alterarDadosSalaCafe.ui")
sala_detalhada_cafe = uic.loadUi("sistema/screens/salaCafeDetalhada.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")

# EVENT LISTENER
cadastro_salas_cafe.btnCadastrar.clicked.connect(cadastrar_sala_cafe)
lista_salas_cafe.btnDeletar.clicked.connect(deletar_sala_cafe)
lista_salas_cafe.btnEditar.clicked.connect(editar_sala_cafe)
lista_salas_cafe.btnDetalhes.clicked.connect(call_sala_cafe_detalhada)