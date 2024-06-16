def calculo_imc(altura, peso):
    imc = peso/(altura**2)
    print(imc)

    print (calculo_imc(1.61,62))

def calculo_imc_retorno (altura, peso):
    imc = peso/altura**2
    return imc

retorno_funcao = calculo_imc(1.60, 40)
print(retorno_funcao)

retorno_funcao = calculo_imc_retorno(1.60, 40)
print(retorno_funcao)

