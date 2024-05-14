letra = input("Digite uma letra: ")
vogais = "aeiou"
if letra.lower() in vogais:
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")