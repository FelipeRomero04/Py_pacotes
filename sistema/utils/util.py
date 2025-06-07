def effect(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


def menu():
   
    effect('MENU PRINCIPAL')

    print('''
        1 - Cadastrar nova usuário
        2 - Ver pessoas cadastradas
        4 - Deletar usuário
        3 - Sair do Sistema''')
    
    option = input('Sua opção: ')
    return option


def debug_dados_name():
    while True:
        try:
            name = input('Informe o nome: ').strip()
            
            if not name.isalpha():
                print('Erro!')
                continue
            return name

        except Exception:
            print('Erro! Algum dado não foi inserido corretamente...')
            continue


def debug_dados_old():
    while True:
        try:
            old = input('Informe a idade: ').strip()

            if not old.isnumeric():
                print('Erro!')
                continue
            return old
        
        except Exception:
            print('Erro! Algum dado não foi inserido corretamente...')
            continue

    