import mysql.connector

bd = mysql.connector.connect(
    user = 'ximena', password = '123',
    database = 'nopalito'
)

cursor = bd.cursor()

while True:
    print("1) Agregar usuario")
    print("2) Mostrar usuario(s)")
    print("0) Salir")
    opcion = int(input("Opcion: "))

    if opcion == 1:
        correo = input("Correo electronico: ")
        contrasenia = input("Contrasenia: ")

        consulta = "INSERT INTO usuario (correo, contrasenia) " \
                    "VALUES (%s, %s)"
        cursor.execute(consulta, (correo, contrasenia))
        bd.commit()
        if cursor.rowcount:
            print("Se agregó usuario")
        else:
            print("Error al agregar usuario")
    elif opcion == 2:
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("id: ", row[0])
            print("correo: ", row[1])
            print("contrasenia: ", row[2])
    elif opcion == 0:
        break