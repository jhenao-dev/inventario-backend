import sqlite3

conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()
print("bd conectada ✅")

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )
""")
conexion.commit()
print("Tabla creada ✅")

# Insertar solo si la tabla está vacía
cursor.execute("SELECT COUNT(*) FROM productos")
total = cursor.fetchone()[0]

if total == 0:
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES ('Laptop', 10, 2500000)")
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES ('Mouse', 50, 45000)")
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES ('Teclado', 30, 120000)")
    conexion.commit()
    print("Productos insertados ✅")
else:
    print("Productos ya existen, no se insertan de nuevo ✅")

# Consultar y mostrar todos los productos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

print("\n--- PRODUCTOS EN INVENTARIO ---")
for producto in productos:
    print(f"ID: {producto[0]} | {producto[1]} | Cantidad: {producto[2]} | Precio: ${producto[3]:,.0f}")