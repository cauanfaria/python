salario = (int(input("Digite o salario: ")))
mes = (int(input("digite a quantidade de meses: ")))
valor = (int(input("valor da casa: ")))

prestação = valor / mes
salariocom30 = (salario * 0.30) + salario
diferenca = prestação - salariocom30
valorreal = prestação - diferenca 

if prestação > salariocom30:
    print(f"sua prestação é {valorreal}")

if prestação < salariocom30:
    print(f"sua prestação é {prestação}")
    
