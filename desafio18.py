from math import sin,cos,tan, radians
a=float(input('Digite o angulo desejado:'))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('O angulo {} tem o SENO de:{:.2f}'.format(a,s))
print('O angulo {} tem o COSSENO de:{:.2f}'.format(a,c))
print('O angilo {} tem a TAGENTE de: {:.2f}'.format(a,t))