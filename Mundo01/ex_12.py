# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto.

preço = float(input("Qual é o valor do produto ? R$"))
novo = preço - (preço * 5 / 100)
print ("O preço do produto era {: .2f} mas com desconto de 5 % ficara {: .2f}" .format(preço, novo))