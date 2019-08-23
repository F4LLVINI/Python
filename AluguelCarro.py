Km=float(input('Quantos Kilometros você percorreu com o carro? KM'))
Di=int(input('Quantos dias você ficou com o carro? '))
v=(Km*0.15)+(Di*60)

print('O valor do aluguel é de: R${:.2f}'.format(v))
