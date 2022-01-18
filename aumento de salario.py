salario = float(input("Digite o salario: "))
aumento = float(input("digite a porcentagem de aumento sem usar %: "))


valor = salario * (1+(aumento/100))
aumento = valor - salario


print(f"o salario aumentou em {aumento} reais e ficou {valor}")