from PyQt5 import uic, QtWidgets
import mysql.connector
from functools import partial

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CHL8xXHp5AfZC8AV",
    database="desafio"
)

alerta_cadastro = uic.loadUi("sistema/screens/alertaCadastro.ui")

def close(ui):
    ui.close()

def call_alerta_cadastro(label):
    alerta_cadastro.show()
    alerta_cadastro.lblAlerta.setText(label)
    alerta_cadastro.btnOk.clicked.connect(partial(close, alerta_cadastro))

def tratamento_sala(nome, capacidade, ui, tabela):
    erro_nome = "A sala precisa de um nome!"
    erro_capacidade = "A sala precisa de um mínimo de capacidade de pessoas"
    erro_ambos = "A sala está sem nome e sem uma capacidade mínima definidas"

    if ((not nome.strip()) and (int(capacidade) == 0)):
        call_alerta_cadastro(erro_ambos)
    elif ((not nome.strip()) and (int(capacidade) > 0)):
        call_alerta_cadastro(erro_nome)
    elif int(capacidade) == 0:
        call_alerta_cadastro(erro_capacidade)
    else:  
        cursor = db.cursor()
        sql = "INSERT INTO " + tabela + " (nome, capacidade) VALUES (%s,%s)"
        data = (str(nome), str(capacidade))
        cursor.execute(sql,data)
        db.commit()
        ui.close()

def deletar_sala(ui, tabela, id_tabela):
    line = ui.tableWidget.currentRow()
    ui.tableWidget.removeRow(line)

    cursor = db.cursor()
    cursor.execute("SELECT " + id_tabela +" FROM " + tabela)
    rdata = cursor.fetchall()
    id_salvo = rdata[line][0]

    cursor.execute("DELETE FROM " + tabela + " WHERE " + id_tabela + " = " + str(id_salvo))
    db.commit()

def update(id_salvo, ui_alterar, tabela, id_tabela):
    nome = ui_alterar.lineEditNome.text()
    capacidade = ui_alterar.spinBoxCapacidade.text()

    cursor = db.cursor()
    sql = "UPDATE "+ tabela +" SET nome = %s, capacidade = %s WHERE "+ id_tabela +" = %s"
    data = (str(nome), str(capacidade), str(id_salvo))
    cursor.execute(sql, data)
    db.commit()

    ui_alterar.close()

def editar_sala(ui, tabela, id_tabela, ui_alterar):
    line = ui.tableWidget.currentRow()

    cursor = db.cursor()
    cursor.execute("SELECT "+ id_tabela +" FROM "+ tabela)
    rdata = cursor.fetchall()
    id_salvo = rdata[line][0]
    
    cursor.execute("SELECT nome, capacidade FROM "+ tabela +" WHERE "+ id_tabela +" =" + str(id_salvo))
    sala = cursor.fetchall()

    ui_alterar.show()

    ui_alterar.lblNome_disabled.setText(str(sala[0][0]))
    ui_alterar.lblCapacidade_disabled.setText(str(sala[0][1]))

    ui_alterar.btnSalvarAlteracao.clicked.connect(partial(update, id_salvo, ui_alterar, tabela, id_tabela))

def call_lista_pessoas_sala(id_salvo, tabela, id_tabela):
    lista_pessoas.show()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM pessoas p INNER JOIN "+ tabela +" c ON p."+ id_tabela +" = c."+ id_tabela +" WHERE c."+ id_tabela +" = " + str(id_salvo))
    rdata = cursor.fetchall()

    lista_pessoas.tableWidget.setRowCount(len(rdata))
    lista_pessoas.tableWidget.setColumnCount(5)

    for i in range(0, len(rdata)):
        for j in range(0, 5):
            lista_pessoas.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))

def sala_detalhada(ui, id_tabela, tabela, ui_detalhada):
    line = ui.tableWidget.currentRow()
    cursor = db.cursor()

    cursor.execute("SELECT "+ id_tabela +" FROM "+ tabela)
    rdata = cursor.fetchall()
    id_salvo = rdata[line][0]

    cursor.execute("SELECT nome, capacidade FROM "+ tabela +" WHERE "+ id_tabela +" = " + str(id_salvo))
    sala_d = cursor.fetchall()

    cursor.execute("SELECT p.idPessoa FROM pessoas p INNER JOIN "+ tabela +" c ON p."+ id_tabela +" = c."+ id_tabela +" WHERE c."+ id_tabela +" = " + str(id_salvo))
    pessoas = cursor.fetchall()

    ui_detalhada.show()
    ui_detalhada.lblNome.setText(str(sala_d[0][0]))
    ui_detalhada.lblCapacidade.setText(str(sala_d[0][1]))
    ui_detalhada.lblPessoasQtd.setText(str(len(pessoas)))
    ui_detalhada.btnVerPessoas.clicked.connect(partial(call_lista_pessoas_sala, id_salvo, tabela, id_tabela))

def call_listas(ui, tabela, id_tabela, ui_detalhada, ui_alterar):
    ui.show()

    cursor = db.cursor()
    sql = "SELECT * FROM " + tabela
    cursor.execute(sql)
    rdata = cursor.fetchall()

    ui.tableWidget.setRowCount(len(rdata))
    ui.tableWidget.setColumnCount(3)

    for i in range(0, len(rdata)):
        for j in range(0, 3):
            ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rdata[i][j])))

    ui.btnDeletar.clicked.connect(partial(deletar_sala, ui, tabela, id_tabela))
    ui.btnEditar.clicked.connect(partial(editar_sala, ui, tabela, id_tabela, ui_alterar))
    ui.btnDetalhes.clicked.connect(partial(sala_detalhada, ui, id_tabela, tabela, ui_detalhada))

lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")