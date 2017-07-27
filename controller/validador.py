#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from PyQt5.QtWidgets import QMessageBox

__all__ = ['validar_cpf', 'validar_cnpj']




def validar_cpf(cpf):

    cpf = ''.join(re.findall('\d', str(cpf)))

    if (not cpf) or (len(cpf) < 11):
        return False

    # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos que faltam
    inteiros = list(map(int, cpf))
    novo = inteiros[:9]

    while len(novo) < 11:
        r = sum([(len(novo)+1-i)*v for i,v in enumerate(novo)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)

    # Se o número gerado coincidir com o número original, é válido
    if novo == inteiros:
        return cpf
    return False

def validar_cnpj(cnpj):
    cnpj = ''.join(re.findall('\d', str(cnpj)))

    if (not cnpj) or (len(cnpj) < 14):
        return False

    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
    inteiros = list(map(int, cnpj))
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)

    # Se o número gerado coincidir com o número original, é válido
    if novo == inteiros:
        return cnpj
    return False


def AlertaCpfCnpj():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Atenção")
    msg.setInformativeText("Você deve escolher:\n Pessoa Física \n Pessoa Juridica")
    msg.setWindowTitle("Erro Para Salvar")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDetailedText("É obrigatório a selecção de pessoa física ou Juridica para o cadastro")
    msg.show()
    msg.exec_()

# A função abaixo Captura a opeção do usuario de salvar ou não dados no Banco
def confirmar():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Atenção")
    yes = msg.addButton("sim",QMessageBox.YesRole)
    msg.addButton("Não",QMessageBox.NoRole)
    msg.setInformativeText("Você deseja efetuar o cadastro ?")
    msg.setWindowTitle("Concluir Cadastro")
    msg.show()
    msg.exec_()
    if msg.clickedButton() == yes:
        return True
    else:
        return False


