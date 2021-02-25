from PyQt5 import uic,QtWidgets
import mysql.connector
from functools import partial
# from functions import tratamento_sala

#BANCO DE DADOS
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CHL8xXHp5AfZC8AV",
    database="desafio"
)


def cadastrar_sala():
    nome = cadastro_salas.lineEditNome.text()
    capacidade = cadastro_salas.spinBoxCapacidade.text()

    # tratamento_sala(nome, capacidade, cadastro_salas, "salas")

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
    nome = alterar_dados_sala.lineEditNome.text()
    capacidade = alterar_dados_sala.spinBoxCapacidade.text()

    cursor = db.cursor()
    sql = "UPDATE salas SET nome = %s, capacidade = %s WHERE idSala = %s"
    data = (str(nome), str(capacidade), str(id))
    cursor.execute(sql, data)
    db.commit()

    alterar_dados_sala.close()

def editar_sala():
    line = lista_salas.tableWidget.currentRow()

    cursor = db.cursor()
    cursor.execute("SELECT idSala FROM salas")
    rdata = cursor.fetchall()
    id = rdata[line][0]

    cursor.execute("SELECT nome, capacidade FROM salas WHERE idSala =" + str(id))
    sala = cursor.fetchall()

    alterar_dados_sala.show()
    alterar_dados_sala.lblNome_disabled.setText(str(sala[0][0]))
    alterar_dados_sala.lblCapacidade_disabled.setText(str(sala[0][1]))
    alterar_dados_sala.btnSalvarAlteracao.clicked.connect(partial(update, id))


def call_lista_pessoas_sala(id):
    lista_pessoas.show()

    cursor = db.cursor()
    cursor.execute("SELECT *  FROM pessoas p INNER JOIN salas s ON p.idSala = s.idSala WHERE s.idSala = " + str(id))
    rdata = cursor.fetchall()

    lista_pessoas.tableWidget.setRowCount(len(rdata))
    lista_pessoas.tableWidget.setColumnCount(5)

    for i in range(0, len(rdata)):
        for j in range(0, 5):
            lista_pessoas.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))

def call_sala_detalhada():
    line = lista_salas.tableWidget.currentRow()
    cursor = db.cursor()

    cursor.execute("SELECT idSala FROM salas")
    rdata = cursor.fetchall()
    id = rdata[line][0]

    cursor.execute("SELECT nome, capacidade FROM salas WHERE idSala =" + str(id))
    sala_d = cursor.fetchall()

    cursor.execute("SELECT p.idPessoa FROM pessoas p INNER JOIN salas s ON p.idSala = s.idSala WHERE s.idSala = " + str(id))
    pessoas = cursor.fetchall()

    sala_detalhada.show()
    sala_detalhada.lblNome.setText(str(sala_d[0][0]))
    sala_detalhada.lblCapacidade.setText(str(sala_d[0][1]))
    sala_detalhada.lblPessoasQtd.setText(str(len(pessoas)))
    sala_detalhada.btnVerPessoas.clicked.connect(partial(call_lista_pessoas_sala, id))


app = QtWidgets.QApplication([])


# CARREGA SCREENS
cadastro_salas = uic.loadUi("sistema/screens/cadastroSalas.ui")
lista_salas = uic.loadUi("sistema/screens/listaSalas.ui")
alterar_dados_sala = uic.loadUi("sistema/screens/alterarDadosSala.ui")
sala_detalhada = uic.loadUi("sistema/screens/salaDetalhada.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")


# EVENT LISTENER
cadastro_salas.btnCadastrar.clicked.connect(cadastrar_sala)
lista_salas.btnDeletar.clicked.connect(deletar_sala)
lista_salas.btnEditar.clicked.connect(editar_sala)
lista_salas.btnDetalhes.clicked.connect(call_sala_detalhada)
