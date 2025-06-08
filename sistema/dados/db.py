from ..utils import util

def options(op, n, o):

    if op == '1':
        def register(): 

            name = n() #função nome debugada
            old = o()  #função idade debugada
          
            with open('usuarios.txt', 'a+', encoding='utf-8') as f:
                f.writelines(f'{name:<20} {old} anos\n')

            print(f'Novo registro de "{name}" adicionado.')
        return register()


    elif op == '2':
        def show_users():
            with open('usuarios.txt', 'r', encoding='utf-8') as r:
                read_file = r.read()

            util.effect('PESSOAS CADASTRADAS')
            print(read_file)
        return show_users()
    
    elif op == '3':
        def clean_list():
            name = n()
            old = o()

            with open('usuarios.txt', 'w+', encoding='utf-8') as c:
                c.writelines(f'{name:<20} {old} anos\n')

            print('Uma nova lista, com nome e idade informados foi criada!')
        return clean_list()



    elif op == '4':
        def exit_sistem():
            print('\nSaindo do sistema...\nAté mais!')
            
        return exit_sistem()


    





#Puxar name e idade novamentes e passa como parametro para register chamando ela, fazendo a atribuição a lista de forma permanente
#função pra limpar a lista e escrever outra
            


