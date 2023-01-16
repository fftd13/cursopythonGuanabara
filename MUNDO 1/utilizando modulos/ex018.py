import math

ang=float(input('digite o ângulo:'))
sen=math.sin(math.radians(ang))
print('o seno de {}º é: {:.2f}'.format(ang,sen))
cos=math.cos(math.radians(ang))
print('o cosseno de {}º é: {:.2f}'.format(ang,cos))
tan=math.tan(math.radians(ang))
print('a tangente de {}º é: {:.2f}'.format(ang,tan))
