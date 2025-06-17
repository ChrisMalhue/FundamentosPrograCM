#FuncionyLista(PromedioNotas)

def main():
    lista_notas = [7, 4, 6, 6.5, 4.8]
    promedio = promedio_notas(lista_notas)
    print("Las notas ingresadas son:", lista_notas)
    print("El promediod de las notas es:", round(promedio, 2))

def promedio_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)

if __name__ == "__main__":
    main()
