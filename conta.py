num1 = (int(input("Digite o numero: ")))
print("digite um operador de acordo com os abaixo: ")
operador = (int(input("(1-adicao) (2-subtracao) (3- multiplicaçao) (4- divisao)")))
num2 = (int(input("digite o numero: ")))

if operador == 1:
    resultado = num1 + num2

elif operador == 2:
    resultado <= num1 - num2

elif operador == 3:
    resultado = num1 * num2

elif operador == 4:
    resultado = num1 / num2

print(f"o resultado ficou: {resultado}")
