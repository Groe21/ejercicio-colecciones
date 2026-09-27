# ejercicio-colecciones

**Tarea Semana 15** - Colecciones de datos: listas, conjuntos y diccionarios
Materia: Fundamentos de Programación
Autor: Oscar Emilio Guerrero Romero

## Problema de la vida real

El programa resuelve el control del **inventario de una tienda**. Permite registrar productos con su precio y categoría, mostrar el inventario completo, buscar un producto, eliminar un producto y recorrer el inventario calculando el valor total y el producto más caro.

## Colecciones de datos utilizadas

| Colección | Estructura en Python | Uso en el programa |
|---|---|---|
| Diccionario | `dict` | `inventario`: relaciona el **nombre del producto** con su **precio** |
| Conjunto | `set` | `categorias`: guarda las categorías **sin repetir** |
| Lista | `list` | `productos`: mantiene el **orden de ingreso** de los productos |

## Funcionalidades (menú interactivo)

1. **Agregar** producto (diccionario + lista + conjunto).
2. **Mostrar** el inventario y las categorías registradas.
3. **Buscar** un producto por su nombre.
4. **Eliminar** un producto del inventario.
5. **Recorrer** el inventario: calcula el valor total y el producto más caro.
6. **Salir** del programa.

## Estructura del código

El archivo se organiza en funciones:

- `agregar_producto()` — inserta datos en las tres colecciones.
- `mostrar_productos()` — recorre la lista y muestra el diccionario.
- `mostrar_categorias()` — muestra el conjunto de categorías.
- `buscar_producto()` — busca un producto en el diccionario.
- `eliminar_producto()` — elimina del diccionario y de la lista.
- `recorrer_productos()` — recorre la lista y acumula el valor total.

El menú principal se encuentra en el bloque `if __name__ == "__main__":`.

## Cómo ejecutar

1. Tener instalado **Python 3**.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python ejercicio_colecciones.py
```

## Ejemplo de salida

```
=== CONTROL DE INVENTARIO DE UNA TIENDA ===
Opciones: 1) Agregar  2) Mostrar  3) Buscar  4) Eliminar  5) Recorrer  6) Salir

Ingrese una opcion: 1
--- AGREGAR PRODUCTO ---
Nombre del producto: Arroz
Precio del producto: 3.50
Categoria del producto: Alimentos
Producto Arroz agregado. Precio: 3.5

Ingrese una opcion: 2
--- INVENTARIO DE LA TIENDA ---
1 )  Arroz  - $ 3.5
Total de productos: 1

--- CATEGORIAS ---
- Alimentos
Total de categorias: 1
```

## Repositorio

- Usuario de GitHub: [Groe21](https://github.com/Groe21)
- Repositorio: [ejercicio-colecciones](https://github.com/Groe21/ejercicio-colecciones)
