from sistema.utils import util

def register():
    nome = input('Informe nome: ')
    idade = input('Informe idade: ')

    with open('usuarios.txt', 'a+', encoding='utf-8') as f:
        f.writelines(f'{nome:<20} {idade}\n')



def show_users():
    with open('usuarios.txt', 'r', encoding='utf-8') as r:
        read_file = r.read()

    util.effect('PESSOAS CADASTRADAS')
    print(read_file)


'''Resolver problema de modulenotfound'''


show_users()

