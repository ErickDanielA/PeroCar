
import pygame
from random import randint

pygame.init()

def perocar():
    # x = 119 + 125 + 110
    x = 470
    y = 200

    pos_x_1 = 119
    pos_x_2 = 494
    pos_x_3 = 294
    pos_x_4 = 374




    pos_y_1 = randint(800, 1500)
    pos_y_2 = randint(1300, 1500)
    pos_y_3 = randint(1500, 1500)
    pos_y_4 = randint(1900, 2000)

    velocidade = 12

    derlei_Segundos = 0
    tempo_Segundo = 0
    tempo_Minutos = 0

    fundo = pygame.image.load('carros/background-1_0.png')
    carro = pygame.image.load('carros/carro_vermelho.png')
    carronpc = pygame.image.load("carros/carro_amarelo.png")
    carronpc2 = pygame.image.load("carros/carro_verde.png")
    carro_preto = pygame.image.load("carros/carro_preto.png")
    carro_policia = pygame.image.load("carros/carro_policia.png")



    velocidade_npc1 = 10
    velocidade_npc2 = 10
    velocidade_npc3 = 10
    velocidade_npc4 = 10

    janela = pygame.display.set_mode((800, 900))
    pygame.display.set_caption("Jogo")

    janela_aberta = True

    while janela_aberta:

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        
        
        
        font = pygame.font.SysFont('arial black', 30)
        if tempo_Segundo <= 9:
            texto = font.render(f" Timer: {tempo_Minutos}:0{tempo_Segundo}", True ,(255, 255, 255),(0,0,0 ))
        else:
            
            texto = font.render(f" Timer: {tempo_Minutos}:{tempo_Segundo}", True ,(255, 255, 255),(0,0,0 ))
        pos_texto = texto.get_rect()                                                        
        pos_texto.center = (86, 50)   
        
        if derlei_Segundos <= 20:
            derlei_Segundos += 1
        else:
            derlei_Segundos = 0
            tempo_Segundo += 1
            # texto = font.render(f" Timer: {tempo_Minutos}:{tempo_Segundo}", True ,(255, 255, 255),(0,0,0 ))


        if tempo_Segundo == 60:
            tempo_Segundo = 0
            tempo_Minutos += 1


        janela.blit(fundo, (0, 0))
        janela.blit(carro, (x, y))
        janela.blit(carronpc, (pos_x_1, pos_y_1))
        janela.blit(carronpc2, (pos_x_2, pos_y_2))
        janela.blit(carro_preto, (pos_x_3, pos_y_3))
        janela.blit(carro_policia, (pos_x_4, pos_y_4))
        janela.blit(texto, pos_texto)

        # pygame.draw.circle(janela, (0, 255, 0), (x, y), 50)
        
        # Controles
        comandos = pygame.key.get_pressed()
        
        # if comandos[pygame.K_UP]:
        #     y -= velocidade
        # if comandos[pygame.K_DOWN]:
        #     y += velocidade
        if comandos[pygame.K_RIGHT]:
            x += velocidade
        if comandos[pygame.K_LEFT]:
            x -= velocidade
        
        if pos_y_1 <= -250:
            pos_y_1 = randint(1200, 1500)
        if pos_y_2 <= -250:
            pos_y_2 = randint(1700, 2000)
        if pos_y_3 <= -250:
            pos_y_3 = randint(2200, 2400)
        if pos_y_4 <= -250:
            pos_y_4 = randint(2600, 3000)
            
        if y <= -250:
            y = 600
            
        # Restrição de X para o jogador
        if x <= 90:
            x = 90
        if x >= 470:
            x = 470
            

        if x - 60 < pos_x_1 and y + 200 > pos_y_1 and pos_y_1 > 30: #colisão carro amarelo, rua 1
            break
        if x + 100 > pos_x_2 and y + 200 > pos_y_2 and pos_y_2 > 30: #colisão carro verde, rua 4
            break
        if x < pos_x_3 and x > 130  and y + 200 > pos_y_3 and pos_y_3 > 30: #Colisão carro preto, rua 2
            break
        if x - 60 < pos_x_4 and x > 200 and y + 200 > pos_y_4 and pos_y_4 > 30: #Colisão carro policia, rua 3
            break
        

        pos_y_1 -= velocidade_npc1
        pos_y_2 -= velocidade_npc2
        pos_y_3 -= velocidade_npc3
        pos_y_4 -= velocidade_npc4
        
        pygame.display.update()

screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("Perocar")
fundo_menu = pygame.image.load("carros/background_meno.jpg")

# Função para desenhar texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Função principal do menu
def main_menu():
    running = True
    while running:
        screen.blit(fundo_menu, (0, 0))  # Fundo preto

        # Carregar fonte e renderizar título
        font = pygame.font.Font(None, 74)
        draw_text('Menu Principal', font, (255, 255, 255), screen, 400, 100)

        # Criar botões
        button_start = pygame.Rect(300, 250, 210, 60)
        button_quit = pygame.Rect(300, 350, 210, 60)

        # Desenhar botões
        pygame.draw.rect(screen, (0, 0, 255), button_start)
        pygame.draw.rect(screen, (255, 0, 0), button_quit)

        # Renderizar texto sobre os botões
        font_button = pygame.font.Font(None, 54)
        draw_text('Start', font_button, (255, 255, 255), screen, 400, 275)
        draw_text('Exit', font_button, (255, 255, 255), screen, 400, 375)

        # Detectar clique
        mx, my = pygame.mouse.get_pos()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_start.collidepoint((mx, my)):
            if click:
                # Iniciar o jogo
                perocar()
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                # exit()

        pygame.display.update()

main_menu()

pygame.quit()
    

