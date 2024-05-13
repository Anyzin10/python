n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
maior=max(n1,n2)
menor=min(n1,n2)
if n1==n2:
    print('Os números {} e {} são iguais.'.format(n1,n2))
else:
    print('O maior número é: {}'.format(maior))
    print('O menor número é: {}'.format(menor))
