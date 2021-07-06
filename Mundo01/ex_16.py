# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
 
from math import trunc
num = float(input("Digite um valor : "))
print ("O numero digitado foi {} e a sua porçao inteira é {}" .format(num,trunc(num)))