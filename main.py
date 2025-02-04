import random 

words: list = ["casa", "torre", "marcos"]

def sort (words:list = [None]) -> list:
    return random.choice(words)

def __a (word:str = None) -> list:

    arr:list  = []
    size:int = len(word) 

    for i in range(size):
        arr.append("_")

    return arr

def _v(word, letter:str = None):

    if letter is None:
        return False
    
    if type(letter) is not str:
        return False
    
    if len(letter) != 1:
        return False
    
    for i in range(len(word)):
        if letter == word[i]:
            return True
        
    return False


def __print(letter, new_w, life, nao):

    ope:str = f"\n\n Vidas: {life}\n letras digitadas: {nao}\n letra digitada: {letter}\n\n Palavra: {new_w}\n\n"
    print(" \n------- Jogo da forca ------- \n")
    print(ope)

def v_word(letter:str, nao:list = [None]) -> bool:

    size:int = len(nao)

    for i in range(size):
        if letter == nao[i]:
            return True
    
    return False


def end(life, word, nao, o):

    a:str = "\n\n --- Parabens você acertou!!! ---- \n\n"
    b:str = "\n\n --- Você perdeu!!! ---- \n\n"

    if o == 1:
        print(f"{a} Palavra: {word}\n Vidas restantes: {life}/4\n Letras digitadas: {nao}\n\n") 
    else:
        print(f"{b} Palavra: {word}\n Vidas restantes: {life}/4\n Letras digitadas: {nao}\n\n")


def v_t(letter: str) -> bool:

    if type(str(letter)):
        return True
    
    return False

def main():

    life:int = 4
    word = sort(words)
    new_w = __a(word)
    c:int = 1

    nao:list = []

    o:int = 0

    while life > 0:

        if c == len(word):
            o += 1
            end(life, word, nao, o) 
            break

        letter:str = str(input("Enter a letter: "))

        m = v_t(letter)

        if m is False:
            print("Digite uma letra")
            continue

        validacao = _v(word, letter)

        b:bool = v_word(letter, nao)

        if b is True:
            print("Letra já digitada")
            continue
        nao.append(letter)

        if validacao is True:
            c += 1

            size:int = len(new_w) 

            for i in range(size):
                
                if  word[i] == letter:
                    new_w[i] = letter
            
        if validacao is False:
            life -= 1

        __print( letter,new_w, life, nao)
    

    if life == 0:
        end(life, word, nao, o)

    print( " -- Fim de Jgo! -- \n")

main()
