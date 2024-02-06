
while True:
    print("\tMenu Principal\n")

    print("1. Operadores Aritmeticos.\n"
        "2. Operadores Relacionales.\n"
        "3. Operadores Logicos.\n"
        "4. Funciones y Condicionales.\n"
        "5. Clases y metdos\n"
        "6. Salir.\n")

    opc = input("Ingrese una opcion: ")

    if opc.isdigit():
        opc = int(opc)

        if opc==1:
            num1 = int(input("Ingrese el primer valor: "))
            num2 = int(input("Ingrese el segundo valor: "))

            suma = num1 + num2
            resta = num1 - num2
            multiplicacion = num1 * num2
            
            if num2==0:
                print(f"El resultado de {num1} + {num2} = {suma}")
                print(f"El resultado de {num1} - {num2} = {resta}")
                print(f"El resultado de {num1} * {num2} = {multiplicacion}")
                print("No se puede dividir entre cero.")
                
            else:
                division = num1 / num2
                print(f"El resultado de {num1} + {num2} = {suma}")
                print(f"El resultado de {num1} - {num2} = {resta}")
                print(f"El resultado de {num1} * {num2} = {multiplicacion}")
                print(f"El resultado de {num1} / {num2} = {division}")
        
        if opc==2:
            numero = float(input("Ingrese un numero: "))
            
            if numero==0:
                print("EL numero es cero.")

            elif numero>0:
                print("El numero es positivo.")

            else:
                print("El numero es negativo.")

        if opc==3:
            
            for i in range(1,20+1,2):
                print(1+i, end=" ")  

        if opc==4:
            def suma(num1,num2):
                suma = num1 + num2
                return suma%2==0
            
            num1 = int(input("Ingrese el primer valor:"))
            num2 = int(input("Ingrese el segundo valor: "))
            result = suma(num1,num2)

            if result:
                print(f"el resultado de la suma es {num1 + num2}  y es un numero par.")
            else:
                print(f"el resultado de la suma es {num1 + num2}  y es un numero impar.")
        
        if opc==5:
            class Estudiante:
                def __init__(self, nombre, edad, calificacion):
                    self.nombre = nombre
                    self.edad = edad
                    self.calificacion = calificacion

            nombre_estudiante = input("Ingrese el nombre: ")
            edad_estudiante = int(input("Ingrese la edad: "))
            calificacion_estudiante = float(input("Ingrese la calificación: "))

            estudiante1 = Estudiante(nombre_estudiante, edad_estudiante, calificacion_estudiante)

            if estudiante1.calificacion >= 60:
                print(f"{estudiante1.nombre} ha aprobado.")
            else:
                print(f"{estudiante1.nombre} no ha aprobado.")
        
        if opc==6:
            print("Saliendo del programa...")
            break
        
        else:
            print("Opcion incorrecta.")
    else:
        print("Opcion incorrecta.")
    