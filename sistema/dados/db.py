def sing_in(nome, idade):
    with open('text.txt', 'w', 'UTF-8'):
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')
