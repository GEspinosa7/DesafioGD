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
    numero = cadastro_salas_cafe.spinBoxNumero.text()
    capacidade = cadastro_salas_cafe.spinBoxCapacidade.text()
    

    #SALVANDO DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    sql = "INSERT INTO cafes (numero, capacidade) VALUES (%s,%s)"
    data = (str(numero), str(capacidade))
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
    numero = alterar_dados_sala_cafe.spinBoxNumero.text()
    capacidade = alterar_dados_sala_cafe.spinBoxCapacidade.text()

    #AUALIZANDO OS DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    sql = "UPDATE cafes SET numero = %s, capacidade = %s WHERE idCafe = %s"
    data = (str(numero), str(capacidade), str(id))
    cursor.execute(sql, data)
    db.commit()
    alterar_dados_sala_cafe.close()

def editar_sala_cafe():
    line = lista_salas_cafe.tableWidget.currentRow()
    cursor = db.cursor()
    cursor.execute("SELECT idCafe FROM cafes")
    rdata = cursor.fetchall()
    id = rdata[line][0]
    cursor.execute("SELECT numero, capacidade FROM cafes WHERE idCafe =" + str(id))
    sala_cafe = cursor.fetchall()

    alterar_dados_sala_cafe.show()

    alterar_dados_sala_cafe.lblNumero_disabled.setText(str(sala_cafe[0][0]))
    alterar_dados_sala_cafe.lblCapacidade_disabled.setText(str(sala_cafe[0][1]))

    alterar_dados_sala_cafe.btnSalvarAlteracao.clicked.connect(partial(update, id))


app = QtWidgets.QApplication([])


# CARREGA SCREENS
cadastro_salas_cafe = uic.loadUi("sistema/screens/cadastroSalasCafe.ui")
lista_salas_cafe = uic.loadUi("sistema/screens/listaSalasCafe.ui")
alterar_dados_sala_cafe = uic.loadUi("sistema/screens/alterarDadosSalaCafe.ui")

# EVENT LISTENER
cadastro_salas_cafe.btnCadastrar.clicked.connect(cadastrar_sala_cafe)
lista_salas_cafe.btnDeletar.clicked.connect(deletar_sala_cafe)
lista_salas_cafe.btnEditar.clicked.connect(editar_sala_cafe)
