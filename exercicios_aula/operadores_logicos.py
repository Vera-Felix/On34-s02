# operador AND
and_operador = True and True #T+T = true
print(and_operador)

and_operador = True and False #T+F = false
print(and_operador)

and_operador = False and False #F+F = false
print(and_operador)

and_operador = (12==12) and (True)
print (and_operador)

and_operador = (13%2==0) and (False) and (44>23)
print(and_operador)

and_operador = (13%2==0) and (True) and (44>23)
print(and_operador)

# operador 
# == igual
or_operador = True or True
print(or_operador)

or_operador = True or False
print (or_operador)

or_operador = False or False
print(or_operador)

# se um for true no or ela considera true

or_operador = (12==12) or (True)
print (and_operador)

# operadorNOT
print(not True)
print(not False)

not_operador = (True and False) or (not (True and True))
# False or (not(True) = False or False = False
print(not_operador)