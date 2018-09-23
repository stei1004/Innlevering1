# -*- coding: utf-8 -*-
import math
v = input("Vil du regne ut energien,E, massen, M, eller farten, V.")

if v==("E"): 
    b=int(input("Skriv inn legemets masse."))
    c=int(input("Skriv inn legemets fart."))
    E=(1/2)*b*(c**2)
    print("Legemets kinetiske energi er", E, "joule.")

elif v==("M"): 
    E=int(input("Skriv inn legemets kinetiske energi."))
    c=int(input("Skriv inn legemets fart."))
    b=(2*E)/c**2
    print("Legemets masse er" ,b, "kg.")
    
else: 
    b=int(input("Skriv inn legemets masse."))
    E=int(input("Skriv inn legemets kinetiske energi."))
    c= math.sqrt((2*E)/b)
    print("Legemets masse er", c, "m/s.")

   