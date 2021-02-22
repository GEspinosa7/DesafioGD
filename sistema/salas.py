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

def cadastrar_sala():
    numero = cadastro_salas.spinBoxNumero.text()
    capacidade = cadastro_salas.spinBoxCapacidade.text()
    

    #SALVANDO DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    sql = "INSERT INTO salas (numero, capacidade) VALUES (%s,%s)"
    data = (str(numero), str(capacidade))
    cursor.execute(sql,data)
    db.commit()

    cadastro_salas.close()


def call_cadastro_sala():
    cadastro_salas.show()

def call_lista_salas():
    lista_salas.show()

    cursor = db.cursor()
    sql = "SELECT * FROM salas"
    cursor.execute(sql)
    rdata = cursor.fetchall()

    lista_salas.tableWidget.setRowCount(len(rdata))
    lista_salas.tableWidget.setColumnCount(3)

    for i in range(0, len(rdata)):
        for j in range(0, 3):
            lista_salas.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))


def deletar_sala():
    line = lista_salas.tableWidget.currentRow()
    lista_salas.tableWidget.removeRow(line)

    cursor = db.cursor()
    cursor.execute("SELECT idSala FROM salas")
    rdata = cursor.fetchall()
    id = rdata[line][0]
    cursor.execute("DELETE FROM salas WHERE idSala=" + str(id))
    db.commit()

def update(id):
    numero = alterar_dados_sala.spinBoxNumero.text()
    capacidade = alterar_dados_sala.spinBoxCapacidade.text()

    #AUALIZANDO OS DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    sql = "UPDATE salas SET numero = %s, capacidade = %s WHERE idSala = %s"
    data = (str(numero), str(capacidade), str(id))
    cursor.execute(sql, data)
    db.commit()
    alterar_dados_sala.close()

def editar_sala():
    line = lista_salas.tableWidget.currentRow()
    cursor = db.cursor()
    cursor.execute("SELECT idSala FROM salas")
    rdata = cursor.fetchall()
    id = rdata[line][0]
    cursor.execute("SELECT numero, capacidade FROM salas WHERE idSala =" + str(id))
    sala = cursor.fetchall()

    alterar_dados_sala.show()

    alterar_dados_sala.lblNumero_disabled.setText(str(sala[0][0]))
    alterar_dados_sala.lblCapacidade_disabled.setText(str(sala[0][1]))

    alterar_dados_sala.btnSalvarAlteracao.clicked.connect(partial(update, id))


app = QtWidgets.QApplication([])


# CARREGA SCREENS
cadastro_salas = uic.loadUi("sistema/screens/cadastroSalas.ui")
lista_salas = uic.loadUi("sistema/screens/listaSalas.ui")
alterar_dados_sala = uic.loadUi("sistema/screens/alterarDadosSala.ui")

# EVENT LISTENER
cadastro_salas.btnCadastrar.clicked.connect(cadastrar_sala)
lista_salas.btnDeletar.clicked.connect(deletar_sala)
lista_salas.btnEditar.clicked.connect(editar_sala)
