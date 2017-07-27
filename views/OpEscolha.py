# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpEscolha.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QDialog
from views import cliente as cli
from views import fornecedor  as forn
from views import produto as prod

class Ui_OpCadastro(object):
    def setupUi(self, OpCadastro,operacao):
        self.op = operacao
        OpCadastro.setObjectName("OpCadastro")
        OpCadastro.resize(362, 226)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpCadastro)
        self.buttonBox.setGeometry(QtCore.QRect(0, 180, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(OpCadastro)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 281, 161))
        self.groupBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox.setObjectName("groupBox")
        self.radioCliente = QtWidgets.QRadioButton(self.groupBox)
        self.radioCliente.setGeometry(QtCore.QRect(30, 40, 101, 22))
        self.radioCliente.setChecked(True)
        self.radioCliente.setObjectName("radioPessoaF")
        self.radioFronecedor = QtWidgets.QRadioButton(self.groupBox)
        self.radioFronecedor.setGeometry(QtCore.QRect(30, 80, 131, 22))
        self.radioFronecedor.setObjectName("radioPessoaJ")
        self.radioProduto = QtWidgets.QRadioButton(self.groupBox)
        self.radioProduto.setGeometry(QtCore.QRect(30, 120, 101, 22))
        self.radioProduto.setObjectName("radioProduto")

        self.retranslateUi(OpCadastro)
        self.buttonBox.accepted.connect(OpCadastro.accept)
        self.buttonBox.rejected.connect(OpCadastro.reject)
        QtCore.QMetaObject.connectSlotsByName(OpCadastro)
        self.buttonBox.accepted.connect(self.Operacao)


    def retranslateUi(self, OpCadastro):
        _translate = QtCore.QCoreApplication.translate
        OpCadastro.setWindowTitle(_translate("OpCadastro", self.op))
        self.groupBox.setTitle(_translate("OpCadastro", "Opção"))
        self.radioCliente.setText(_translate("OpCadastro", "Cliente"))
        self.radioFronecedor.setText(_translate("OpCadastro", "Fornecedor"))
        self.radioProduto.setText(_translate("OpCadastro", "Produto"))

    def Operacao(self):
        if self.radioCliente.isChecked() == True:
            self.window = QDialog()
            Wcliente = cli.Ui_Dialog()
            Wcliente.setupUi(self.window)
            self.window.show()
            self.window.exec_()
        elif self.radioFronecedor.isChecked() == True:
            self.window = QDialog()
            Wfornecedor = forn.Ui_Dialog()
            Wfornecedor.setupUi(self.window)
            self.window.show()
            self.window.exec_()

        else:
            self.window = QDialog()
            WProduto = prod.Ui_Produto()
            WProduto.setupUi(self.window)
            self.window.show()
            self.window.exec_()





