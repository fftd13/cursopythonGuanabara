from random import randint
from time import sleep

print('-=-'*16)
print('vou pensar em um numero de 0 a 5 tente advinhar')
print('-=-'*16)
num = int(input('em que numero eu pensei?:'))
rc = randint (0,5)
print('processandinho...')
sleep(3)
if num == rc:
    print('parabens,voce acertou,eu pensei no numero {}'.format(rc))
else:
    print('eu pensei no numero {},e nao no numero {}'.format(rc,num))