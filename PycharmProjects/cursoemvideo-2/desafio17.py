'''c1=float(input('Informe o cateto oposto:'))
c2=float(input('Informe o cateto adjacente:'))
n=(c1**2 + c2**2)**(1/2)
print('A hipotenusa é:{:2f}'.format(n))'''

import math
c1=float(input('Informe o cateto oposto:'))
c2=float(input('Informe o cateto adjacente:'))
n=math.hypot(c1,c2)
print('A hipotenusa é:{:.2f}'.format(n))