def somaImposto(taxaimposto, custo):
    return (0.01*taxaimposto) * custo

def menu():
    taxa = float(input("Digite um percentual de imposto: "))
    custo = float(input("Digite o valor do custo: "))
    resultado = somaImposto(taxa, custo)
    print(f"O valor do imposto é: {resultado}")

menu()