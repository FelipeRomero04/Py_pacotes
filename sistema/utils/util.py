def effect(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


def menu():
   
    effect('MENU PRINCIPAL')

    print(' 1 - Cadastrar nova usuário\n',
        '2 - Ver pessoas cadastradas\n',
        '3 - Reiniciar lista\n',
        '4 - Sair do Sistema\n'
        )
    
    while True:
        option = input('Sua opção: ')
        if not option.isnumeric() :
            print('Erro: Insira uma das opções acima.')
            continue
        elif not option in (('1'), ('2'), ('3'), ('4')):
            print('Erro: Essa opção não existe!')
            continue
        break
    return option


def debug_dados_name():
    while True:
        try:
            name = input('Informe o nome: ').strip()
            
            if not name.isalpha():
                print('Erro! Informe um nome valido...')
                continue
            return name

        except Exception:
            print('Erro! Seus dados não foram inseridos corretamente...')
            continue


def debug_dados_old():
    while True:
        try:
            old = input('Informe a idade: ').strip()

            if not old.isnumeric():
                print('Erro! Seus dados não foram inseridos corretamente...')
                continue
            return old
        
        except Exception:
            print('Erro! Algum dado não foi inserido corretamente...')
            continue

    