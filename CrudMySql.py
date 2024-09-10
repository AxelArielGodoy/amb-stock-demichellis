import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="tienda"
    )
    return conexion

def crear_registro_stock():
    rubro = input("Ingrese el rubro: ")
    narticulo = input("Ingrese el número de artículo: ")
    descripcion = input("Ingrese la descripción: ")
    presentacion = input("Ingrese la presentación: ")
    cantu = int(input("Ingrese la cantidad unitaria: "))
    preciocosto = float(input("Ingrese el precio de costo: "))
    precioventa = float(input("Ingrese el precio de venta: "))
    cantstock = int(input("Ingrese la cantidad en stock: "))
    stockcritico = int(input("Ingrese el stock crítico: "))

    conexion = conectar()
    cursor = conexion.cursor()

    consulta = """
        INSERT INTO stock (rubro, narticulo, descripcion, presentacion, cantu, preciocosto, precioventa, cantstock, stockcritico) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    datos = (rubro, narticulo, descripcion, presentacion, cantu, preciocosto, precioventa, cantstock, stockcritico)
    cursor.execute(consulta, datos)
    conexion.commit()

    cursor.close()
    conexion.close()

    print("Registro creado exitosamente.")

def leer_registros_stock():
    conexion = conectar()
    cursor = conexion.cursor()

    consulta = "SELECT * FROM stock"
    cursor.execute(consulta)

    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    print("Registros de Stock:")
    for registro in resultados:
        print(registro)

def actualizar_registro_stock():
    narticulo = input("Ingrese el número de artículo a actualizar: ")
    rubro = input("Ingrese el nuevo rubro: ")
    descripcion = input("Ingrese la nueva descripción: ")
    presentacion = input("Ingrese la nueva presentación: ")
    cantu = int(input("Ingrese la nueva cantidad unitaria: "))
    preciocosto = float(input("Ingrese el nuevo precio de costo: "))
    precioventa = float(input("Ingrese el nuevo precio de venta: "))
    cantstock = int(input("Ingrese la nueva cantidad en stock: "))
    stockcritico = int(input("Ingrese el nuevo stock crítico: "))

    conexion = conectar()
    cursor = conexion.cursor()

    consulta = """
        UPDATE stock 
        SET rubro = %s, descripcion = %s, presentacion = %s, cantu = %s, preciocosto = %s, precioventa = %s, cantstock = %s, stockcritico = %s 
        WHERE narticulo = %s
    """
    datos = (rubro, descripcion, presentacion, cantu, preciocosto, precioventa, cantstock, stockcritico, narticulo)
    cursor.execute(consulta, datos)
    conexion.commit()

    cursor.close()
    conexion.close()

    print("Registro actualizado exitosamente.")

def borrar_registro_stock():
    narticulo = input("Ingrese el número de artículo a borrar: ")

    conexion = conectar()
    cursor = conexion.cursor()

    consulta = "DELETE FROM stock WHERE narticulo = %s"
    datos = (narticulo,)
    cursor.execute(consulta, datos)
    conexion.commit()

    cursor.close()
    conexion.close()

    print("Registro borrado exitosamente.")

def menu():
    while True:
        print("\n--- Menú de Gestión de Stock ---")
        print("1. Crear un nuevo registro")
        print("2. Leer todos los registros")
        print("3. Actualizar un registro")
        print("4. Borrar un registro")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_registro_stock()
        elif opcion == "2":
            leer_registros_stock()
        elif opcion == "3":
            actualizar_registro_stock()
        elif opcion == "4":
            borrar_registro_stock()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

menu()