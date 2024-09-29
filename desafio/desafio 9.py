larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('sua parede tem a dimesão de {}x{} e sua área é de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('para pinta essa parede, você precisá de {} litros de tinta.'.format(tinta))