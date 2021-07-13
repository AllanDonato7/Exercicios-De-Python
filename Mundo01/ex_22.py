 # Crie um programa que leia o nome completo de uma pessoa e mostre:  

# O nome com todas as letras maiúsculas e minúsculas.

# Quantas letras ao todo (sem considerar espaços).

# Quantas letras tem o primeiro nome.
 

nome = str(input("Qual o seu nome ? ")) .strip()
print("Analizando seu nome...")
print("Seu nome em maiusculas é {}".format(nome.upper()))
print("Seu nome em minusculas é {}".format(nome.lower()))
print("Seu nome ao todo tem {} letras" .format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras" .format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))
