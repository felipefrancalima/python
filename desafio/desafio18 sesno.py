import math

# Solicita ao usuário para inserir um valor de ângulo
angulo = float(input('Digite o ângulo que você deseja: '))

# Calcula o seno, cosseno e tangente do ângulo
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Exibe os resultados formatados com duas casas decimais
print('O ângulo de {}° tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(angulo, tangente))
