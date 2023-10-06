import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

while True:
    clear_screen()
    print("Opciones de calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '5':
        break
    
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    if opcion == '1':
        print("Resultado: ", suma(numero1, numero2))
    elif opcion == '2':
        print("Resultado: ", resta(numero1, numero2))
    elif opcion == '3':
        print("Resultado: ", multiplicacion(numero1, numero2))
    elif opcion == '4':
        resultado = division(numero1, numero2)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print("Resultado: ", resultado)
    else:
        print("Opción no válida")
    
    input("Presione Enter para continuar...")

