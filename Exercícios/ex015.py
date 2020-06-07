dia = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
preco = (60 * dia) + (km * 0.15)
print(f'O total a pagar é de R${preco:.2f}')
