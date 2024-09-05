print("""
𝕲𝖔𝖑𝖉𝖊𝖓 𝕻𝖆𝖗𝖐 𝕴𝖓𝖙𝖊𝖗𝖓𝖆𝖈𝖎𝖔𝖓𝖆𝖑
""")

print('1. Cadastro de hospedes')
print('2. Listr hospedes')
print('3. Ativar hospedes')
print('4. Sair da aplicação')

opcao_escolhida = int(input('Escolha uma opção: '))
print('Você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar hospede')
elif opcao_escolhida == 2:
    print('Listar hospede')
elif opcao_escolhida == 3:
    print('Ativar/desativar hospede')
else:
    print('Saindo da aplicação')
    