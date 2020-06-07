from math import hypot
catOp  = float(input('Comprimento do cateto oposto: '))
catAdj = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(catOp, catAdj):.2f}')
