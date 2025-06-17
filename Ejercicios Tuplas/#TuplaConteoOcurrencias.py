#TuplaConteoOcurrencias

def main():
    lista_palabras = ["hola", "hola", "hola", "uno", "dos", "tres"]
    resultado = contar_ocurrencias(lista_palabras)
    print(f"El numero de palabras dentro de la lista es: {resultado}")

def contar_ocurrencias(lista_palabras):
    conteo = {}
    for palabra in lista_palabras:
        conteo[palabra] = conteo.get(palabra , 0) + 1
    return conteo

if __name__ == "__main__":
    main()