tipos_de_pessoas = 10 #variavel tipos_de_pessoas recebendo valor 10
x = f"Existe {tipos_de_pessoas} tipos de pessoas." #variavel x recebendo uma string com o formato "f_string" (deixa colocar um valor na string)
binario = "binario" #variavel binario recebendo um valor. esse valor é do tipo string pq está entre " "
nao = "não" #variavel nao recebendo um valor. esse valor é do tipo string pq está entre " "
y = f"Aquelas que sabem {binario} e aquelas que {nao}." #variavel y recebendo uma string com o formato "f_string"

print(x) #printando as variaveis
print(y)

print(f"Eu disse: {x}") #printando as variaveis com o formato f_string
print(f"Eu também disse: {y}")

hilario = False #variavel hilario recebendo o valor boleano falso
avaliacao_piada = "Essa piada foi muito engraçada?!{}" ##variavel recebendo um valor string

print(avaliacao_piada.format(hilario)) #printando a variavel avaliacao_piada com o formato .format juntado o valor da variavel hilario

w = "Esse é o lado esquerdo de..." #variavel do w recebendo um valor string
e = "uma string com seu lado direito" #variavel do e recebendo um valor string

print(w + e) #printando as duas variaveis juntas,
