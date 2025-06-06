def effect(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)



def menu():
   
    effect('MENU PRINCIPAL')

    print('''1 - Ver pessoas cadastradas
        2 - Cadastrar nova usuário
        3 - Deletar usuário
        3 - Sair do Sistema''')
    
    option = input('Sua opção: ')
    return option