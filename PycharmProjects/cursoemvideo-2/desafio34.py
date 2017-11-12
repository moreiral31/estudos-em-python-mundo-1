s=float(input('Digite seu Salario:R$'))
if s>1250:
    a=s*0.1
    t=s+a
    print('Seu aumento foi de:{:.2f}'.format(a))
    print('Seu salario foi para:R${:.2f}'.format(t))
if s<=1250:
    a=s*0.15
    t=s+a
    print('Seu aumento foi de:{:.2f}'.format(a))
    print('Seu salario foi para:R${:.2f}'.format(t))



