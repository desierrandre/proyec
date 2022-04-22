inventario_Prin=[]
ncant=int(input("Escriba la cantidad de productos que desea ingresar "))
inv=open("inventario.txt", "w")
for i in range(0,ncant):
    nombre=input("Escriba el nombre del producto ")
    codigo=int(input("Escriba el codigo del producto "))
    undidad=input("Escriba la unidad de medida del producto ")
    precio=int(input("Escriba el precio del producto "))
    cant_exist=int(input("Escriba la cantidad de ese producto que hay "))
    inventario_Prin.append(nombre)
    inventario_Prin.append(codigo)
    inventario_Prin.append(undidad)
    inventario_Prin.append(precio)
    inventario_Prin.append(cant_exist)    
int_list = [str(i) for i in inventario_Prin]
for i in int_list:
    inv.write(f"{i} \n")
inv.close()

print ("\n Menu")
print (" 1- Buscar la unidad de medida de  un producto")
print (" 2- Añadir nuevo producto  ")
print (" 3- Eliminar un producto ")
print (" 4- Imprimir lista de productos en el inventario")
print (" 5- Buscar productos ")
accion=int(input(" Escriba el numero de la accion que dea realizar: "))

if accion==1: 
    nom=input("Escriba el nombre del producto al cual le quiere saber su medida")
    inventario_Prin.index(nom)
