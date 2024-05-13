n1=float(input('Digite um número: '))
n2=float(input('Digite um segundo número: '))
n3=float(input('Digite um terceiro número: '))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('É possível fazer um triângulo.')
else:
    print('Não é possível fazer um triângulo.')
