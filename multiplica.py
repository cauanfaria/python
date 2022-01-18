primeiro = (int(input("digite o primeiro; ")))
segundo = (int(input("Digite o segundo: ")))

resultado = primeiro / segundo

num = primeiro

while num >= 0:
    print(f"{num}")
    num = num - segundo
print(f'resultado da multiplicação é {resultado}')