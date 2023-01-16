times = 'd','e','h','a','b','f','g','c','i','j','k',\
        'l','m','n','o','p','q','r','s','t'
print(f'os cinco primeiros colocados: {times[0:5]}')
print(f'os ultimos quatro colocados: {times[16:]}')
print(f'ordem alfabetica: {sorted(times)}')
print(f'o "b" esta na {times.index("b")+1}ª posiçao')