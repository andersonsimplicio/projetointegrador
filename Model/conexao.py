import sqlite3

class managerdb:

    def __init__(self):
        self.AbrirConexao()

    def AbrirConexao(self):
        self.conexao = sqlite3.connect("Model/database/Estoque2.db",uri=True)

    def fecharConexao(self):
        self.conexao.commit()
        self.conexao.close()

    def getcursor(self):
        return self.conexao.cursor()



