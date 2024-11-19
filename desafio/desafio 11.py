salário = float(input('Qual é o salário do funcionario? R$'))
novo = salário + (salário * 15 / 100)
print('um funcionario que R${:.2F}, com 15% de aumento, passa a receber R${:.2f} salário'.format(salário, novo))