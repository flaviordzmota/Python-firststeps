import shutil


def escrever_no_arquivo(texto):
    diretorio = 'Z:/PYTHON/Execícios Iniciais -  Python/notas.txt'
    arquivo = open(diretorio, "w")
    arquivo.write(texto)
    arquivo.close()

def atualizar_texto_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    #print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        #print(lista_notas)
        media = lambda notas:sum([int(i) for i in notas]) / 3
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

#def copiar_arquivo(nome_arquivo):
    #shutil.copy(nome_arquivo, 'Z:/PYTHON/notas.txt')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'Z:/PYTHON/Execícios Iniciais -  Python/notas.txt')

if __name__ == '__main__':
    mover_arquivo('notas.txt')
    #copiar_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_no_arquivo('Linha 1. \n')
    #aluno = '\nJoao, 9,5,8'
    #atualizar_texto_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')