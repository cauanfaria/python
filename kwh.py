kwh = (int(input("quantos de kwh foram consumidos: ")))
print("digite sua instalação de acordo com os numeros abaixo")
instalacao = (int(input("1-Residencial 2-industrial 3-comercio: ")))

if instalacao == 1 and kwh < 500:
    preço = kwh * 0.40
if instalacao == 1 and kwh > 500:
    preço = kwh * 0.65

if instalacao == 2 and kwh < 5000:
    preço = kwh * 0.55
if instalacao == 2 and kwh > 5000:
    preço = kwh * 0.60

if instalacao == 3 and kwh < 1000:
    preço = kwh * 0.55
if instalacao == 3 and kwh > 1000:
    preço = kwh * 0.60

print(f"o preço ficou {preço} reais")
