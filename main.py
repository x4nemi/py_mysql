import mysql.connector

bd = mysql.connector.connect(
    user = 'ximena', password = '123',
    database = 'nopalito'
)

cursor = bd.cursor() #lo que hará la conexión del
                     #script y la base de datos

while True:
    print("1) Agregar usuario")
    print("2) Mostrar usuario(s)")
    print("0) Salir")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        valores = []
        valores.append(input("Correo electronico: "))
        valores.append(input("Contrasenia: "))

        consulta = "INSERT INTO usuario (correo, contrasenia) " \
                   "VALUES (%s, %s)"
        cursor.execute(consulta, tuple(valores)) # esta es la orden
        bd.commit() # esto es lo que lo aplica a la base
        if cursor.rowcount: # atributo que dice los renglones modificados
        # si hay renglones afectados sí se aplicó
            print("Se agregó usuario")
        else:
            print("Error al agregar usuario")
    elif opcion == 2:
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("\nid: ", row[0])
            print("correo: ", row[1])
            print("contrasenia: ", row[2])
    elif opcion == 0:
        break