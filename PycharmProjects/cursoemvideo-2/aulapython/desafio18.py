from math import radians, sin, cos,tan
a=float(input('Digite o angulo desejado:'))
s= sin(radians(a))
c= cos(radians(a))
t= tan(radians(a))
print('O angulo {} tem o SENO de:{:.2f}'. format(a,s))
print('O angulo {} tem o COSSENO de:{:.2f}'.format(a,c))
print('O angulo {} tem a TANGENTE de:{:.2f}'. format(a,t))
