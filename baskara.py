import math
Va = int(input("Digite o valor de a:"))
Vb = int(input("Digite o valor de b:"))
Vc = int(input("Digite o valor de c:"))

def delt(a, b, c):
    return (b * b) - 4 * (a * c)

def bskr1(DELT, a, b):
     return -b + math.sqrt(DELT) / 2 * a

def bskr2(DELT, a, b):
     return -b - math.sqrt(DELT) / 2 * a
     
print(f"os resultados foram: {bskr1},{bskr2}")



DELT = delt(Va, Vb, Vc)
BSKR = bskr1(DELT, Va, Vb)
BSKR2 = bskr2(DELT, Va, Vb)
