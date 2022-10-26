from datetime import datetime

from pyparsing import sys


def nomear_cachorro():
    nome_cachorro = input("Digite o nome do cachorro: ")
    return nome_cachorro


def nomear_dono_cachorro():
    nome_dono = input("Digite o nome do Dono (a): ")
    return nome_dono


def validar_nome(nome):
    """Validando se o nome nao eh vazio"""
    if len(nome) == 0:
        return False
    else:
        return True


def marcar_atendimento():
    data_e_hora_em_texto = input("Digite data e hora do atendimento: ")
    data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
    return data_e_hora


def pesar_cachorro():
    peso_cachorro = float(input("Digite o peso do cachorro: "))
    return peso_cachorro


def mensurar_tamanho():
    tamanho_cachorro = int(input('Tamanho do cachorro: Digite 1 - P/ 2 - M/ 3 - G: '))
    return tamanho_cachorro


def validar_tamanho(tamanho):
    if tamanho in {1, 2, 3}:
        return True
    else:
        return False


def precificar_banho(peso_cachorro):
    if peso_cachorro <= 5:
        preco_banho = peso_cachorro * 5.60
    elif peso_cachorro > 5:
        preco_banho = peso_cachorro * 7.80
    return preco_banho


def precificar_tosa(peso_cachorro, tamanho_cachorro):
    if tamanho_cachorro == 1 and peso_cachorro <= 5:
        preco_tosa = peso_cachorro * 7.6
    elif tamanho_cachorro == 1 and peso_cachorro >= 5:
        preco_tosa = peso_cachorro * 8.9
    if tamanho_cachorro == 2 and peso_cachorro <= 5:
        preco_tosa = peso_cachorro * 8.60
    elif tamanho_cachorro == 2 and peso_cachorro >= 5:
        preco_tosa = peso_cachorro * 9.70
    if tamanho_cachorro == 3 and peso_cachorro <= 5:
        preco_tosa = peso_cachorro * 9.40
    elif tamanho_cachorro == 3 and peso_cachorro >= 5:
        preco_tosa = peso_cachorro * 10.20
    return preco_tosa


def calcular_total_pagar(preco_tosa, preco_banho):
    preco_final = preco_banho + preco_tosa
    return preco_final


def calcular_desconto(preco_banho, preco_tosa):
    desconto = (preco_banho + preco_tosa) * 0.85
    if preco_tosa > 0 and preco_banho > 0:
        return desconto
    else:
        return preco_banho + preco_tosa


def calcular_faturamento_petshop():
    servicos = [57.90, 72, 96, 35.70, 47.25]
    faturamento = sum(servicos)
    return f'O faturamento foi de {faturamento}'


def calcular_custo():
    custo = 61.77
    return custo


def calcular_lucro(faturamento, custo):
    lucro = faturamento - custo
    return lucro


def imprimir_servicos(nome, nome_dono, horario_atendimento, peso, tamanho, preco_banho, preco_tosa, preco_final,
                      desconto):
    print("-" * 80)
    print(f"Nome: {nome}")
    print(f"Nome do Dono(a){nome_dono} ")
    print(f"Peso: {peso}")
    print(f"Tamanho: {tamanho}")
    print(f"Data e hora do Atendimento{horario_atendimento}")
    print(f"Valor do banho: {preco_banho}")
    print(f"Valor tosa: {preco_tosa}")
    print("-" * 80)
    print(f"Valor total:{preco_final}")
    print("-" * 80)
    print(f"Desconto de 15% na compra dos dois servircos:{desconto}")
    print("-" * 80)


def abandonar_programa():
    sys.exit()


if _name_ == "_main_":
    print('==================== PETSHOP Cão Feliz :) ====================')
    nome = input("Digite o nome do cachorro: ")
    if not validar_nome(nome):
        abandonar_programa()
    nome_dono = nomear_dono_cachorro()
    peso = pesar_cachorro()
    tamanho = mensurar_tamanho()
    if not validar_tamanho(tamanho):
        abandonar_programa()
    horario_atendimento = marcar_atendimento()
    preco_banho = precificar_banho(peso)
    preco_tosa = precificar_tosa(peso, tamanho)
    preco_final = calcular_total_pagar(precificar_tosa, precificar_banho)
    desconto = calcular_desconto(preco_banho, preco_tosa)

    imprimir_servicos(nome, nome_dono, horario_atendimento, peso, tamanho, preco_banho, preco_tosa, preco_final,
                      desconto)