# -*- coding: utf-8 -*-
tall=1
n=int(input("Skriv heltallet du vil ta fakulteten til. Tallet må være større eller lik null!"))

if n<0:
    print("Tallet må være ett heltall over null!")


    
else: 
    for x in range(n):
        tall=tall*(x+1)
    print(tall)


