#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input ("Qual é o salario do funcionario ? R$"))
novo = salario - (salario * 20 / 100)
print ("Um funcionario que ganhava R${: .2f} , com 20 % de baixa , começara a ganha R${: .2f}" .format(salario, novo))
