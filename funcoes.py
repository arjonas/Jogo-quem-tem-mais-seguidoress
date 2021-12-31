from art import logo, vs
from gamedata import data
import random


def log():  # exibe o logo do game na tala
    print(logo)


log()


def versus(nome, dado, local, nome2, dado2, local2):  # exibe o logo de '''versus' na tala
    print(f'Compare o numero de seguidores de A \n {nome}, um(a) {dado} de {local}')

    print(vs)

    print(f'contra  B {nome2},uma(a) {dado2} de {local2}')


def winner(seguidor, following, nome1, nome2):
    if seguidor > following:
        return nome1
    else:
        return nome2


def sorteia():  # sorteia um dos itens de data
    return random.choice(data)


def usuario(palpite, Anome, Bnome, vencedor):
    if palpite == 'A':
        palpite = Anome
    elif palpite == 'B':
        palpite = Bnome
    if palpite == vencedor:
        return True
    else:
        return False



def troca(escolha, vencedor):
    if escolha == vencedor:
        return True
    elif escolha != vencedor:
        return False