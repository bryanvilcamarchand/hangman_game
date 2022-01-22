# Import libreries that use in the project directory (ENG)
# Importo las librerias que usaremos en el proyecto (SPA)

import random
import os
import time

# Search in google and copy hangman images to use in our project. (ENG)
# Buscamos en google la imagen del ahorcado y la copiamos para usarlo en el proyecto. (SPA)

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

# Select the words to use in our project (ENG)
# Elegimos las palabras que usaremos en el proyecto (SPA)


    DB = ['CANADA', 'ISLANDIA', 'GROELANDIA', 'RUSIA', 'ANTARTIDA', 'ESTONIA']

# Use 'random.choise' to randomly select a worf of our small dataset DB (ENG)

# Select the word to use in the game, and show the numbers of characters of the word selected. We have 6 attemps to the game. (ENG) 
# Seleccionamos una palabra de manera aleatoria y mostrar la cantidad de guiones de acuerdo a ella. Tenemos 6 intentos en el juego. (SPA)

    word = random.choice(DB)
    spaces = ['_'] * len(word)
    attempts = 6

# Write the message to use in the intro of the game. We use time.sleep to appers dots to expect another messages. (ENG)
# Escribimos el mensaje que usaremos en el intro del juego. Usamos time.sleep para que aparezcan puntos mientras esperamos que aparezcan todos los mensajes. (SPA)
  
    print(''' 
           Bivenvenido(a) al juego del ahorcado.
    ''')
    
    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)


    print(''' 
    El invierno es la mejor época para algunos y la peor para otros.
    Esta estación del ańo es más dura en algunos países. Por ello tu
    reto hoy es adivinar cuales son los países más fríos del planeta.
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
    Adivina cuáles es el nombre del país se esconde a continuación: 
                                                      ''')

    time.sleep(2)
    print('''                                .                     ''')
    time.sleep(2)
    print('''                               .                     ''')
    time.sleep(2)


# Create an infinitive cicle, and shows the numbers of characters of the selected word. Then, ask the user for a letter. (ENG)
# Creamos un ciclo infinito, mostramos el numero de caracteres de la palabra seleccionada. Luego, le pedimos al usuario ingrese una letra. (SPA)

    while True:
        os.system('clear')
        for character in spaces:
            print(character, end=" ")
        print(images2[attempts])
        letter = input('Elige una letra: ').upper()

# Create the logical rules to guess the word. If you don't guess the word, you lose an attemp. If the number of attemps is 0, you lose the game. (ENG)
# Creamos la lógica para adivinar una letra de la palabra seleccionada. Si no aciertas, pierdes intentos. Si la cantidad de intentos es cero, pierdes el juego. (SPA)

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True


        if not found:
            attempts -= 1

        if '_' not in spaces:
            os.system('clear')
            print('Felicidades, ganaste el juego.')
            break
            input()

        if attempts == 0:
            os.system('clear')
            print('Lo siento, has perdido el juego.')
            break
            input()


if __name__ == '__main__':
    run()

