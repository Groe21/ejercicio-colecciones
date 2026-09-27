def agregar_producto(inventario, productos, categorias, nombre, precio, categoria):
    if nombre in inventario:
        print("El producto", nombre, "ya esta registrado.")
        return False

    inventario[nombre] = precio
    productos.append(nombre)
    categorias.add(categoria)
    print("Producto", nombre, "agregado. Precio:", precio)
    return True


def mostrar_productos(inventario, productos):
    if len(productos) == 0:
        print("El inventario esta vacio.")
        return

    print("--- INVENTARIO DE LA TIENDA ---")
    for i in range(len(productos)):
        nombre = productos[i]
        print(i + 1, ") ", nombre, " - $", inventario[nombre])
    print("Total de productos:", len(productos))


def mostrar_categorias(categorias):
    if len(categorias) == 0:
        print("No hay categorias registradas.")
        return

    print("--- CATEGORIAS ---")
    lista = sorted(categorias)
    for categoria in lista:
        print("-", categoria)
    print("Total de categorias:", len(categorias))


def buscar_producto(inventario, nombre):
    if nombre in inventario:
        print("Producto encontrado:", nombre)
        print("Precio:", inventario[nombre])
        return True

    print("El producto", nombre, "no esta en el inventario.")
    return False


def eliminar_producto(inventario, productos, nombre):
    if nombre not in inventario:
        print("El producto", nombre, "no esta en el inventario.")
        return False

    del inventario[nombre]
    productos.remove(nombre)
    print("Producto", nombre, "eliminado.")
    return True


def recorrer_productos(inventario, productos):
    if len(productos) == 0:
        print("No hay productos en el inventario.")
        return

    print("--- RECORRIDO DEL INVENTARIO ---")
    valor_total = 0
    producto_mas_caro = productos[0]

    for nombre in productos:
        valor_total = valor_total + inventario[nombre]
        if inventario[nombre] > inventario[producto_mas_caro]:
            producto_mas_caro = nombre
        print("Producto:", nombre, "| Precio: $", inventario[nombre])

    print("Valor total: $", valor_total)
    print("Producto mas caro:", producto_mas_caro, "- $", inventario[producto_mas_caro])


if __name__ == "__main__":

    inventario = {}
    productos = []
    categorias = set()

    print("=== CONTROL DE INVENTARIO DE UNA TIENDA ===")
    print("1) Agregar  2) Mostrar  3) Buscar  4) Eliminar  5) Recorrer  6) Salir")

    while True:

        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            categoria = input("Categoria del producto: ")
            agregar_producto(inventario, productos, categorias, nombre, precio, categoria)

        elif opcion == "2":
            mostrar_productos(inventario, productos)
            mostrar_categorias(categorias)

        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(inventario, nombre)

        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, productos, nombre)

        elif opcion == "5":
            recorrer_productos(inventario, productos)

        elif opcion == "6":
            print("Programa terminado.")
            break

        else:
            print("Opcion no valida. Ingrese un numero del 1 al 6.")
