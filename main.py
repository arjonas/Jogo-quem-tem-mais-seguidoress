from art import logo, vs
from gamedata import data
import random
import os
from funcoes import sorteia,versus,winner,usuario,troca






A = sorteia()

B = sorteia()

exit = False

while exit is False :

  Anome = A['nome']
  Adado=  A['descrição']
  Aseguidores= A['follower_count']
  Alocal = A['país']

  Bnome = B['nome']
  Bdado=  B['descrição']
  Bseguidores= B['follower_count']
  Blocal = B['país']
  Vencedorseguidores = 0
  if Aseguidores > Bseguidores:
    Vencedorseguidores = Aseguidores
  else:
    Vencedorseguidores = Bseguidores

  versus(Anome,Adado,Alocal,Bnome,Bdado,Blocal)




  vencedor =  winner(Aseguidores,Bseguidores,Anome,Bnome)
  print(vencedor)


  palpit  = str(input('\nDigite A ou B \n')).upper()
  print(palpit)
  escolha = usuario(palpit,Anome,Bnome,vencedor)
  print(escolha)



  if escolha is True :
    os.system('cls')
    print(f'Voce acertou  o vencedor é {vencedor} com {Vencedorseguidores} Milhoes de seguidores')

  else:
    print(f'Voce errou \n o Vencedor(a) é {vencedor} com {Vencedorseguidores} Milhoes de seguidores')
    exit = True


  if palpit == 'A':
    B = sorteia()
  elif palpit == 'B':
    A = sorteia()

