import random 

words: list = ["casa", "torre", "marcos"]

def sort (words:list = [None]) -> list: # yes
    return random.choice(words)

def __a (word:str = None) -> list:

    #word = sort(words)

    arr:list  = []
    size:int = len(word) 

    for i in range(size):
        arr.append("_")

    return arr

def _v(word, letter:str = None):

    #word:str = sort(words)

   #new_w = __a(word)


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

def main():

    life:int = 4
    word = sort(words)
    new_w = __a(word)
  
    # word = sort(words)
    # new_w = __a(word)
    # nao:list = []

    nao:list = []

    while life > 0:

        letter:str = str(input("Enter a letter: "))

        validacao = _v(word, letter)

        b:bool = v_word(letter, nao)

        if b is True:
            print("Letra já digitada")
            continue
        nao.append(letter)

        if validacao is True:

            #add(letter, word, new_w, nao, life)
            #b:bool = v_word(letter, nao)
            #nao.append(letter)

            size:int = len(new_w) 

            for i in range(size):
                
                if  word[i] == letter:
                    new_w[i] = letter
            
        if validacao is False:
            life -= 1
            #nao.append(letter)


        __print( letter,new_w, life, nao)
    
    print( " Fim de Jgo! \n")

# def add(word, letter,new_w, nao, life):

#     lifee = life


#     for i in range(len(word)):
#         if letter == word[i]:
#             new_w[i] = letter
#             nao.append(letter)
            

#     __print(letter, new_w, lifee, nao)

    
main()

