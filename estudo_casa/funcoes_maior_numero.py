def maior_num(lista_num):
    lista_num.sort() #ordena
    lista_num.reverse() #
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([6288,554,-2,890,10])
print(resultado)