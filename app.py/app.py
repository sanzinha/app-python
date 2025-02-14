print('salgados da visa\n')

print('1.cadastra restaurante')
print('2. listar restaurante')
print('3. ativar restaurante')
print('4.sair')

opçao_escolhida= int (input('escolha uma opção:'))
print(f'você escolheu a opção{opçao_escolhida}')

if opçao_escolhida == 1:
    print('cadastra restaurante')
elif opçao_escolhida == 2:
    print ('listar restaurante')
elif opçao_escolhida == 3:
    print('ativar restaurante')
else:
    print('encerrar o programa')
