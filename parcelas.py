preço = (float(input("Digite o preço do produto: ")))
parcela = (float(input("Digite a quantidade de parcelas: ")))

if parcela == 6:
    p = (preço/6) * 1.08
    print(f"seu preço vai ficar 6x de{p}")
else:
    if parcela == 12:
        p = (preço/12) * 1.14
        print(f"seu preço vai ficar 12x de{p}")
    else:
        if parcela == 24:
            p = (preço/24) * 1.23
            print(f"seu preço vai ficar 24x de{p}")
        else:
            if parcela == 36:
                p = (preço/36) * 1.38
                print(f"seu preço vai ficar 36x de{p}")
            else:
                print("essa parcela é invalida")
