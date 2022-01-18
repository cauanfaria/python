alt = (float(input("Digite sua altura: ")))
peso = (float(input("Digite seu peso: ")))

imc = peso / (alt * alt)

if imc < 18.5:
    print("Você esta abaixo do peso.")
else:
    if imc >= 18.5 and imc <= 24.9:
        print("Seu peso está normal.")
    else:
        if imc >= 25.0 and imc <= 29.9:
            print("Você esta sobrepeso.")
        else:
            if imc >= 30.0 and imc <= 34.9:
                print("Você esta obeso, grau I")
            else:
                if imc >= 35.0 and imc <= 39.9:
                    print("Você esta obeso, grau II")
                else:
                    if imc >= 40.0:
                        print("Você esta obeso, grau III")
            
