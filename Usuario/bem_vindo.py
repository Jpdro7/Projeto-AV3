import time
import os

def cabecalho(usuario):
    print('...')
    time.sleep(1.50)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=' * 50)
    if usuario:
        print(f'Bem Vindo {usuario}'.center(50))
    else:
        print('Bem - Vindo'.center(50))
    print('=' * 50)