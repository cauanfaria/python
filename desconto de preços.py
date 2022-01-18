preço = float(input("digite o preço: "))
desconto = float(input("digite a porcentagem do desconto sem usar %: "))


valor= preço * (desconto/100)

descontão = preço - valor


print(f"o desconto foi{descontão} reais e o valor ficou {valor}")