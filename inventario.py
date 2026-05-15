import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()
print("bd conectada ✅")

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )
""")
conexion.commit()
print("Tabla creada ✅")

def ver_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print("\n--- PRODUCTOS EN INVENTARIO ---")
    for producto in productos:
     print(f"ID: {producto[0]} | {producto[1]} | Cantidad: {producto[2]} | Precio: ${producto[3]:,.0f}")

def agregar_producto():
   nombre = input("Nombre del producto:")
   cantidad = int(input("cantidad:"))
   precio = float(input("precio:"))
   try:
      cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?,?,?)",(nombre, cantidad, precio))
         
      conexion.commit()
      print(f"'{nombre}' agregado correctamente")
   except:
      print(f" ya existe un producto llamado {nombre}")

def eliminar_producto():
   ver_productos()
   id_eliminar = int(input("\nIngresa el ID del producto a eliminar: "))
   cursor.execute("DELETE FROM productos WHERE id = ?", (id_eliminar,))
   conexion.commit()
   if cursor.rowcount > 0 :
      print("producto eliminado correctamente")
   else:
      print("no se encontró un producto con ese id")



salir = False
while not salir:
    print("\n--- MENÚ ---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
       ver_productos()
    elif opcion == "2":
       agregar_producto()
    elif opcion == "3":
       print("hasta luego")
       conexion.close()
       salir = True
    elif opcion == "4":
       eliminar_producto()

    else:
       print("opcion no valida, intentelo de nuevo")