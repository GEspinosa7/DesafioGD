from PyQt5 import uic,QtWidgets
app = QtWidgets.QApplication([])

from pessoa import  call_cadastro_pessoa, call_lista_pessoas
from salas import  call_cadastro_sala
from salas_cafe import call_cadastro_cafe
from functions import call_listas
from functools import partial
import images



# CARREGA SCREENS
mainScreen = uic.loadUi("sistema/screens/main.ui")

## PESSOAS
cadastro_pessoas = uic.loadUi("sistema/screens/cadastroPessoas.ui")
lista_pessoas = uic.loadUi("sistema/screens/listaPessoas.ui")

##SALAS
lista_salas = uic.loadUi("sistema/screens/listaSalas.ui")
sala_detalhada = uic.loadUi("sistema/screens/salaDetalhada.ui")
alterar_dados_sala = uic.loadUi("sistema/screens/alterarDadosSala.ui")

##SALAS DE CAFE
lista_salas_cafe = uic.loadUi("sistema/screens/listaSalasCafe.ui")
sala_detalhada_cafe = uic.loadUi("sistema/screens/salaCafeDetalhada.ui")
alterar_dados_sala_cafe = uic.loadUi("sistema/screens/alterarDadosSalaCafe.ui")

# EVENT LISTENERS

##PESSOAS
mainScreen.pessoasBtnCadastrar_3.clicked.connect(call_cadastro_pessoa)
mainScreen.pessoasBtnConsultar_3.clicked.connect(call_lista_pessoas)

##SALAS
mainScreen.salasBtnCadastrar_2.clicked.connect(call_cadastro_sala)
mainScreen.salasBtnConsultar_2.clicked.connect(
   partial(call_listas, lista_salas, "salas", "idSala", sala_detalhada, alterar_dados_sala)
)

##SALAS DE CAFE
mainScreen.salasCafeBtnCadastrar_2.clicked.connect(call_cadastro_cafe)

mainScreen.salasCafeBtnConsultar_2.clicked.connect(
   partial(
      call_listas, lista_salas_cafe, "cafes", "idCafe", sala_detalhada_cafe, alterar_dados_sala_cafe
   )
)


mainScreen.show()
app.exec()

#TODO: consertar erro sql de cadastrar pessoas