p = float(input('Preço do produto? R$'))
desc = p - (p * 5 / 100)
print(f'O produto que custava {p}, na promoção com desconto de 5% vai custar R${desc:.2f}.')