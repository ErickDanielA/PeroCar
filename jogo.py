import pygame
from random import randint

pygame.init()
x = 119 + 125 + 110
y = 200

pos_x = 119

pos_y_1 = 800
pos_y_2 = 800
pos_y_3 = 800
pos_y_4 = 800

velocidade = 12



fundo = pygame.image.load('carros/background-1_0.png')
carro = pygame.image.load('carros/carro_vermelho.png')
carronpc = pygame.image.load("carros/carro_amarelo.png")
carronpc2 = pygame.image.load("carros/carro_verde.png")
carro_preto = pygame.image.load("carros/carro_preto.png")
carro_policia = pygame.image.load("carros/carro_policia.png")

velocidade_npc1 = 10
velocidade_npc2 = 11
velocidade_npc3 = 20
velocidade_npc4 = 9

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo")

janela_aberta = True

while janela_aberta:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    
        

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(carronpc, (pos_x, pos_y_1))
    janela.blit(carronpc2, (pos_x + 375, pos_y_2))
    janela.blit(carro_preto, (pos_x + 175, pos_y_3))
    janela.blit(carro_policia, (pos_x + 255, pos_y_4))

    # pygame.draw.circle(janela, (0, 255, 0), (x, y), 50)
    pygame.display.update()

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    
    if pos_y_1 <= -250 and pos_y_2 <= -250 and pos_y_3 <= -250:
        pos_y_1 = randint(600, 1500)
        pos_y_2 = randint(600, 1500)
        pos_y_3 = randint(600, 1500)
        pos_y_4 = randint(600, 1500)

    if y <= -250:
        y = 600

    pos_y_1 -= velocidade_npc1
    pos_y_2 -= velocidade_npc2
    pos_y_3 -= velocidade_npc3
    pos_y_4 -= velocidade_npc4

pygame.quit()
    

