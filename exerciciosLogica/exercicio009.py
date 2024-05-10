n1=float(input('Digite um número: '))
n2=float(input('Digite um segundo número: '))
n3=float(input('Digite um terceiro número: '))
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    if n1==n2==n3:
        print('O triângulo é equilátero.')
    elif n1==n2 or n1==n3 or n2==n3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os valores não formam um triângulo.')
