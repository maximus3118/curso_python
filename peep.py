
class Numero:
    def __init__(self, Numero):
        self.Numero = Numero

    def EvaluarNumero(self):
        if self.Numero & 1 :
            print("El numero es impar")
            if self.Numero == 7:
                print("\nEl numero ingresado es un comodin")
        else:
            print("par")
            if self.Numero == 10:
                print("\nEl numero ingresado es 10")
    def sumar(self,numerosumar):
        return self.Numero +  numerosumar

if __name__ == "__main__":
    numeroevaluar= Numero(int(input("Ingrese un numero: ")))
    numeroevaluar.EvaluarNumero()  
    sumarealizada = numeroevaluar.sumar(8)
    print("\nLa suma realizada es: ",sumarealizada)

        
        
