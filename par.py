
def evaluar_numero(numero):
    if numero   == 10:
     print("El numero es 10")
    elif numero == 7:
        print("se ha ingresado un comodin")
    elif numero % 2 == 0:   
        print("El numero es par")
    else:
        print("El numero es impar")
        
        
def main():
    # puedes cambiar este numero para probar
    numero = int(input("Ingrese un numero: ") )
    evaluar_numero(numero)
   
#Ejecutar la función principal 
if __name__ == "__main__":
    main()    
    
           