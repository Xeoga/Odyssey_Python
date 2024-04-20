# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.
# CODUL TĂU VINE MAI JOS:
number = 7
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if number >= 0:
    print(f"Numarul este pozitiv")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if number >=0 and number % 2 ==0:
    print(f"Numarul este pozitiv si par:)")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if not (number % 2 == 0): #Metoda (number % 2 != 00) 
    print(f"Numar impar")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.
# CODUL TĂU VINE MAI JOS:
un_sir_de_caractere = 'This_is_my_string_in_Python'
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if 'Python' in un_sir_de_caractere:
    print(f"Cuvantul Python in sirul {un_sir_de_caractere}")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if 'Java' in un_sir_de_caractere:
    print(f"Cuvantul Python in sirul {un_sir_de_caractere}")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if 'Java' in un_sir_de_caractere:
    print(f"Cuvantul Python in sirul {un_sir_de_caractere}")
elif 'Python' in un_sir_de_caractere:
    print(f"Cuvantul Python in sirul {un_sir_de_caractere}")
else:
    print("Nici un cuvant nu a fost gasit :(")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
# CODUL TĂU VINE MAI JOS:
if 'Python' in un_sir_de_caractere and 'Java' in un_sir_de_caractere:
    print(f"In '{un_sir_de_caractere}' sunt gasite ambele cuvint(Python, Java):")
elif 'Python' in un_sir_de_caractere:
    print(f"Cuvantul Python in sirul {un_sir_de_caractere}")
elif 'Java' in un_sir_de_caractere:
    print(f"Cuvantul Java in sirul {un_sir_de_caractere}")
else:
    print("Nici un cuvant nu a fost gasit :( .")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"
# CODUL TĂU VINE MAI JOS:
number = int(input("Introduceti un numar de la 1-5:  "))
if number == 1:
    print("Unu")
elif number == 2:
    print("Doi")
elif number == 3:
    print("Trei")
elif number == 4:
    print("Patru")
elif number == 5:
    print("Cinci")
else:
    print("Optiune invalida")
    # Afigeti in python nui goto(77) de ce ? A am gasit pentru ca sa fie mai clar codul SAD :(

# CODUL TĂU VINE MAI SUS: