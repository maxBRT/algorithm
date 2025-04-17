#!/usr/bin/env python3

import math

""""
Fonction convertir_en_base(base, nombre):
    SI "." est dans le nombre :
        Séparer le nombre en partie_entière et partie_fractionnaire
    SINON :
        partie_entière = nombre
        partie_fractionnaire = ""

    Convertir partie_entière en entier
    Créer une liste vide nouvelle_base

    TANT QUE partie_entière > 0 :
        reste = partie_entière % base
        SI base == 16 ET reste >= 10 :
            Convertir reste en lettre hexadécimale (A-F)
        Ajouter reste au début de nouvelle_base
        partie_entière = partie_entière // base

    SI partie_fractionnaire n'est pas vide :
        Normaliser partie_fractionnaire en le divisant par 10^len(partie_fractionnaire)
        Ajouter "." à nouvelle_base
        Créer un ensemble vide liste_de_fractions
        POUR i de 0 à 10 :
            SI partie_fractionnaire est dans liste_de_fractions :
                Ajouter "..." à nouvelle_base et arrêter la boucle
            Ajouter partie_fractionnaire à liste_de_fractions
            partie_fractionnaire *= base
            partie_entiere = partie_fractionnaire (partie entière de la multiplication)
            partie_fractionnaire -= partie_entiere
            SI base == 16 ET partie_entiere >= 10 :
                Convertir partie_entiere en lettre hexadécimale (A-F)
            Ajouter partie_entiere à nouvelle_base

    Retourner nouvelle_base comme chaîne de caractères

"""

def welcome_message():
    print("Welcome to the base converter!")
    print("This program converts a decimal number to a given base to.")
    print("Make sure to mark the decimal point with a dot (.) if needed.")
    print("Type 'exit' to quit the program.")

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

def convert_to_base(base: int, number: str):
    if "." in number:
        integer_part, fractional_part = number.split('.')
    else:
        integer_part, fractional_part = number, ""

    integer_part = int(integer_part)
    quotient = None

    new_base = []

    while quotient != 0:
        quotient = math.floor((integer_part / base))
        result = integer_part - (quotient * base)
        if base == 16:
            if str(result).isdigit():
                result = result
            if result == 10:
                result = "A"
            elif result == 11:
                result = "B"
            elif result == 12:
                result = "C"
            elif result == 13:
                result = "D"
            elif result == 14:
                result = "E"
            elif result == 15:
                result = "F"
            else:
                if int(result) >= base:
                    print(f"Error: Digit {result} exceeds the base {base}.")
                    exit(1)

        new_base.insert(0, str(result))
        integer_part = quotient

    if fractional_part != "":
        fractional_part = float(fractional_part) / (10 ** len(fractional_part))
        new_base.append(".")
        quotient = None
        list_of_fractions = []
        i = 0

        while i < 10 and fractional_part not in list_of_fractions:
            list_of_fractions.append(fractional_part)
            quotient = fractional_part * base
            integer_part = int(quotient)
            fractional_part = quotient - integer_part
            if base == 16:
                if integer_part == 10:
                    integer_part = "A"
                elif integer_part == 11:
                    integer_part = "B"
                elif integer_part == 12:
                    integer_part = "C"
                elif integer_part == 13:
                    integer_part = "D"
                elif integer_part == 14:
                    integer_part = "E"
                elif integer_part == 15:
                    integer_part = "F"
                else:
                    if int(integer_part) >= base:
                        print(f"Error: Digit {integer_part} exceeds the base {base}.")
                        exit(1)

            new_base.append(str(integer_part))
            i += 1
        if fractional_part in list_of_fractions:
            new_base.append("...")


    return "".join(new_base)

welcome_message()
while True:
    base, number = get_input()
    if base < 2 or base > 16:
        print("The base must be between 2 and 16.")
        continue

    decimal_number = convert_to_base(base, number)
    print(f"The decimal equivalent of {number} in base {base} is {decimal_number}.")
