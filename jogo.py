import pygame

pygame.init()
x = 119 + 125 + 110
y = 300

pos_x = 119
pos_y = 300

velocidade = 15


fundo = pygame.image.load('carros/background-1_0.png')
carro = pygame.image.load('carros/carro_red.png')
carronpc = pygame.image.load("carros/carro_verde.png")
carronpc2 = pygame.image.load("carros/carro_amarelo.png")
velocidade_npc = 20

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
    janela.blit(carronpc, (pos_x, pos_y))
    janela.blit(carronpc2, (pos_x + 375, pos_y))
    
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
    
    if pos_y <= -250:
        pos_y = 600

    pos_y -= velocidade_npc

pygame.quit()
    

