'''import random
nome=[]
nome.append(input('Digite o nome do primiero aluno:'))
nome.append(input('Digite o nome do segundo aluno:'))
nome.append(input('Digite o nome do terceiro aluno:'))
nome.append(input('Digite o nome do quarto aluno:'))
print('O Aluno escolhido foi:',random.choice(nome))
print(nome) '''

import random
n1=(input('Primeiro aluno:'))
n2=(input('Segundo aluno:'))
n3=(input('Terceiro aluno:'))
n4=(input('Quarto aluno:'))
lista=[n1,n2,n3,n4]
e=random.choice(lista)
print('O aluno escolhido foi:{}'.format(e))