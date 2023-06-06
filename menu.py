from forca import forca
from numeroAleatorio import numeroAleatorio
from os import system
games = {
    'Forca': forca,
    'Número Aleatório': numeroAleatorio
}

def run_game(i):
    system('cls')
    try:
        list(games.values())[i]()
    except Exception as e:
        if len(games) + 1 != i:
            print('Jogo não encontrado')
    
def show_menu():
    for i, key in enumerate(games.keys()):
        print(f'{i + 1} - {key}')
        
def menu():
    while True:
        ROW = '************************************'
        print(ROW)
        print('Escolha o game')
        print(ROW)
        show_menu()
        print(f'{len(games) + 1} - Sair')
        game = int(input('Escolha o jogo: '))
        print(f'Você escolheu {game}')
        if run_game(game):
            print('game')
        if game == len(games) + 1:
            print('Adeus!!!')
            exit()
if __name__ == '__main__':
    menu()