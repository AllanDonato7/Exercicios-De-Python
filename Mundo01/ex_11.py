# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input(" Largura da Parede : "))
alt = float(input(" Altura da Parede : "))
area = larg * alt
print ("Sua Parede tem a dimensao de {}x{} e sua area é de {}m2" .format(larg, alt, area))
tinta = area / 2
print ("Sua parede ira precisar de {}L de tinta " .format(tinta))
