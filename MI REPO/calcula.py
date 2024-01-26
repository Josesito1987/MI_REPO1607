#Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#En caso de no introducir una opción válida, el programa informará de que no es correcta.

num_1 = int(input('Ingrese el primer nro.: '))
num_2 = int(input('Ingrese el segundo nro.: '))

bandera = True
while bandera:
    opcion = input('''Ingrese una opcion:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Salir
    Operacion Selecciona: ''')

    if opcion == '1':
        print (int(num_1 + num_2))
    elif opcion == '2':
        print (int(num_1 - num_2))
    elif opcion == '3':
        print (int(num_1 * num_2))
    elif opcion == '4':
        print ('Gracias por confiar en "MathNumbs"')
        bandera = False
    else:
        print ('No esxiste opcion. Intentelo nuevamente: ')
