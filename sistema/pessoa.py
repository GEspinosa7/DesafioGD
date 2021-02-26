from PyQt5 import uic,QtWidgets
from db import db
from functools import partial
from functions import call_alerta_padrao, call_alerta_sucesso

def cadastrar_pessoa():

    nome = cadastro_pessoas.lineEditNome.text()
    sobrenome = cadastro_pessoas.lineEditSobrenome.text()
    line_sala = cadastro_pessoas.tableWidget_sala.currentRow()
    line_sala_cafe = cadastro_pessoas.tableWidget_cafe.currentRow()

    erro_nome = "A pessoa está sem nome!"
    erro_sobrenome = "A pessoa está sem sobrenome!"
    erro_ambos = "A pessoa está sem nome e sobrenome"

    cursor = db.cursor()
    
    cursor.execute("SELECT idSala, capacidade FROM salas")
    s_data = cursor.fetchall()

    id_sala = s_data[line_sala][0]
    capacidade_sala = s_data[line_sala][1]

    cursor.execute("SELECT idPessoa  FROM pessoas p INNER JOIN salas s ON p.idSala = s.idSala WHERE s.idSala = " + str(id_sala))
    s_sala_qtd = cursor.fetchall()
    qtd_sala = len(s_sala_qtd)

    cursor.execute("SELECT idCafe, capacidade FROM cafes")
    sc_data = cursor.fetchall()

    id_cafe = sc_data[line_sala_cafe][0]
    capacidade_cafe = sc_data[line_sala_cafe][1]

    cursor.execute("SELECT * FROM pessoas p INNER JOIN cafes c ON p.idCafe = c.idCafe WHERE c.idCafe = " + str(id_cafe))
    rdata = cursor.fetchall()
    qtd_cafe = len(rdata)

    if (qtd_sala >= capacidade_sala):
       call_alerta_padrao("Sala com limite de pessoas atingido")
    elif (qtd_cafe >= capacidade_cafe):
        call_alerta_padrao("Sala de Café com limite de pessoas atingido")
    elif ((not nome.strip()) and (not sobrenome.strip())):
        call_alerta_padrao(erro_ambos)
    elif ((not nome.strip()) and (sobrenome.strip())):
        call_alerta_padrao(erro_nome)
    elif ((nome.strip()) and (not sobrenome.strip())):
        call_alerta_padrao(erro_sobrenome)
    else:
        call_alerta_sucesso(nome + " " + sobrenome + " cadastrado com sucesso!")

        sql = "INSERT INTO pessoas (nome, sobrenome, idSala, idCafe) VALUES (%s, %s, %s, %s)"
        data = (str(nome), str(sobrenome), str(id_sala), 2)
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

    if len(rdata) == 0:
        lista_pessoas.btnEditar.setHidden(True)
        lista_pessoas.btnDeletar.setHidden(True)
    else:
        lista_pessoas.btnEditar.setHidden(False)
        lista_pessoas.btnDeletar.setHidden(False)

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

    if len(rdata) == 0:
        call_alerta_padrao("Você deletou a última pessoa cadastrada")
    else:
        id_pessoa = rdata[line][0]
        cursor.execute("DELETE FROM pessoas WHERE idPessoa=" + str(id_pessoa))
        db.commit()
        call_alerta_sucesso("Pessoa removida com sucesso")
        lista_pessoas.tableWidget.removeRow(line)
        

def update(id_salvo):
    nome = alterar_dados_pessoa.lineEditNome.text()
    sobrenome = alterar_dados_pessoa.lineEditSobrenome.text()

    #AUALIZANDO OS DADOS NO BANCO DE DADOS
    cursor = db.cursor()
    sql = "UPDATE pessoas SET nome = %s, sobrenome = %s WHERE idPessoa = %s"
    data = (str(nome), str(sobrenome), str(id_salvo))
    cursor.execute(sql, data)
    db.commit()
    alterar_dados_pessoa.close()
    call_alerta_sucesso("Dados editados com sucesso")

def editar_pessoa():
    line = lista_pessoas.tableWidget.currentRow()
    
    cursor = db.cursor()
    cursor.execute("SELECT idPessoa FROM pessoas")
    rdata = cursor.fetchall()

    if len(rdata) == 0:
        call_alerta_padrao("Não existe nenhuma pessoa para editar")
    else:
        id_salvo = rdata[line][0]

        cursor.execute("SELECT nome, sobrenome FROM pessoas WHERE idPessoa=" + str(id_salvo))
        pessoa = cursor.fetchall()

        alterar_dados_pessoa.show()

        alerta_campos = "Verifique todos os dados antes de confirmar a edição, repita os valores dos dados que você não queira mudar"
        call_alerta_padrao(alerta_campos)

        alterar_dados_pessoa.lblNome_disabled.setText(str(pessoa[0][0]))
        alterar_dados_pessoa.lblSobrenome_disabled.setText(str(pessoa[0][1]))

        alterar_dados_pessoa.btnSalvarAlteracao.clicked.connect(partial(update, id_salvo))



# CARREGA SCREENS
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")
alterar_dados_pessoa = uic.loadUi("sistema/screens/alterarDadosPessoa.ui")
# alerta_sala_cheia = uic.loadUi("sistema/screens/alertaSalaCheia.ui")
alerta_padrao = uic.loadUi("sistema/screens/alertaPadrao.ui")

# EVENT LISTENER
cadastro_pessoas.btnCadastrar.clicked.connect(cadastrar_pessoa)
lista_pessoas.btnDeletar.clicked.connect(deletar_pessoa)
lista_pessoas.btnEditar.clicked.connect(editar_pessoa)
# alerta_sala_cheia.btnOk.clicked.connect(partial(close, alerta_sala_cheia))
