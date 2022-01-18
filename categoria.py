categoria = int(input("digite a categoria: "))

if categoria == 1:
    categoria = "o preço é 10"
else:
    if categoria == 2:
        categoria = "o preço é 15"
    else:
        if categoria == 3:
            categoria = "o preço é 19"
        else:
            if categoria == 4:
                categoria = "o preço é 23"
            else:
                if categoria == 5:
                    categoria = "o preço é 27"
                else:
                    if categoria > 5:
                        categoria = "essa categoria não existe"

print(f"{categoria}")