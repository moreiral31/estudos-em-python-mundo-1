v=int(input('Qual a distancia da viagem?'))
if v<=200:
    d=v*0.50
    print('Sua viagem é de {}Km'.format(v))
    print('E custará R${:.2f}'.format(d))
else:
    d=v*0.45
    print('Sua viagem é de {}Km'.format(v))
    print('E custará R${:.2f}'.format(d))
