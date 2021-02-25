from PyQt5 import uic,QtWidgets
from functools import partial
from functions import tratamento_sala, deletar_sala, editar_sala,  sala_detalhada

def cadastrar_sala_cafe():
    nome = cadastro_salas_cafe.lineEditNome.text()
    capacidade = cadastro_salas_cafe.spinBoxCapacidade.text()

    tratamento_sala(nome, capacidade, cadastro_salas_cafe, "cafes")

def call_cadastro_sala_cafe():
    cadastro_salas_cafe.show()

app = QtWidgets.QApplication([])

# CARREGA SCREENS
cadastro_salas_cafe = uic.loadUi("sistema/screens/cadastroSalasCafe.ui")
lista_salas_cafe = uic.loadUi("sistema/screens/listaSalasCafe.ui")
alterar_dados_sala_cafe = uic.loadUi("sistema/screens/alterarDadosSalaCafe.ui")
sala_detalhada_cafe = uic.loadUi("sistema/screens/salaCafeDetalhada.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")
alerta_cadastro = uic.loadUi("sistema/screens/alertaCadastro.ui")

# EVENT LISTENER
cadastro_salas_cafe.btnCadastrar.clicked.connect(cadastrar_sala_cafe)
lista_salas_cafe.btnDeletar.clicked.connect(
    partial(deletar_sala, lista_salas_cafe, "cafes", "idCafe", sala_detalhada_cafe)
)
lista_salas_cafe.btnEditar.clicked.connect(
    partial(editar_sala, lista_salas_cafe, "cafes", "idCafe", alterar_dados_sala_cafe)
)
lista_salas_cafe.btnDetalhes.clicked.connect(
    partial(sala_detalhada, lista_salas_cafe, "idCafe", "cafes", sala_detalhada_cafe)
)
