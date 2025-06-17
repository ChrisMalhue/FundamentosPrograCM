#FuncinesyTuplas
def mayor_y_menor(tupla):
    return (max(tupla), min(tupla))

def main():
    tupla = (7, 5, 3, 9, 8, 10, 1, 4, 6, 2)
    print(tupla)
    mayor_menor = mayor_y_menor(tupla)
    print("El numero mayor y el numero menot de la tupla es:", mayor_menor)
    
if __name__ == "__main__":
    main()