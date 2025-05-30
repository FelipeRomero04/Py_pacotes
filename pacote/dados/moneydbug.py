from decimal import Decimal

# def leia_dinheiro(msg):
#     p = input(msg)
#     try:
#         p = float(p)
#         return p
#     except Exception:
#         if ',' in p:
#             p_split= p.split(',')
#         for v in p_split:
#             if v.isnumeric:
#                 continue
#             '.'.join(p_split)
            
#         return float(p)
#         return f'Erro! O valor {p} é invalido, tente novamente.'

def leia_dinheiro(msg):
    try:
        p = float(input(msg))
        return p
    except ValueError:
        p = str(p)
        if ',' in p:
            p_split = p.split(',')
        for v in p_split:
            if v.isnumeric():
                continue
            else:
                return 'ERRO'
        p = '.'.join(p_split)
        return float(p)
    

def leia_dinheiro(msg):
    p = input(msg)

    if ',' in p:
        p_split = p.split(',')
    
        for v in p_split:
            if v.isnumeric:
                continue
            return 'ERRO'
        p = float('.'.join(p_split))
        return p
    try:
        return float(p)
    except ValueError:
        print(f'Erro! {p} não é um valor válido.')            






   


   #a virgula ja esta sendo trata em outro ponto, se tiver

   #splitar na virgula e usar isnumeric, caso seja falso, retornar msg de erro

#Quando da value erro nenhum valor e atribuido
                
            
    

    


