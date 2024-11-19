import pygame              # Importa o módulo pygame
pygame.init()              # Inicializa todos os módulos do pygame
pygame.mixer.music.load('ex01.mp3')  # Carrega o arquivo de música
pygame.mixer.music.play()  # Inicia a reprodução da música
pygame.event.wait()        # Aguarda um evento (para que o programa não feche imediatamente)
