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

def add_product(productsAddedN: int) -> bool:
    for i in range(0, productsAddedN):
        indexProducts = []
        fileAdded = open("./inventario.txt", "a")
        idProduct = int(input("Escriba el codigo del producto: "))
        for indexIdProduct in range(0, len(FILE_LIST), 5):
            indexProducts.append(FILE_LIST[indexIdProduct])
        for indexIdProduct in range(0, len(FILE_LIST), 5):
            if str(idProduct) in indexProducts:
                print("Ya existe este id")
                return 1
        nameProduct = input("Escriba el nombre del producto: ")
        unitProduct = input("Escriba la unidad de medida del producto: ")
        priceProduct = int(input("Escriba el precio del producto: "))
        stockProduct = int(input("Escriba la cantidad de ese producto que hay: "))
        fileAdded.write(
            f"{str(idProduct)}\n{nameProduct}\n{unitProduct}\n{str(priceProduct)}\n{str(stockProduct)}\n"
        )
        fileAdded.close()
        read_file("./inventario.txt", "r")
    return True 

def delete_product(idProduct: int, file):
    indexIdProduct = FILE_LIST.index(str(idProduct))
    for index in range(indexIdProduct, indexIdProduct+5):
        FILE_LIST.pop(indexIdProduct)
    for line in FILE_LIST:
        file.write(f"{line}\n")
    file.close()

def name_products_matched(characterMatched: str) -> list:
    productsMatches = []
    for product in range(1, len(FILE_LIST), 5):
        if characterMatched.upper() in FILE_LIST[product][0].upper():
            productsMatches.append(FILE_LIST[product])
    return productsMatches

if __name__ == '__main__':
    productsAddedN = int(input("Escriba la cantidad de productos que desea ingresar: "))
    fileCreate = open("./inventario.txt", "w")
    fileCreate.close()
    isAdded = add_product(productsAddedN)
    if isAdded:
        read_file("./inventario.txt", "r")
        print("\n Menu")
        print(" 1- Buscar la unidad de medida de  un producto")
        print(" 2- A??adir nuevo producto  ")
        print(" 3- Eliminar un producto ")
        print(" 4- Imprimir lista de productos en el inventario")
        print(" 5- Buscar productos ")
        optionMenu = int(input("Escriba el n??mero de la acci??n de desea realizar: "))
        if optionMenu == 1:
            nameProduct = input("Escriba el nombre del producto al cual le quiere saber su medida: ")
            print(find_name_product(nameProduct))
        elif optionMenu == 2:
            isAdded = add_product(1)
            if isAdded:
                pass
            else:
                print("Hubo un error")
        elif optionMenu == 3:
            idProduct = int(input("Escriba el c??digo del producto que quiere eliminar: "))
            fileInventary = open("./inventario.txt", "w")
            delete_product(idProduct, fileInventary)
        elif optionMenu == 5:
            characterMatched = input("Escriba la inicial del producto que desea buscar: ")
            name_products_matched(characterMatched)
    else:
        print("Hubo un error!")
