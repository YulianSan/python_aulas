from random import randint
from os import system

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
tentativas = 0

while True:
    print(f'Você está na rodada {(tentativas):02d}')
    try:
        number_choice = int(input('Tente acertar o número: '))
    except ValueError:
        print('Valor não é um número')
        break
    
    print(ROW)
    
    is_equal = number_choice == RANDOM_NUMBER
    no_have_more_try = tentativas >= MAX_TENTATIVAS
    
    if is_equal:
        print(f'Você acertou o número aleatório é {str(RANDOM_NUMBER)}')
        break
    elif no_have_more_try:
        print('Perdeu')
        break
    else:
        tentativas += 1
        print('Errou o número')
        
        is_greater = number_choice > RANDOM_NUMBER
        is_less = number_choice < RANDOM_NUMBER
        
        if is_greater:
            print('O número é menor')
        elif is_less:
            print('O número é maior')
            
    input('Precione enter para continuar e limpar a tela...')
    system('cls')