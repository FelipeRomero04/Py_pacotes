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


    if op == '2':
        def show_users():
            with open('usuarios.txt', 'r', encoding='utf-8') as r:
                read_file = r.read()

            util.effect('PESSOAS CADASTRADAS')
            print(read_file)
        return show_users()
    
    if op == '3':
        def exit_sistem():
            print('Saindo do sistema...\nAté mais!')
            
        return exit_sistem()



#função pra limpar a lista e escrever outra
            


