#FuncionesyMatrices
def sumar_filas(matriz):
    return [sum(fila) for fila in matriz]

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("matriz")
    for fila in matriz:
        print(fila)

    resultado = sumar_filas(matriz)
    print("La suma de cada fila es:",resultado)
    
if __name__ == "__main__":
    main()