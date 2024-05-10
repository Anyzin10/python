n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite um terceiro número: '))
if n1>n2>n3:
    print('O maior número é: ',n1)
elif n2>n3>n1:
    print('O maior número é: ',n2)
else:
    print('O maior número é: ',n3)
