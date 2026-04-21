import pygame
import random #escolhe uma música aleatória
import botao #classe dos botões
import saveloadguesstheflow #salvar e carregar pra voltar de onde parou

#inicializando o pygame e o mixer 
pygame.init() 
pygame.mixer.init() 

pygame.mixer.music.load("Matuê - O Som [ ezmp3.cc ].mp3") #carrega a música "O som do Matuê"
pygame.mixer.music.play(-1) #faz ela tocar em loop

#configurações da janela
LARGURA, ALTURA = 800, 600 #dimenções
TELA = pygame.display.set_mode((LARGURA, ALTURA)) #cria a janela
BG = pygame.image.load("fundo jogo pipinha.png") #carrega o fundo
pygame.display.set_caption("MATUÊ: Guess the flow") #nome da janela

BRANCO = (255, 255, 255) #sublinhado
COR_TEXTO = (1, 43, 146) #texto das dicas e o digitado pelo jogador
COR_CORRETO = (1, 43, 110) #letras corretas
COR_POSICAO_ERRADA = (137, 43, 166) #letras corretas porem na posição errada
COR_DICAS = (137, 43, 166) #título Dicas, tentativas e alertas

# Fonte
fonte = pygame.font.Font("Blank River.ttf", 36)


# Estados do jogo
MENU_INICIAL = "menu_inicial"
MENU_REGRAS = "menu_regras"
MENU_PRINCIPAL = "menu_principal"
MENU_FINAL = "menu_final"
estado_atual = MENU_INICIAL #onde o jogo começa

# Dados das músicas possíveis
palavras_musicas = {
    "o som": "Álbum: 333",
    "like this": "Álbum: 333",
    "fortal": "Álbum: 333",
    "maria": "Álbum: 333",
    "v de vilão": "Álbum: 333",
    "castlevania": "Álbum: 333",
    "cogulandia": "Álbum: Máquina do tempo",
    "antes": "Álbum: Máquina do tempo",
    "gorila roxo": "Álbum: Máquina do tempo",
    "é sal": "Álbum Máquina do tempo",
    "mdt": "Álbum Máquina do tempo",
    "vem chapar": "Álbum Máquina do tempo",
    "kenny g": "Essa música é um single",
    "anos luz": "Essa música é um single",
    "celine": "Essa música é um single",
    "mantém": "Essa música é um single",
    "banco": "Essa música é um single",
    "quer voar": "Essa música é um single",
    "vampiro": "Essa música é um single",
}

#função pra resetar o jogo/carregar a sessão
def reset_jogo():
    global palavra_secreta, album, num_letras, tentativas, input_text, tentativa_num, feedback_text, alerta_exibido, dica_desbloqueada, estado_atual #variaveis pra usar depois
    estado_salvo = saveloadguesstheflow.carregar_sessao() #chamando a função do saveload,carregando dados da sessão anterior se tiver
    
    if estado_salvo: #caso tenha uma sessão salva
        # carrega a sessão salva
        estado_atual = estado_salvo["estado_atual"] #com os dados passados
        palavra_secreta = estado_salvo["palavra_secreta"]
        album = estado_salvo["album"]
        num_letras = estado_salvo["num_letras"]
        tentativas = estado_salvo["tentativas"]
        input_text = estado_salvo["input_text"]
        tentativa_num = estado_salvo["tentativa_num"]
        feedback_text = estado_salvo["feedback_text"]
        alerta_exibido = estado_salvo["alerta_exibido"]
        dica_desbloqueada = estado_salvo["dica_desbloqueada"]
    else: #caso não tenha uma sessão salva
        #inicia uma nova sessão
        palavra_secreta, album = random.choice(list(palavras_musicas.items())) #escolhe aleatoriamente a música e o álbum correspondente na lista
        num_letras = len(palavra_secreta.replace(" ", "")) #calculando o número de letras sem espaços
        tentativas = 6
        input_text = ""
        tentativa_num = 1 #indica a primeira tentativa
        feedback_text = [] #inicia o feedback com uma lista vazia pq não começou ainda
        alerta_exibido = False #o alerta de 3 tentativas não aparece ainda
        dica_desbloqueada = False #a segunda dica não foi desbloqueada ainda
        estado_atual = MENU_INICIAL #começa no menu inicial

