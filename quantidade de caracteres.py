def qtde(n):
    s = str(n)
    return len(s)

def menu():
    numero = int(input("Digite um numero qualquer: "))
    resultado = qtde(numero)
    print(f"A quantidade de caracteres é: {resultado}")

menu()