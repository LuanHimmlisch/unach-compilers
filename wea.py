import re


entrada = input("Metemela: ")

exito = re.match(r"^a*(b|c)*$", entrada)

if (exito):
    print("Wenas shabal")
else:
    print("Oh no! Sos lince")