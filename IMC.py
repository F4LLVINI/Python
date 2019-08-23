pso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))
imc = pso/(alt*2)


print("Seu IMC é {:.2f}".format(imc))

if imc < 18.5:
    print("Magreza")
elif imc < 24.9:
    print("Saudavel")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 39.9:
    print("Obesidade")
else:
    print("Obesidade grave")
