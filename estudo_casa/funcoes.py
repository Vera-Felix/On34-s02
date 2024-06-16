# 1a. função:
"""""
def big_mac():
    print("Sanduiche Big Mac")

print ("Início")
big_mac()
print ("Fim")
"""""
# 2a.  função:
"""""
def fazer_big_mac(nome):
    print(f"Sanduiche Big {nome}")

fazer_big_mac("Roger")
fazer_big_mac("Luis")
fazer_big_mac("André")
"""""
# 3a.  função:
def fazer_big_mac(nome):
    print(f"Sanduiche Big {nome}")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}")

"""""
fazer_big_mac("Roger")
fazer_batata("Grande")
preparar_refrigerante("Coca","Média")
"""
def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)

fazer_combo_big_mac("Roger","GRande","Coca","Média")


