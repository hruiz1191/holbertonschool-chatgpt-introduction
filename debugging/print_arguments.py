#!/usr/bin/python3
import sys

# Verificar si hay argumentos además del nombre del archivo
if len(sys.argv) > 1:
    print("File name:", sys.argv[0])  # Nombre del archivo
    print("Arguments provided:")
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
else:
    print("No arguments were provided. Please provide arguments when running the script.")
