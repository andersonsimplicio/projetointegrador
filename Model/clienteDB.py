import Model.conexao as conn
import sqlite3
from PyQt5.QtWidgets import QMessageBox
class clienteBD:
    def __init__(self):
        self.banco = conn.managerdb()

    def insert(self,dados,lougra):
        lista= [tuple(dados)]
        c = self.banco.getcursor()
        lista_end = [tuple(lougra)]
        try:
            c.executemany("""INSERT INTO Cliente (cod_cliente,nome,nome_fantasia,cpf,cnpj,tipo,status,ins_estadual,ins_municipal,email,emailxml,telefone1,telefone2)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",lista)
            c.executemany("""INSERT INTO Cliente_Endereco(cod_cliente,cod_municipio,numero,logradouro,cidade,bairro,pais,uf,complemento,cep)VALUES(?,?,?,?,?,?,?,?,?,?)""",lista_end)
            self.banco.fecharConexao()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setInformativeText("Dados salvos \ncom sucesso!!!")
            msg.setWindowTitle("Banco de dados")
            msg.show()
            msg.exec_()
        except sqlite3.Error as ex:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erro ao Gravar")
            msg.setInformativeText("Erro ao gravar os dados no Banco!")
            msg.setWindowTitle("Banco de Dados")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            msg.exec_()







