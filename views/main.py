# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu2.0.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from views.img import testando_rc
from views import cliente as cli #tela de cliente
from views import fornecedor as forn # tela de Fornecedor
from views import produto as prod
from views import OpEscolha as opcao
from views import consultacliente as consulcli
from views import consultafornecedor as consulforn
from views import consultaproduto as consulprod
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1556, 659)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QMainWindow {\n"
"background-image: url(:/logo.png);\n"
"background-repeat: no-repeat;\n"
"background-attachment: fixed;\n"
"background-position: bottom center;\n"
"}\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCadastro = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastro.setGeometry(QtCore.QRect(20, 110, 111, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCadastro.sizePolicy().hasHeightForWidth())
        self.btnCadastro.setSizePolicy(sizePolicy)
        self.btnCadastro.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnCadastro.setFont(font)
        self.btnCadastro.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnCadastro.setStyleSheet("QPushButton\n"
"{ \n"
"   background-image: url(:/icon.png);\n"
"   font: bold 14pt \"Verdana\";\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton#quit_button\n"
"{\n"
"   background-image: url(:/icon.png);\n"
"  font: bold 14pt \"Verdana\";\n"
"  color: white;\n"
"} \n"
"QPushButton:hover\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"\n"
"} \n"
"QPushButton:hover#quit_button\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"   \n"
"}")
        self.btnCadastro.setObjectName("btnCadastro")
        self.btnConsulta = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsulta.setGeometry(QtCore.QRect(150, 110, 111, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConsulta.sizePolicy().hasHeightForWidth())
        self.btnConsulta.setSizePolicy(sizePolicy)
        self.btnConsulta.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnConsulta.setFont(font)
        self.btnConsulta.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnConsulta.setStyleSheet("QPushButton\n"
"{ \n"
"   background-image: url(:/icon.png);\n"
"   font: bold 14pt \"Verdana\";\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton#quit_button\n"
"{\n"
"   background-image: url(:/icon.png);\n"
"  font: bold 14pt \"Verdana\";\n"
"  color: white;\n"
"} \n"
"QPushButton:hover\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"\n"
"} \n"
"QPushButton:hover#quit_button\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"   \n"
"}")
        self.btnConsulta.setObjectName("btnConsulta")
        self.btnRelatorios = QtWidgets.QPushButton(self.centralwidget)
        self.btnRelatorios.setGeometry(QtCore.QRect(480, 110, 131, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRelatorios.sizePolicy().hasHeightForWidth())
        self.btnRelatorios.setSizePolicy(sizePolicy)
        self.btnRelatorios.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnRelatorios.setFont(font)
        self.btnRelatorios.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnRelatorios.setStyleSheet("QPushButton\n"
"{ \n"
"   background-image: url(:/icon.png);\n"
"   font: bold 14pt \"Verdana\";\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton#quit_button\n"
"{\n"
"   background-image: url(:/icon.png);\n"
"  font: bold 14pt \"Verdana\";\n"
"  color: white;\n"
"} \n"
"QPushButton:hover\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"\n"
"} \n"
"QPushButton:hover#quit_button\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"   \n"
"}")
        self.btnRelatorios.setObjectName("btnRelatorios")
        self.btnMovimentacoes = QtWidgets.QPushButton(self.centralwidget)
        self.btnMovimentacoes.setGeometry(QtCore.QRect(280, 110, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMovimentacoes.sizePolicy().hasHeightForWidth())
        self.btnMovimentacoes.setSizePolicy(sizePolicy)
        self.btnMovimentacoes.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnMovimentacoes.setFont(font)
        self.btnMovimentacoes.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnMovimentacoes.setStyleSheet("QPushButton\n"
"{ \n"
"   background-image: url(:/icon.png);\n"
"   font: bold 14pt \"Verdana\";\n"
"   color: white;\n"
"}\n"
"\n"
"QPushButton#quit_button\n"
"{\n"
"   background-image: url(:/icon.png);\n"
"  font: bold 14pt \"Verdana\";\n"
"  color: white;\n"
"} \n"
"QPushButton:hover\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"\n"
"} \n"
"QPushButton:hover#quit_button\n"
"{\n"
"    background-image: url(:/ico.png);\n"
"    font: bold 14pt \"Verdana\";\n"
"   \n"
"}")
        self.btnMovimentacoes.setObjectName("btnMovimentacoes")
        self.btnCalculadora = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalculadora.setGeometry(QtCore.QRect(630, 110, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalculadora.sizePolicy().hasHeightForWidth())
        self.btnCalculadora.setSizePolicy(sizePolicy)
        self.btnCalculadora.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnCalculadora.setFont(font)
        self.btnCalculadora.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnCalculadora.setStyleSheet("QPushButton\n"
"{ \n"
"background-image: url(:/calc2.png);\n"
"background-position: center;\n"
"font: bold 14pt \"Verdana\";\n"
"color: transparent;\n"
"}\n"
"\n"
"QPushButton#quit_button\n"
"{\n"
"background-image: url(:/calc2.png);\n"
"background-position: center;\n"
"font: bold 14pt \"Verdana\";\n"
"color: transparent;\n"
"} \n"
"QPushButton:hover\n"
"{\n"
"background-image: url(:/ico.png);\n"
"font: bold 14pt \"Verdana\";\n"
"color: white;\n"
"\n"
"} \n"
"QPushButton:hover#quit_button\n"
"{\n"
"background-image: url(:/ico.png);\n"
"font: bold 14pt \"Verdana\";\n"
"color: white;\n"
"}\n"
"")
        self.btnCalculadora.setAutoDefault(False)
        self.btnCalculadora.setDefault(False)
        self.btnCalculadora.setFlat(False)
        self.btnCalculadora.setObjectName("btnCalculadora")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1556, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menuCadastro = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuCadastro.setFont(font)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuConsulta = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuConsulta.setFont(font)
        self.menuConsulta.setObjectName("menuConsulta")
        self.menuMovimentacoes = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuMovimentacoes.setFont(font)
        self.menuMovimentacoes.setObjectName("menuMovimentacoes")
        self.menuAjuda = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuAjuda.setFont(font)
        self.menuAjuda.setObjectName("menuAjuda")
        self.menuRelatorios = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuRelatorios.setFont(font)
        self.menuRelatorios.setObjectName("menuRelatorios")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mCadastroCliente = QtWidgets.QAction(MainWindow)
        self.mCadastroCliente.setObjectName("mCadastroCliente")
        self.mCadastroFornecedor = QtWidgets.QAction(MainWindow)
        self.mCadastroFornecedor.setObjectName("mCadastroFornecedor")
        self.mCadastroProduto = QtWidgets.QAction(MainWindow)
        self.mCadastroProduto.setObjectName("mCadastroProduto")
        self.mConsultaCliente = QtWidgets.QAction(MainWindow)
        self.mConsultaCliente.setObjectName("mConsultaCliente")
        self.mConsultaFornecedor = QtWidgets.QAction(MainWindow)
        self.mConsultaFornecedor.setObjectName("MConsultaFornecedor")
        self.mConsultaProduto = QtWidgets.QAction(MainWindow)
        self.mConsultaProduto.setObjectName("mConsultaProduto")
        self.mMovimentacoesEntrada = QtWidgets.QAction(MainWindow)
        self.mMovimentacoesEntrada.setObjectName("mMovimentacoesEntrada")
        self.mMovimentacoesSaida = QtWidgets.QAction(MainWindow)
        self.mMovimentacoesSaida.setObjectName("mMovimentacoesSaida")
        self.mAjudaAjuda = QtWidgets.QAction(MainWindow)
        self.mAjudaAjuda.setObjectName("mAjudaAjuda")
        self.mAjudaSobre = QtWidgets.QAction(MainWindow)
        self.mAjudaSobre.setObjectName("mAjudaSobre")
        self.mRelatoriosCompras = QtWidgets.QAction(MainWindow)
        self.mRelatoriosCompras.setObjectName("mRelatoriosCompras")
        self.mRelatoriosVendas = QtWidgets.QAction(MainWindow)
        self.mRelatoriosVendas.setObjectName("mRelatoriosVendas")
        self.mRelatoriosFornecedores = QtWidgets.QAction(MainWindow)
        self.mRelatoriosFornecedores.setObjectName("mRelatoriosFornecedores")
        self.mRelatoriosClientes = QtWidgets.QAction(MainWindow)
        self.mRelatoriosClientes.setObjectName("mRelatoriosClientes")
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.mCadastroCliente)
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.mCadastroFornecedor)
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.mCadastroProduto)
        self.menuCadastro.addSeparator()
        self.menuConsulta.addSeparator()
        self.menuConsulta.addAction(self.mConsultaCliente)
        self.menuConsulta.addSeparator()
        self.menuConsulta.addAction(self.mConsultaFornecedor)
        self.menuConsulta.addSeparator()
        self.menuConsulta.addAction(self.mConsultaProduto)
        self.menuConsulta.addSeparator()
        self.menuMovimentacoes.addSeparator()
        self.menuMovimentacoes.addAction(self.mMovimentacoesEntrada)
        self.menuMovimentacoes.addSeparator()
        self.menuMovimentacoes.addAction(self.mMovimentacoesSaida)
        self.menuMovimentacoes.addSeparator()
        self.menuAjuda.addSeparator()
        self.menuAjuda.addAction(self.mAjudaAjuda)
        self.menuAjuda.addSeparator()
        self.menuAjuda.addAction(self.mAjudaSobre)
        self.menuAjuda.addSeparator()
        self.menuRelatorios.addSeparator()
        self.menuRelatorios.addAction(self.mRelatoriosCompras)
        self.menuRelatorios.addSeparator()
        self.menuRelatorios.addAction(self.mRelatoriosVendas)
        self.menuRelatorios.addSeparator()
        self.menuRelatorios.addAction(self.mRelatoriosFornecedores)
        self.menuRelatorios.addSeparator()
        self.menuRelatorios.addAction(self.mRelatoriosClientes)
        self.menuRelatorios.addSeparator()
        self.menuBar.addAction(self.menuCadastro.menuAction())
        self.menuBar.addAction(self.menuConsulta.menuAction())
        self.menuBar.addAction(self.menuMovimentacoes.menuAction())
        self.menuBar.addAction(self.menuRelatorios.menuAction())
        self.menuBar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Açoes de botões

        self.mCadastroCliente.triggered.connect(self.openCliente)

        self.mCadastroFornecedor.triggered.connect(self.openForn)

        self.mCadastroProduto.triggered.connect(self.openProd)

        self.btnCadastro.clicked.connect(self.OpEscolha)

        self.mConsultaCliente.triggered.connect(self.searchcliente)

        self.mConsultaProduto.triggered.connect(self.searchproduto)

        self.mConsultaFornecedor.triggered.connect(self.searchfornecedor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Programa Estoque"))
        self.btnCadastro.setText(_translate("MainWindow", "Cadastro"))
        self.btnConsulta.setText(_translate("MainWindow", "Consulta"))
        self.btnRelatorios.setText(_translate("MainWindow", "Relatórios"))
        self.btnMovimentacoes.setText(_translate("MainWindow", "Movimentações"))
        self.btnCalculadora.setText(_translate("MainWindow", "F5"))
        self.menuCadastro.setTitle(_translate("MainWindow", "C&adastro"))
        self.menuConsulta.setTitle(_translate("MainWindow", "C&onsulta"))
        self.menuMovimentacoes.setTitle(_translate("MainWindow", "Movi&mentações"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Aju&da"))
        self.menuRelatorios.setTitle(_translate("MainWindow", "R&elatórios"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.mCadastroCliente.setText(_translate("MainWindow", "Cliente"))
        self.mCadastroFornecedor.setText(_translate("MainWindow", "Fornecedor"))
        self.mCadastroProduto.setText(_translate("MainWindow", "Produto"))
        self.mConsultaCliente.setText(_translate("MainWindow", "Cliente"))
        self.mConsultaFornecedor.setText(_translate("MainWindow", "Fornecedor"))
        self.mConsultaProduto.setText(_translate("MainWindow", "Produto"))
        self.mMovimentacoesEntrada.setText(_translate("MainWindow", "Entrada"))
        self.mMovimentacoesSaida.setText(_translate("MainWindow", "Saída"))
        self.mAjudaAjuda.setText(_translate("MainWindow", "Ajuda"))
        self.mAjudaSobre.setText(_translate("MainWindow", "Sobre"))
        self.mRelatoriosCompras.setText(_translate("MainWindow", "Compras"))
        self.mRelatoriosVendas.setText(_translate("MainWindow", "Vendas"))
        self.mRelatoriosFornecedores.setText(_translate("MainWindow", "Fornecedores"))
        self.mRelatoriosClientes.setText(_translate("MainWindow", "Clientes"))

    # Função para abrir tela de cadastro
    def openCliente(self):
            self.window = QDialog()
            self.window.setStyleSheet("QWidget { background-color : white;}")
            Wcliente = cli.Ui_Dialog()
            Wcliente.setupUi(self.window)
            self.window.show()
            self.window.exec_()

    def openForn(self):
            self.window = QDialog()
            WFonecedor = forn.Ui_Dialog()
            WFonecedor.setupUi(self.window)
            self.window.show()
            self.window.exec_()

    def openProd(self):
        self.window = QDialog()
        WProduto = prod.Ui_Produto()
        WProduto.setupUi(self.window)
        self.window.show()
        self.window.exec_()

    def OpEscolha(self):
        escolha = QDialog()
        op = opcao.Ui_OpCadastro()
        op.setupUi(escolha,"Cadastro")
        escolha.show()
        escolha.exec_()


    #Funções para abrir Telas de Consulta


    def searchcliente(self):
        self.window = QDialog()
        WconsultaCli = consulcli.Ui_Dialog()
        WconsultaCli.setupUi(self.window)
        self.window.show()
        self.window.exec_()

    def searchproduto(self):
        self.window = QDialog()
        WconsulProd = consulprod.Ui_Dialog()
        WconsulProd.setupUi(self.window)
        self.window.show()
        self.window.exec_()
    def searchfornecedor(self):
        self.window = QDialog()
        WconsulForn = consulforn.Ui_Dialog()
        WconsulForn.setupUi(self.window)
        self.window.show()
        self.window.exec_()