reset_jogo()

# Função de feedback
def verificar_palavra(tentativa, palavra_secreta): #o que o jogador tentou e a música escolhida
    feedback = [] #lista vazia pra armazenar o resultado da comparação tentativa e palavra secreta
    palavra_secreta_temp = list(palavra_secreta) #transforma a string em lista para a verificação dos caracteres separados

    for i in range(len(tentativa)): #cria um loop que percorre a lista para comparar com a palavra secreta
        if i < len(palavra_secreta) and tentativa[i] == palavra_secreta[i]: #testa se a letra ta certa e na posição certa
            feedback.append((tentativa[i].upper(), COR_CORRETO)) #se sim, ela é add ao feedback em maiusculo e com a cor certa
            palavra_secreta_temp[i] = None #transforma em none pois ainda não foi verificada
        else:
            feedback.append((tentativa[i], None))

    for i in range(len(tentativa)): #o loop agora confere as letras corretas em posição errada
        if feedback[i][1] is None: #verifica se nao foi verificada ainda
            if tentativa[i] in palavra_secreta_temp: #verifica se i aparece na palavra secreta mas no lugar errado
                feedback[i] = (tentativa[i].lower(), COR_POSICAO_ERRADA) #se sim, ela vira minuscula e é marcada pela cor 
                palavra_secreta_temp[palavra_secreta_temp.index(tentativa[i])] = None #transforma em none pois ja foi ferificado
            else:
                feedback[i] = ("_", BRANCO) #se a letra i nao ta na palavra_secreta_temp, o feedback ganha um _ branco

    return feedback


# Funções para cada menu
def mostrar_menu_inicial():
    BG = pygame.image.load("fundo jogo pipinha.png") #carrega o fundo
    TELA.blit(BG, (0,0)) #posição dele
    

def mostrar_menu_regras():
    BG = pygame.image.load("fundo regras.png")
    TELA.blit(BG, (0,0))
    
    
    

