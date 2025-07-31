def pedir_calificaiones():
    calificaciones = []
    cantidad = int(input("¿Cuantas calificaciones vas a ingresar? ") )
    
    for i in range(cantidad):
       nota = float(input(f"Ingrese la calificacion #{i+1}") )
       while nota < 0 or nota > 10:
           print("La calificacion debe estar entre 0 a 5")
           nota = float(input(f"Ingrese la calificacion #{i+1}") )
    calificaciones.append(nota)
    return calificaciones
    
def calcular_promedio (calificaciones):
      return sum(calificaciones) / len(calificaciones)
def mostrar_resultados(promedio):
    print(f"promedio final: {promedio:.2f}")
    if promedio >= 3.0:
        print("!aprobaste!disfruta tus vacaciones")
    else:
        print("No aprobaste. !animos tu puedes!")

def main():
      print("=== Calculadora de promedios ===")
      calificaciones = pedir_calificaiones()
      promedio = calcular_promedio(calificaciones)
      mostrar_resultados(promedio)
      
if __name__ == "__main__":
        main()
    
