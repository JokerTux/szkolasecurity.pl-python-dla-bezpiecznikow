'''
Praca domowa

Stwórz skrypt, który:
1. Tworzy listę liczb od 0 do 9 (pętla for)
2. Iteruje po tej liście pętlą for lub while i wypisuje jej zawartość
3. Usuwa liczby 3 i 5 z listy [ list.remove() ]
3. Zamienia liczby 8 i 9 na stringi (list.remove() lub list.pop() i list.append(), bądź zwykłe przypisanie list[8] = '8′
Lista po tych przekształceniach powinna wyglądać tak: [0, 1, 2, 4, 6, 7, '8′, '9′]
'''

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
        lista.append("8")
for b in lista:
    if b == 9:
        lista.remove(b)
        lista.append("9")

# Wersja "reczna"
#lista[6] = "8"
#lista[7] = "9"
    
print (lista)  
