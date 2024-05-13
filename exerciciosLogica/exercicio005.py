A = int(input('Digite o primeiro número (A): '))
B = int(input('Digite o segundo número (B): '))
if A % B == 0:
    print('{} é divisível por {}.'.format(A,B))
else:
    print('{} não é divisível por {}.'.format(A,B))