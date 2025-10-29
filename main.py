sirul_de_caractere = "Exemplu de sir de caractere"
print(sirul_de_caractere[0])
for caracter in sirul_de_caractere:
    print(caracter)
for i in range(len(sirul_de_caractere)):
    print(sirul_de_caractere[i])

print("---------------------"   )
# LISTE
lista_de_numere = [10, 20, 30, 40, 50]
lista_diversa = [1, 'text', 3.14]

# nu am mai reusit sa pun codul pe care la dictat--bag piciorul --

# continua dupa mult cod scris cu cautarea elementlor in lista
# indexD
# element
lista= [10, 20, 30, 40, 50]
index_element = lista.index(8)
print(index_element)


# count- numaram elementele
# parcurgerea elementelor dintr-o lista
print("---------------------")
lista=[10, 20, 30, 40, 50]
for element in lista:
    print(element)

# afisarea elementelor pare
for element in lista:
    if element %2 == 0:
        print(element)

# parcurgerea cu index
# for index in range (len(lista)):
# pozitia elementului la care suntem: index
# valoarea elementului : lista[index]
print("----------------------")
lista=[101, 220, 301, 40, 50]
for index in range(len(lista)):
    print(lista[index])

# afisati numerele pare de pe pozitiile divizibile cu 3
for index in range(len(lista)):
    # pozitia e index
    # valoare e lista(index)
    if lista[index]%2 == 0 and index % 3 == 0:
        print(lista[index])
# parcurgere cu while
# parcurgem cat timp avem elemente in lista sau pana e indeploinita o conditie
# parcurgere tot pe index , cresterea indexului la finalul fiecarui pas
lista = [10, 20, 30, "stop" 40, 50]
index = 0
while index < len(lista) and lista [index] ! == "stop":
    print(lista[index])
    index += 1
