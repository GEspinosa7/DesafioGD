from functools import partial
from PyQt5 import uic,QtWidgets
from functions import cadastrar_sala, deletar_sala, editar_sala,  sala_detalhada

def call_cadastro_cafe():
    cadastro_salas_cafe.show()

app = QtWidgets.QApplication([])

# CARREGA SCREENS
cadastro_salas_cafe = uic.loadUi("sistema/screens/cadastroSalasCafe.ui")
lista_salas_cafe = uic.loadUi("sistema/screens/listaSalasCafe.ui")
alterar_dados_sala_cafe = uic.loadUi("sistema/screens/alterarDadosSalaCafe.ui")
sala_detalhada_cafe = uic.loadUi("sistema/screens/salaCafeDetalhada.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")
alerta_padrao = uic.loadUi("sistema/screens/alertaPadrao.ui")

# EVENT LISTENER

cadastro_salas_cafe.btnCadastrar.clicked.connect(
    partial(cadastrar_sala, cadastro_salas_cafe, "cafes")
)

lista_salas_cafe.btnDeletar.clicked.connect(
    partial(deletar_sala, lista_salas_cafe, "cafes", "idCafe", sala_detalhada_cafe)
)
lista_salas_cafe.btnEditar.clicked.connect(
    partial(editar_sala, lista_salas_cafe, "cafes", "idCafe", alterar_dados_sala_cafe)
)
lista_salas_cafe.btnDetalhes.clicked.connect(
    partial(sala_detalhada, lista_salas_cafe, "idCafe", "cafes", sala_detalhada_cafe)
)
