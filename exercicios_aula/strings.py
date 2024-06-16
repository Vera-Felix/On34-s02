nome = "Carla"
sobrenome = "dos Santos"
print(nome+" "+sobrenome)

conteudo = "Meu ano do nascimento é " + str (1969) # str converte para string
print(conteudo)

salario = input ('Digite  seu salario:')
salario = int (salario)
salario_ano = salario*12
print(salario_ano)

valor = 5
print (float(valor))

print (bool(0)) #false
print (bool(1)) #true
print(bool("conteudo")) #true
print(bool("")) #false

# um numero, outro numero. soma, multiplica, divide

# segundo
#usuario digita um valor
# você retorna se é par ou impar
numero = float(input("Digite um numero: "))
eh_impar = numero%2
eh_impar = bool (eh_impar)
print ("O numero", numero,"é impar?", bool (eh_impar))


