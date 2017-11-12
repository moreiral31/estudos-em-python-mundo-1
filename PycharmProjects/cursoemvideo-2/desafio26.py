f=str(input('Digite uma frase:')).upper().strip()
print('Sua frase tem {}, "A"'.format(f.count('A')))
print('A primera letra A aparece na posição:{}'. format(f.find('A')))
print('A ultima letra A aparece na posição:{}'.format(f.rfind('A')))