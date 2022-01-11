
lista = []

#Twory liste 0-10
for i in range(10):
    lista.append(i)

#Szuka liczb 3 i 5 w liscie, nastepnie je usuwa.
for l in lista:
    if l == 3 or l == 5:
        lista.remove(l)

#Usuwa liczby 8 ,9 a nastepnie dodaje je jako string.
for a in lista:
    if a == 8:
        lista.remove(a)
for b in lista:
    if b == 9:
        lista.remove(b)

lista.append("8")
lista.append("9")

# Wersja "reczna"
#lista[6] = "8"
#lista[7] = "9"
    
print (lista)  
