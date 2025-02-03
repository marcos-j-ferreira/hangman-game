import random 

words: list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "ximenia", "yuzu", "zucchini"]

def sort (words:list = [None]) -> list: # yes
    return random.choice(words)

def __a (word:str = None) -> list:

    #word = sort(words)

    arr:list  = []
    size:int = len(word)

    for i in range(size):
        arr.append("_")
    return arr

def _v(letter:str = None):

    word:str = sort(words)

    new_w = __a(word)


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

def main():

    life:int = 4

    word = sort(words)
    new_w = __a(word)
    nao:list = []


    while life > 0:

        letter:str = str(input("Enter a letter: "))

        validacao = _v(letter)

        if validacao is True:

            for i in range(len(word)):
                if letter == word[i]:
                    new_w[i] = letter
                    nao.append(letter)
            

        if validacao is False:
            life -= 1
            nao.append(letter)

        __print(word, letter, new_w, life, nao)
    
    print( " Fim de Jgo! \n")

def __print(word, letter, new_w, life, nao):

    ope:str = f"\n\n Vidas: {life}\n letras digitadas: {nao}\n letra digitada: {letter}\n\n Palavra: {new_w}\n\n"
    print(" \n------- Jogo da forca ------- \n")
    print(ope)


main()

