# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
# CODUL TĂU VINE MAI JOS:s
list_1 = [i for i in range(1,11)]
print(*list_1)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.
# CODUL TĂU VINE MAI JOS:
for i in list_1:
    if i % 2 == 0:
        print(f"Numerele pare sunt: {i}")
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.
# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.
# CODUL TĂU VINE MAI JOS:
per_dic = {
    'name':"Boris",
    'age': 300,
    'city':"Moscow"
}
for i in per_dic.items(): #Va avea tipul de tuplu
    print(i)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.
# CODUL TĂU VINE MAI JOS:
matrice_3x3 =[
    [1, 3, 5],
    [5, 8, 9],
    [1, 9, 4]
]
for i in matrice_3x3:
    print(*i)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.
# CODUL TĂU VINE MAI JOS:
gen_list = [i for i in range(1,21)]
for i in gen_list:
    print(i, end=' ')
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.
# CODUL TĂU VINE MAI JOS:
for count, value in enumerate(gen_list):
    print(f"{count}:{value}")
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.
# CODUL TĂU VINE MAI JOS:
print('-' * 60)
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
for number, letter in zip(numbers, letters):
    print(f"{number}:{letter}") 
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
# CODUL TĂU VINE MAI JOS:
print('-' * 60)
our_list = []
for i in range(1, 11):
    our_list.append(i)
print(*our_list)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.
# CODUL TĂU VINE MAI JOS:
print('-' * 60)
while our_list[0] <= 50:
    our_list = [x * 2 for x in our_list]
print(our_list)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].
# CODUL TĂU VINE MAI JOS:
import math  
print('-' * 60)
patrat_perfect = [x for x in range(1, 101) if math.isqrt(x) ** 2 == x] 
print(*patrat_perfect)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.
# CODUL TĂU VINE MAI JOS:
print('-' * 60)
for i in range(1, 11):
    print(f"{i} * 7 = {i * 7}")
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine.
# Dacă nu există, printează "Nu există valori mai mari decât 10".
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****
# CODUL TĂU VINE MAI JOS:
print()
user_input = int(input("Introduceti nr de *: "))
for i in range(user_input):
    for j in range(user_input):
        print("*",end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos
# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456
# CODUL TĂU VINE MAI JOS: 
for i in range(1,8):
    for j in range(1,i):
        print(j,end='')
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:
# 54321
# 5432
# 543
# 54
# 5
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Afișarea 3:
# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Afișarea 4:
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Afișarea 5:
# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
