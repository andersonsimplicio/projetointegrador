# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaproduto.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(780, 500)
        Dialog.setMinimumSize(QtCore.QSize(780, 500))
        Dialog.setMaximumSize(QtCore.QSize(780, 500))
        self.btnPesquisar = QtWidgets.QPushButton(Dialog)
        self.btnPesquisar.setGeometry(QtCore.QRect(540, 70, 75, 23))
        self.btnPesquisar.setObjectName("btnPesquisar")
        self.btnAbrir = QtWidgets.QPushButton(Dialog)
        self.btnAbrir.setGeometry(QtCore.QRect(240, 400, 75, 23))
        self.btnAbrir.setObjectName("btnAbrir")
        self.btnSair = QtWidgets.QPushButton(Dialog)
        self.btnSair.setGeometry(QtCore.QRect(420, 400, 75, 23))
        self.btnSair.setStyleSheet("QPushButton::menu-indicator {\n"
"    image: url(download.png);\n"
"    subcontrol-position: right center;\n"
"    subcontrol-origin: padding;\n"
"    left: -2px;\n"
"}")
        self.btnSair.setCheckable(False)
        self.btnSair.setAutoRepeat(False)
        self.btnSair.setAutoExclusive(False)
        self.btnSair.setAutoDefault(False)
        self.btnSair.setDefault(False)
        self.btnSair.setFlat(False)
        self.btnSair.setObjectName("btnSair")
        self.btnLimpar = QtWidgets.QPushButton(Dialog)
        self.btnLimpar.setGeometry(QtCore.QRect(330, 400, 75, 23))
        self.btnLimpar.setStyleSheet("QPushButton::menu-indicator {\n"
"    image: url(download.png);\n"
"    subcontrol-position: right center;\n"
"    subcontrol-origin: padding;\n"
"    left: -2px;\n"
"}")
        self.btnLimpar.setCheckable(False)
        self.btnLimpar.setAutoRepeat(False)
        self.btnLimpar.setAutoExclusive(False)
        self.btnLimpar.setAutoDefault(False)
        self.btnLimpar.setDefault(False)
        self.btnLimpar.setFlat(False)
        self.btnLimpar.setObjectName("btnLimpar")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(170, 160, 421, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.cmpCodigo = QtWidgets.QLineEdit(Dialog)
        self.cmpCodigo.setGeometry(QtCore.QRect(20, 30, 51, 20))
        self.cmpCodigo.setObjectName("cmpCodigo")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 50, 81, 16))
        self.label_4.setObjectName("label_4")
        self.cmpCodBarras = QtWidgets.QLineEdit(Dialog)
        self.cmpCodBarras.setGeometry(QtCore.QRect(400, 70, 121, 20))
        self.cmpCodBarras.setText("")
        self.cmpCodBarras.setObjectName("cmpCodBarras")
        self.cmpDescricao = QtWidgets.QLineEdit(Dialog)
        self.cmpDescricao.setGeometry(QtCore.QRect(90, 30, 361, 20))
        self.cmpDescricao.setObjectName("cmpDescricao")
        self.cmpDescricaoReduzida = QtWidgets.QLineEdit(Dialog)
        self.cmpDescricaoReduzida.setGeometry(QtCore.QRect(20, 70, 361, 20))
        self.cmpDescricaoReduzida.setText("")
        self.cmpDescricaoReduzida.setObjectName("cmpDescricaoReduzida")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnPesquisar.setText(_translate("Dialog", "Pesquisar"))
        self.btnAbrir.setText(_translate("Dialog", "Abrir"))
        self.btnSair.setText(_translate("Dialog", "Sair"))
        self.btnLimpar.setText(_translate("Dialog", "Limpar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Descrição"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Descr. Reduzida"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Cód. de Barra"))
        self.label.setText(_translate("Dialog", "Código"))
        self.label_2.setText(_translate("Dialog", "Descrição"))
        self.label_4.setText(_translate("Dialog", "Cód. de Barra"))
        self.label_3.setText(_translate("Dialog", "Descrição Reduzida"))

