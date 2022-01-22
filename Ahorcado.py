import random
import os
import time



def run():

    images = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    images2 = images[::-1]

    DB = ['BANDERA', 'HIMNO', 'ESCUDO', 'ESCARAPELA']

    word = random.choice(DB)
    spaces = ['_'] * len(word)
    attempts = 6

  
    print(''' 
           Bivenvenido a la Trivia de símbolos patrios.
    ''')
    
    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)


    print(''' 
    Como buen peruano estoy seguro que conoces cuales son nuestros
        símbolos patrios. Pondremos a prueba tus conocimientos.
    ''')

    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)


    print('''         
                        Comienza el juego 
                                                      ''')

    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)

    print('''         
    Adivina cual es el símbolo patrio que se esconde a continuación: 
                                                      ''')

    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)
    print('''                               .                     ''')
    time.sleep(2)


    while True:
        os.system('clear')
        for character in spaces:
            print(character, end=" ")
        print(images2[attempts])
        letter = input('Elige una letra: ').upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attempts -= 1

        if '_' not in spaces:
            os.system('clear')
            print('Ganaste')
            break
            input()

        if attempts == 0:
            os.system('clear')
            print('Perdiste')
            break
            input()




if __name__ == '__main__':
    run()

