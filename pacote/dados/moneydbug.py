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
    p = float(input(msg))

    if ValueError:
        p = str(p).strip
    if ',' in p:
        p_split = p.split(',')
        for v in p_split:
            if v.isnumeric():
                continue
        p = '.'.join(p_split)
        return float(p)
                






   


   #a virgula ja esta sendo trata em outro ponto, se tiver

   #splitar na virgula e usar isnumeric, caso seja falso, retornar msg de erro

#Quando da value erro nenhum valor e atribuido
                
            
    

    


