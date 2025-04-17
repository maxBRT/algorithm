#!/usr/bin/env python3

"""
ENTRÉE: Base (entier), Nombre (chaîne de caractères)

SI Nombre contient '.' ALORS
    Séparer Nombre en PartieEntière et PartieFractionnaire au niveau du point décimal
SINON
    PartieEntière = Nombre
    PartieFractionnaire = chaîne vide
FIN SI

Convertir PartieEntière en une liste de caractères

SI Base égale 16 ALORS
    POUR chaque position dans PartieEntière
        SI le chiffre est A-F ALORS convertir en valeur décimale correspondante (10-15)
    FIN POUR
FIN SI

RésultatEntier = 0
POUR chaque chiffre de droite à gauche de PartieEntière (position = 0, 1, 2, ...)
    Vérifier que le chiffre < Base (sinon erreur)
    Valeur = chiffre * (Base ^ position)
    RésultatEntier = RésultatEntier + Valeur
FIN POUR

RésultatFractionnaire = 0
SI PartieFractionnaire n'est pas vide ALORS
    // Convertir PartieFractionnaire en une liste de chiffres individuels
    Convertir PartieFractionnaire en une liste de caractères

    SI Base égale 16 ALORS
        POUR chaque position dans PartieFractionnaire
            SI le chiffre est A-F ALORS convertir en valeur décimale correspondante (10-15)
        FIN POUR
    FIN SI

    POUR chaque chiffre de gauche à droite de PartieFractionnaire (position = 1, 2, 3, ...)
        Vérifier que le chiffre < Base (sinon erreur)
        Valeur = chiffre * (Base ^ -position)  // Noter l'exposant négatif
        RésultatFractionnaire = RésultatFractionnaire + Valeur
    FIN POUR
FIN SI

Résultat = RésultatEntier + RésultatFractionnaire

SORTIE: Résultat
"""

def hexa_to_decimal(Digit: str):
    if Digit.isdigit():
        return Digit
    elif Digit.upper() == 'A':
        return '10'
    elif Digit.upper() == 'B':
        return '11'
    elif Digit.upper() == 'C':
        return '12'
    elif Digit.upper() == 'D':
        return '13'
    elif Digit.upper() == 'E':
        return '14'
    elif Digit.upper() == 'F':
        return '15'

def welcome_message():
    print("Welcome to the base converter!")
    print("This program converts a number from a given base to decimal.")
    print("Make sure the digits of the number do not exceed the base.")
    print("Make sure to mark the decimal point with a dot (.) if needed.")
    print("Type 'exit' to quit the program.")

def convert_to_decimal(base: int, number) -> float:
    if '.' in number:
        integer_part, fractional_part = number.split('.')
    else:
        integer_part, fractional_part = number, ""

    integer_result = 0
    integer_part = list(integer_part)
    n = len(integer_part) - 1
    i = 0

    if base == 16:
      for x in range(len(integer_part)):
            integer_part[x] = hexa_to_decimal(integer_part[x])

    for _ in integer_part:
        if int(integer_part[n]) >= base:
            print(f"Error: Digit {integer_part[n]} exceeds the base {base}.")
            exit(1)
        integer_result += int(integer_part[n]) * (base ** i)
        n -= 1
        i += 1

    fractional_result = 0

    if fractional_part:
        fractional_part = list(fractional_part)

        if base == 16:
            for x in range(len(fractional_part)):
                fractional_part[x] = hexa_to_decimal(fractional_part[x])

        for i in range(len(fractional_part)):
            if int(fractional_part[i]) >= base:
                print(f"Error: Digit {fractional_part[i]} exceeds the base {base}.")
                exit(1)
            fractional_result += int(fractional_part[i]) * (base ** -(i+1))

    return integer_result + fractional_result

def get_input() -> tuple[int, str]:
    base = input("Enter the base: ")
    if base == "exit":
        exit(0)
    number = input("Enter the number: ")
    if number == "exit":
        exit(0)
    try:
        base = int(base)
    except ValueError:
        print("The base must be an integer.")
        exit(1)
    return base, number

welcome_message()
while True:
    base, number = get_input()
    result = convert_to_decimal(base, number)
    print("The result is: ", result)
