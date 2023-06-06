from random import randint
from os import system
def numeroAleatorio():
    ROW = '************************************'
    print(ROW)
    print('Número aleatório')
    print(ROW)

    dificuldades = {
        'easy': 30,
        'normal': 15,
        'hard': 5
    }

    dificuldade = input('Escolha a dificuldade:(easy, normal, hard) ')

    system('cls')

    if not (dificuldade in dificuldades):
        print('Dificuldade desconhecida, o valor sera 20')
        
    MAX_TENTATIVAS = dificuldades.get(dificuldade, 20)

    RANDOM_NUMBER = randint(1, 100)

    for tentativas in range(0, MAX_TENTATIVAS):
        print(f'Você está na rodada {(tentativas + 1):02d}')
        try:
            number_choice = int(input('Tente acertar o número: '))
            while(number_choice < 0 or number_choice > 100):
                number_choice = int(input('Coloque um número entre (1 a 100): '))
        except ValueError:
            print('Valor não é um número')
            break
        
        print(ROW)
        
        is_equal = number_choice == RANDOM_NUMBER
        
        if is_equal:
            print(f'Você acertou o número aleatório')
            break
        else:
            tentativas += 1
            print('Errou o número')
            
            is_greater = number_choice > RANDOM_NUMBER
            is_less = number_choice < RANDOM_NUMBER
            is_close = abs(number_choice - RANDOM_NUMBER)
            
            if is_greater:
                print('O número é menor')
            elif is_less:
                print('O número é maior')
            
            
            if is_close <= 5:
                print('Você está quente')
            elif is_close <= 15:
                print('Você está morno')
            else:
                print('Você está frio')
                
        input('Precione enter para continuar e limpar a tela...')
        system('cls')
    print(f'O número secreto é: {RANDOM_NUMBER}')