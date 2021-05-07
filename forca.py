def abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    palavra = "abacaxi" #nome que o usuario tem q adivinhar 
    palavra_secreta = palavra.upper() #a palavra vai ficar em caixa alta
    return palavra_secreta 

def inicializa_letras_acertadas(palavra):
    return " ".join(["*" for letra in palavra])

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, pede_chute, palavra_secreta):
    
    index = 0 #retorna a primeira letra 
    for letra in palavra_secreta: #letra vai percorrer a palavra secreta
        if (chute == letra): #verificar se o chute esta na letra 
            letras_acertadas[index] = letra #a cada letra acertada vai verificando o index
        index += 1 #add mais um acerto
        return letra

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    
    palavra_secreta   = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
     
    print(letras_acertadas)
  
    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(inicializa_letras_acertadas)
    
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count('*'))
            if (letras_faltando == "0"):
                print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavra_secreta.upper()))
        else:
            erros += 1
            print(letras_acertadas)
            print('Ainda faltam acertar {} letras'.format(letras_faltando))
            print('Você ainda tem {} tentativas'.format(7-erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "*" not in letras_acertadas

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()