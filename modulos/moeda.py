def aumentar(preco, porcent, f=True):
    more = preco + (preco * porcent / 100)

    if f:
        return (f'${more}')
    return more

def diminuir(preco, porcent, f=True):
    less = preco - (preco * porcent / 100)
    if f:
        return (f'${less}')
    return less

def dobro(preco, f=True):
    double = preco * 2

    if f:
        return(f'${double}')
    return double

def metade(preco, f=True):
    half = preco / 2

    if f:
        return (f'${half}')
    return half


def resumo(p, porc_more, porc_less, f=True):
    list = [
        ('Preco Analisado:', p), 
        ('Dobro do preco', dobro(p)), 
        ('Metade do preco', metade(p)), 
        (f'{porc_more}', aumentar(p, porc_more)), 
        (f'{porc_less}', diminuir(p, porc_less))
        ]

    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)

    print('-' * 30)
    for k, v in list:
        print(f'{k:<20} {v}')
    print('-' * 30)
    

