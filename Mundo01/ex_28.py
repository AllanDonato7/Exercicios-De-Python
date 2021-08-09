# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint
computador = randint(0, 5) 
print("Vou pensar em um numero entre 0 e 5. tente adivinhar...")
jogador = int(input("Em que numero eu pensei :")) #JOGADOR TENTA ADIVINHA.
if jogador == computador : 
    print("PARABENS! Voce conseguiu me vencer.")
else:
    print("GANHEI !Eu pensei no numero {} e nao no {}!".format(computador , jogador))