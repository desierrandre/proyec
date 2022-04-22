import re
# GLOBAL VARIABLES
FILE_LIST = []

def read_file(name_file: str, mode="r"):
    file = open(name_file, mode)
    for line in file:
        FILE_LIST.append(re.sub("\\n", "",line))
    file.close()

def find_name_product(nameProduct: str) -> str:
    indexNameProduct = FILE_LIST.index(nameProduct)
    indexUnitProduct = indexNameProduct + 2
    return FILE_LIST[indexUnitProduct]

def add_product(productsAddedN: int, file):
    for i in range(0, productsAddedN):
        idProduct = int(input("Escriba el codigo del producto: "))
        nameProduct = input("Escriba el nombre del producto: ")
        unitProduct = input("Escriba la unidad de medida del producto: ")
        priceProduct = int(input("Escriba el precio del producto: "))
        stockProduct = int(input("Escriba la cantidad de ese producto que hay: "))
        file.write(
            f"{str(idProduct)}\n{nameProduct}\n{unitProduct}\n{str(priceProduct)}\n{str(stockProduct)}\n"
        )
    file.close()

def delete_product(idProduct: int, file):
    indexIdProduct = FILE_LIST.index(str(idProduct))
    for index in range(indexIdProduct, indexIdProduct+5):
        FILE_LIST.pop(indexIdProduct)
    for line in FILE_LIST:
        file.write(f"{line}\n")
    file.close()

if __name__ == '__main__':
    productsAddedN = int(input("Escriba la cantidad de productos que desea ingresar: "))
    fileInventary=open("./inventario.txt", "w")
    add_product(productsAddedN, fileInventary)
    read_file("./inventario.txt", "r")
    print("\n Menu")
    print(" 1- Buscar la unidad de medida de  un producto")
    print(" 2- Añadir nuevo producto  ")
    print(" 3- Eliminar un producto ")
    print(" 4- Imprimir lista de productos en el inventario")
    print(" 5- Buscar productos ")
    optionMenu = int(input("Escriba el número de la acción de desea realizar: "))
    if optionMenu == 1:
        nameProduct = input("Escriba el nombre del producto al cual le quiere saber su medida: ")
        print(find_name_product(nameProduct))
    if optionMenu == 3:
        idProduct = int(input("Escriba el código del producto que quiere eliminar"))
        fileInventary = open("./inventario.txt", "w")
        delete_product(idProduct, fileInventary)

