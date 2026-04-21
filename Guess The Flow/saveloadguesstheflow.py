import pickle

#arquivo para salvar o estado do jogo
ARQUIVO = "estado_jogo.pkl"

def salvar_sessao(estado_jogo):
    #salva em um arquivo o estado do jogo
    with open(ARQUIVO, "wb") as arquivo: #abre o arquivo/ 
        pickle.dump(estado_jogo, arquivo) #converte de python pra binário e escreve no arquivo

def carregar_sessao():
    #carrega, se tiver, o estado do jogo salvo
    try:
        with open(ARQUIVO, "rb") as arquivo:
            return pickle.load(arquivo) #retorna o objeto carregado
    except (FileNotFoundError, EOFError): #caso nao ache, retorna sem nada
        return None  #None se não houver sessão salva