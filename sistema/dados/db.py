from ..utils import util

def options(op, name='User', old='0'):

    if op == '1':
        def register(): 
          
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


