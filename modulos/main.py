import moeda

p = float(input('Digite o preço: '))

# print(f'O preco aumenta em 10%. fica {moeda.aumentar(p, 10, f=True)}')
# print(f'O preço diminuido em 10%. fica em {moeda.diminuir(p, 10, f=True)}')
# print(f'O dobro {moeda.dobro(p, f=True)}')
# print(f'Metade {moeda.metade(p, f=False)}')

moeda.resumo(p, 85, 30)