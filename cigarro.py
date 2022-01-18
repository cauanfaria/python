dia = int(input("quantos cigarros por dia?: "))
anos = int(input("fuma por quantos anos?: "))


cigarros = ((anos * 365) * dia) * 10
tempo = cigarros/1440


print(f"voce perdeu {tempo} dias de vida")