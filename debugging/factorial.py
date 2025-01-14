#!/usr/bin/python3
import sys  # Usamos esta biblioteca para leer lo que el usuario escribe

# Esta función calcula el factorial
def factorial(n):
    result = 1  # Empezamos con 1 porque multiplicar por 1 no cambia nada
    while n > 1:  # Mientras n sea mayor que 1
        result *= n  # Multiplicamos result por n
        n -= 1  # Reducimos n en 1
    return result  # Devolvemos el resultado final

# Ahora verificamos si el usuario dio un número como argumento
if len(sys.argv) > 1:  # sys.argv contiene lo que el usuario escribe después del comando
    try:
        # Convertimos lo que el usuario escribió en un número entero
        num = int(sys.argv[1])
        
        if num < 0:  # Si el número es negativo, mostramos un mensaje de error
            print("Error: El número debe ser mayor o igual a 0.")
        else:
            # Calculamos el factorial
            f = factorial(num)
            print(f"El factorial de {num} es: {f}")
    except ValueError:  # Si el usuario no escribió un número
        print("Error: Por favor, ingresa un número entero.")
else:
    # Si el usuario no escribe nada, mostramos cómo usar el programa
    print("Uso: ./factorial.py <número>")
list