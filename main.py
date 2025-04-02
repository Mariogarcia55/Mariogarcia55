x=4
while True:
    #"la pregunta en el bucle para quue se repita al momento de fallar"
    p=int(input("que numero crees que es "))
    if p==x:
       print("el numero el correcto") 
       break
    elif p>x:
        print("el numero es menor")
        
    elif p<x:
        print("el numero es mayor")
    elif p== "salir":
        break   
    else:
        print("vuelve a intentarlo")
        