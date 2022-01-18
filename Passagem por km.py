km = (int(input("Escreva a kilometragem: ")))

if km < 200:
    preço = km * 0.50 

if km > 200:
    preço = km * 0.45

print(f"o preço da sua passagem ficou {preço} reais")