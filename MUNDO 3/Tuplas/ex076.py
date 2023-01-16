produtos = ('a',22.00,
            'b',10.50,
            'c',2,
            'd',6.50)
for pos in range (0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<20}',end='')
    else:
        print(f'R${produtos[pos]:>6.2f}')