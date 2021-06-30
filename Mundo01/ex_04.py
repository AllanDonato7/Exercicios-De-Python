# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input("Digite Algo  : ")
print ("o tipo primitivo desse valor é " , type(n))
print ("só tem espaços ?", n.isspace())
print ("é numerico ?" , n.isnumeric())
print ("é alfabetico ?" , n.isalpha())
print ("é alfanumerico ?" , n.isalnum())
print ("Esta em maiúsculas ?", n.isupper())
print ("Esta em Minúsculas ?" , n.islower())
print ("Esta capitalizada ?" , n.istitle())


