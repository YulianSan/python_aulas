from random import choice
from os import system

def forca():
    palavras = ['cavalo', 'aguia', 'gato', 'vaca']
    ROW = '************************************'
    
    palavra = choice(palavras).upper()
    print(palavra)

    win = False
    died = False
    letter_correct = ['_' for _ in palavra]
    error = 0
    
    while(not win and not died):
        print(ROW)
        print('Jogo da forca')
        print(ROW)
        
        while(True):
            letter = input('Escolha uma letra: ').upper()
            if(letter not in letter_correct):
                break
            else:
                print('A letra já foi escolhida, selecione outra letra: ')
                
        if letter in palavra:
            for i, letter_forca in enumerate(palavra):
                if letter == letter_forca:
                    letter_correct[i] = letter
        else:
            print('Errou!!!')
            error += 1
            died = error == 7
            
        print(letter_correct)
        win = '_' not in letter_correct
        print(f'Você tem mais {7 - error} tentativas')    
        input('Press enter to continue...')    
        system('cls')
    
    if died:
        print('Você perdeu :(')
    if win:
        print('Você ganhou!')
        
if __name__ == '__main__':
    forca()
print('Obrigado por participar')