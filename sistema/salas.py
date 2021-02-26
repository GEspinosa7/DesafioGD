from PyQt5 import uic
from functools import partial
from functions import cadastrar_sala, deletar_sala, editar_sala,  detalhar_sala

def call_cadastro_sala():
    cadastro_salas.show()


# CARREGA SCREENS
cadastro_salas = uic.loadUi("sistema/screens/cadastroSalas.ui")
lista_salas = uic.loadUi("sistema/screens/listaSalas.ui")
alterar_dados_sala = uic.loadUi("sistema/screens/alterarDadosSala.ui")
sala_detalhada = uic.loadUi("sistema/screens/salaDetalhada.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")
alerta_padrao = uic.loadUi("sistema/screens/alertaPadrao.ui")


# EVENT LISTENER
cadastro_salas.btnCadastrar.clicked.connect(
    partial(cadastrar_sala, cadastro_salas, "salas")
)

lista_salas.btnDeletar.clicked.connect(
    partial(deletar_sala, lista_salas, "salas", "idSala", sala_detalhada)
)

lista_salas.btnEditar.clicked.connect(
    partial(editar_sala, lista_salas, "salas", "idSala", alterar_dados_sala)
)

lista_salas.btnDetalhes.clicked.connect(
    partial(detalhar_sala, lista_salas, "idSala", "salas", sala_detalhada)
)
