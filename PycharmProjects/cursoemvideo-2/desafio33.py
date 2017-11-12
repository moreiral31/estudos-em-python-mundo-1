a=int(input('PRIMEIRO numero:'))
b=int(input('SEGUNDO numero:'))
c=int(input('TERCEIRO numero:'))
#Verificando menor
m=a
if b<a and b<c:
    m=b
if c<a and c<b:
    m=c
#verficand maior
n=a
if b>a and b>c:
    n=b
if c>a and c>b:
    n=c
print('O menor valor digitado foi:{}'. format(m))
print('O maior valor digitado foi:{}'.format(n))

