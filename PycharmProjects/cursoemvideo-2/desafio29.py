v=float(input('Qual a velocidae atual do carro?'))
if v>80:
    m=(v-80)*7
    print('Voce excedeu o limida de 80Km/h')
    print('Pague a multa de: R${:.2f}'.format(m))
print('Tenha um bom dia e diriga com seguraça!')