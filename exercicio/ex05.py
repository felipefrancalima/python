real = float(input("Quanto dinheiro você tem carteira? R$"))
dolar = real / 5.44
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))