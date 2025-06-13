def suma(valor1, valor2):
    total = valor1 + valor2
    return total
def resta(valor1, valor2):
    total = valor1 - valor2
    return total
def division(valor1, valor2):
    total = valor1 / valor2
    return total
def multiplicacion(valor1, valor2):
    total = valor1 * valor2
    return total

def main():
    while True:
        try:
            print("Opcion 1 Sumar\nOpcion 2 Restar\nOpcion 3 Multiplicar\nOpcion 4 Dividir\nOpcion 5 Salir\n(Tenga en cuenta que esta calculadora funciona solo con 2 valores)")
            opcion1 = int(input("Ingrese la opcion que desea realizar: "))
            valor1 = int(input("Ingrese el Valor 1: "))
            valor2 = int(input("Ingrese el Valor 2: "))
        except ValueError:
            print("Ingrese un valor dentro de las opciones")
            continue
        if opcion1 == 1:
            suma2 = suma(valor1, valor2)
            print(f"Su total es: {suma2}")
        elif opcion1 == 2:
            resta2 = resta(valor1, valor2)
            print(f"Su total es: {resta2}")
        elif opcion1 == 3:
            multiplicacion2 = multiplicacion(valor1, valor2)
            print(f"Su total es: {multiplicacion2}")
        elif opcion1 == 4:
            divison2 = division(valor1, valor2)
            print(f"Su total es: {divison2}")
        elif opcion1 == 5:
            print("Saliendo del programa...")
            break
if __name__ == "__main__":
    main()

            
            
            
