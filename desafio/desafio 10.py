preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava RS{}, na promoção com desconto de %5 vai custa R${}'.format(preço, novo))