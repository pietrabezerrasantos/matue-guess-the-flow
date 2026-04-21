import pygame
class Botao():
    def __init__(self, x, y, image, scale):
        largura = image.get_width() #pega a largura da imagem do botão
        altura = image.get_height() #pega a altura

        self.image = pygame.transform.scale(image, (int(largura * scale), int(altura * scale))) #redimenciona o botão com a imagem, as dimensões e a escala
        self.rect = self.image.get_rect() #verifica os toques do mouse e posicionar o botão na tela
        self.rect.topleft = (x, y) #as coordenadas para a posição do botão
        self.clicked = False #uma vez = um clique
    
    def draw(self, surface): #desenho do botão 
        action  = False #variavel de clique para o botão
        pos = pygame.mouse.get_pos() #pega as coordenadas da posição do mouse 

        if self.rect.collidepoint(pos): #verifica se a posição de clique do mouse está dentro da area do botão (rect)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #se sim
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0: #se nao foi clicado
            self.clicked = False #liberdado pra ser clicado

        surface.blit(self.image, (self.rect.x, self.rect.y)) #desenha o botão na superficie com as coordenadas

        return action #variavel principal
    
jogar_imagem = pygame.image.load("botao jogar.png") #carrega as imagens dos botoes
iniciar_imagem = pygame.image.load("botao iniciar.png")
reiniciar_imagem = pygame.image.load("botao reiniciar.png")

jogar_botao = Botao(300, 400, jogar_imagem, 1) #características dos botoes
iniciar_botao = Botao(530, 75, iniciar_imagem, 1)
reiniciar_botao = Botao(300, 400, reiniciar_imagem, 1)