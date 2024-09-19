import os

hospedes = []

def mostra_titulo():

def mostra_titulo():
 print("""
𝕲𝖔𝖑𝖉𝖊𝖓 𝕻𝖆𝖗𝖐 𝕴𝖓𝖙𝖊𝖗𝖓𝖆𝖈𝖎𝖔𝖓𝖆𝖑
""")

def mostra_escolha():
    print('1. Cadastro de hospedes')
    print('2. Listr hospedes')
    print('3. Ativar hospedes')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            print('Cadastrar hospede')
        elif opcao_escolhida == 2:
            print('Listar hospede')
        elif opcao_escolhida == 3:
            print('Ativar/desativar hospede')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def mostra_hospedes():
    os.system('cls')
    print('Lista de hospedes\n')

    for hospedes in hospedes:
        print(f'-{hospedes}') 

        input('\nDigite uma tecla para voltar ao menu principal:')
        main()   

def finalizar_programa():
    os. system('cls')
    print('finalizando programa')

def opcao_invalida():
    print('Este caracter não é permitido')
    input('Digite qualquer tecla')
    main()        

def main():
    mostra_titulo()
    mostra_escolha()
    escolhe_opcao()

if __name__ == '__main__':
    main()