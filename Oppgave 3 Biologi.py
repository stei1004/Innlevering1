# -*- coding: utf-8 -*-
b=int(input("Skriv inn den nåværende populasjonen."))
p=int(input("Skriv inn den årlige prosentvise endringen i populasjonen."))
t=int(input("Skriv inn i hvor mange år frem i tid du vil regne populasjonen."))


d=input("Ønsker du å se dyrene år for år? Skriv JA eller NEI.")
if d==("JA"):
    for x in range(0,t+1): 
        c=b*((1+(p/100))**x)
        print("Populasjonen etter", x, "år, er" , c," dyr.")
        
elif d==("NEI"): 
    c=b*((1+(p/100))**t)
    print("Populasjonen etter" , t, "år er", c, "dyr.")
    
    
    