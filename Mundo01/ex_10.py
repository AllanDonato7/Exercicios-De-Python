# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input(" Quanto dinheiro na carteira vc tem ? "))
dolar = real / 4.92
print("Com R${: .0f} voce pode comprar US${: .0f}".format(real, dolar))
