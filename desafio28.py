from random import randint
from time import sleep
c=randint(0,5) #Faz o computador pensa
print('-=-'*20)
print('Estou pensando em um numero entre 0 e 5...')
print('-=-'*20)
j=int(input('Em que numero eu pensei?'))  #faz o jogador advinhar
print('PROCESSANDO...')
sleep(2)
if j==c:
    print('PARABENS,Voce advinhou o numero{}!'.format(c))
else:
    print('INFELIZMENTE, você errou o numero é {}'.format(c))

    