def mostrar_menu_principal():
    BG = pygame.image.load("fundo default.png")
    TELA.blit(BG, (0,0))
    
    dica_texto = fonte.render("Dicas:", True, COR_DICAS) #cria "dicas" com a fonte que eu escolhi
    TELA.blit(dica_texto, (200, 20)) #posição dela
    dica_texto1 = fonte.render(f"- Essa música tem {num_letras} letras", True, COR_TEXTO) #mensagem da dica
    TELA.blit(dica_texto1, (200, 60)) #posição dela
    if dica_desbloqueada: #verifica se ja desbloqueou a dica
        dica_texto2 = fonte.render(f"- {album}", True, COR_TEXTO) #se sim,mostra a proxima dica (album)
        TELA.blit(dica_texto2, (200, 100)) #posição da dica

    tentativa_texto = fonte.render(f"Tentativa {tentativa_num}/{tentativas}", True, COR_DICAS) #tentativas/cor
    TELA.blit(tentativa_texto, (200, 140)) #posição

    if tentativa_num == 4 and not alerta_exibido: #verifica se passou da 3 tentativa e se o alerta nao apareceu
        alerta_texto = fonte.render("Atenção! Só restam mais 3 tentativas!", True, COR_POSICAO_ERRADA) #caso sim, mostra ele
        TELA.blit(alerta_texto, (200, 180)) #posição

    input_texto = fonte.render(input_text, True, COR_TEXTO) #mostra o texto do jogador/fonte e cor
    TELA.blit(input_texto, (LARGURA // 2 - input_texto.get_width() // 2, ALTURA // 2 - 40)) #posição centralizada

    x_offset = LARGURA // 2 - len(feedback_text) * 15 // 2 #centraliza o feedback
    for letra, cor in feedback_text:
        letra_render = fonte.render(letra, True, cor) #cria o feedback por letra e cor
        TELA.blit(letra_render, (x_offset, ALTURA // 2)) #mostra na tela para a proxima letra ficar no meio
        x_offset += letra_render.get_width() + 5 #add um pequeno espaço pra proxima letra entrar

def mostrar_menu_final(ganhou):
    BG = pygame.image.load("fundo default.png") #carrega o fundo
    TELA.blit(BG, (0,0)) #posição dele
    if ganhou:
        mensagem = "Acertou! Você é fã mesmo!"
    else:
        mensagem = f"Errou! A música escolhida era \"{palavra_secreta}\"! Ouça mais Matuê!"

    texto = fonte.render(mensagem, True, COR_CORRETO if ganhou else COR_DICAS) #mostra a mensagem no fim do jogo
    TELA.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 20)) #posição das mensagens


ganhou = False #variavel de derrota ou vitória
estado_atual = MENU_INICIAL #o jogo começa assim

# loop principal
while True:
    for event in pygame.event.get(): #percorre todos os eventos 
        if event.type == pygame.QUIT: #se fechar a janela

            pygame.mixer.music.stop() #a música para

            # salva o jogo só se o estado atual for MENU_PRINCIPAL
            if estado_atual == MENU_PRINCIPAL:
                estado_jogo = {
                    "estado_atual": estado_atual,
                    "palavra_secreta": palavra_secreta,
                    "album": album,
                    "num_letras": num_letras,
                    "tentativas": tentativas,
                    "input_text": input_text,
                    "tentativa_num": tentativa_num,
                    "feedback_text": feedback_text,
                    "alerta_exibido": alerta_exibido,
                    "dica_desbloqueada": dica_desbloqueada,
                }
                saveloadguesstheflow.salvar_sessao(estado_jogo) #salva os dados dessas variaveis 
            else:
                # iimpa o estado salvo se o jogo estiver em outro menu
                saveloadguesstheflow.salvar_sessao({})
            
            pygame.quit() #encerra o pygame

        # logica entre os menus e eventos
        if estado_atual == MENU_INICIAL:
            mostrar_menu_inicial() #mostra o menu com o que foi adicionado nele
            botao.jogar_botao.draw(TELA) #desenha o botão jogar
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao.jogar_botao.rect.collidepoint(event.pos): #verifica se o botão foi clicado
                    estado_atual = MENU_REGRAS #muda para o menu regras

        elif estado_atual == MENU_REGRAS:
            mostrar_menu_regras()
            botao.iniciar_botao.draw(TELA) #desenha o botão de iniciar
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao.iniciar_botao.rect.collidepoint(event.pos): #verifica se o botão foi clicado
                    estado_atual = MENU_PRINCIPAL #muda para o menu principal

        elif estado_atual == MENU_PRINCIPAL:
            mostrar_menu_principal()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #se pressionou enter
                    if len(input_text) == len(palavra_secreta):#verifica se a tentativa é do tamanho da palavra secreta
                        feedback_text = verificar_palavra(input_text.lower(), palavra_secreta) # se sim, chama a função verificar palavra
                        if input_text.lower() == palavra_secreta: #se for a mesma, ganhou
                            ganhou = True
                            estado_atual = MENU_FINAL #muda para o menu final
                        else: #se não acertar ainda, sobem as tentativas
                            tentativa_num += 1
                            if tentativa_num == 3: #se chegar a 3, desbloqueia a dica
                                dica_desbloqueada = True
                            if tentativa_num >= tentativas: #se acabarem as tentativas, perde o jogo
                                ganhou = False
                                estado_atual = MENU_FINAL
                        input_text = ""
                    else:
                        alerta_exibido = True #a quantidade de letras deve ser igual
                elif event.key == pygame.K_BACKSPACE:#se backspace for clicado,apaga a ultima letra
                    input_text = input_text[:-1]
                else: #clicou em algo que não funciona no jogo
                    if len(input_text) < len(palavra_secreta): #verifica se aina tem espaço para digitar
                        input_text += event.unicode #adiciona a letra clicada

        elif estado_atual == MENU_FINAL:
            mostrar_menu_final(ganhou) #mostra o menu final dependendo da variavel ganhou
            botao.reiniciar_botao.draw(TELA) #desenha o reiniciar
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if botao.reiniciar_botao.rect.collidepoint(event.pos):#verifica se foi clicado
                    #limpa o estado salvo ao finalizar a partida
                    saveloadguesstheflow.salvar_sessao({})
                    reset_jogo() #chama a função de reset
                    estado_atual = MENU_PRINCIPAL

    pygame.display.flip() #atualização da tela