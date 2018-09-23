# -*- coding: utf-8 -*-
import math 
a=float( input("Skriv inn antall H^+ - ioner i løsningen. 10^-3 må skrives som 1e-3 osv."))
pH = -math.log10(a)

print("Løsningens pH verdi er", pH,".")

if 0<=pH<7: 
    print("Løsningen er sur.")
    
elif pH==7: 
    print("Løsningen er nøytral.")
    
else: 
    print("Løsningen er basisk.")