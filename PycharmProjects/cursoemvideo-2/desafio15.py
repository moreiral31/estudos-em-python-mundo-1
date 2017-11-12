d=int(input('Quantos dias alugado?'))
k=float(input('Quantos Km rodados?'))
n1=(d*60)+(k*0.15)
print('total a pagar: R${:.2f}'.format(n1))