import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    """validando número de telefone no formato (11 99623-2315)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    res = re.findall(modelo, celular)
    return res
