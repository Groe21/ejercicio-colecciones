# ============================================================
# TAREA SEMANA 15 - Colecciones de datos: listas, conjuntos y diccionarios
# Materia: Fundamentos de Programacion
# Autor: Oscar Emilio Guerrero Romero
# Problema de la vida real: control del inventario de una tienda
# ============================================================

# El diccionario "inventario" relaciona el nombre de un producto con su precio.
# El conjunto "categorias" almacena las categorias sin repetir.
# La lista "productos" mantiene el orden de ingreso de los productos.


def agregar_producto(inventario, categorias, productos, nombre, precio, categoria):
    """Agrega un producto al inventario, a la lista y a las categorias."""
    if nombre in inventario:
        print("El producto", nombre, "ya esta registrado.")
        return False

    inventario[nombre] = precio
    productos.append(nombre)
    categorias.add(categoria)
    print("Producto", nombre, "agregado con exito. Precio:", precio)
    return True


def mostrar_productos(inventario, productos):
    """Muestra en pantalla todos los productos del inventario."""
    print("\n--- INVENTARIO DE LA TIENDA ---")
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        for posicion in range(len(productos)):
            nombre = productos[posicion]
            print(posicion + 1, ") ", nombre, " - $", inventario[nombre])
    print("Total de productos registrados:", len(productos))


def mostrar_categorias(categorias):
    """Muestra las categorias existentes sin repetir, ordenadas alfabeticamente."""
    print("\n--- CATEGORIAS REGISTRADAS ---")
    if len(categorias) == 0:
        print("No hay categorias registradas.")
    else:
        lista_ordenada = sorted(categorias)
        for categoria in lista_ordenada:
            print("-", categoria)
        print("Cantidad de categorias:", len(categorias))


def buscar_producto(inventario, nombre):
    """Busca un producto en el inventario y muestra su precio."""
    print("\n--- BUSQUEDA DE PRODUCTO ---")
    if nombre in inventario:
        print("Producto encontrado:", nombre)
        print("Precio:", inventario[nombre])
        return True
    print("El producto", nombre, "no se encuentra en el inventario.")
    return False


def eliminar_producto(inventario, productos, nombre):
    """Elimina un producto del inventario y de la lista."""
    if nombre not in inventario:
        print("El producto", nombre, "no se encuentra en el inventario.")
        return False

    del inventario[nombre]
    productos.remove(nombre)
    print("Producto", nombre, "eliminado correctamente.")
    return True


def recorrer_productos(inventario, productos):
    """Recorre el inventario y calcula el valor total y el producto mas caro."""
    print("\n--- RECORRIDO DEL INVENTARIO ---")
    if len(productos) == 0:
        print("No hay productos para recorrer.")
        return

    valor_total = 0
    producto_mas_caro = productos[0]

    for nombre in productos:
        valor_total = valor_total + inventario[nombre]
        if inventario[nombre] > inventario[producto_mas_caro]:
            producto_mas_caro = nombre
        print("Producto:", nombre, "| Precio: $", inventario[nombre])

    print("Valor total del inventario: $", valor_total)
    print("Producto mas caro:", producto_mas_caro, "- $", inventario[producto_mas_caro])


def salir():
    """Muestra el mensaje de finalizacion del programa."""
    print("Programa terminado.")


def main():
    """Menu principal que permite Agregar, Mostrar, Buscar, Eliminar y Recorrer."""
    # ---------------- DECLARACION DE LAS COLECCIONES ----------------
    inventario = {}          # Diccionario: producto -> precio
    categorias = set()       # Conjunto: categorias sin repetir
    productos = []           # Lista: orden de ingreso de los productos

    print("=== CONTROL DE INVENTARIO DE UNA TIENDA ===")
    print("Opciones: 1) Agregar  2) Mostrar  3) Buscar  4) Eliminar  5) Recorrer  6) Salir")

    while True:
        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            # AGREGAR
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            categoria = input("Categoria del producto: ")
            agregar_producto(inventario, categorias, productos, nombre, precio, categoria)

        elif opcion == "2":
            # MOSTRAR
            mostrar_productos(inventario, productos)
            mostrar_categorias(categorias)

        elif opcion == "3":
            # BUSCAR
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto(inventario, nombre)

        elif opcion == "4":
            # ELIMINAR
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario, productos, nombre)

        elif opcion == "5":
            # RECORRER
            recorrer_productos(inventario, productos)

        elif opcion == "6":
            # SALIR
            salir()
            break

        else:
            print("Opcion no valida. Ingrese un numero del 1 al 6.")


if __name__ == "__main__":
    main()
