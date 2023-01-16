from math import sqrt

co=float(input('digite o cateto oposto:'))
ca=float(input('digite o cateto adjacente:'))
hip=(co**2+ca**2)
print('{}²+{}²={:.2f}²'.format(co,ca,sqrt(hip)))
print('hipotenusa:{:.2f}'.format(hip))

