"""
    Faça um Programa que peça dois números e imprima o menor deles.
"""

num1 = int(input("ENTRE COM O PRIMEIRO NUMERO: "))
num2 = int(input("ENTRE COM O SEGUNDO NUMERO: "))

if num1 > num2:
 print('\nNUMERO %d E MAIOR QUE NUMERO %d'%(num1,num2))
else:
 print('\nNUMERO %d E MAIOR QUE NUMERO %d'%(num2,num1))