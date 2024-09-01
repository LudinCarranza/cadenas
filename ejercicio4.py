# ingreso del numero
telefono = input("Introduce el número de teléfono en el formato +34-número-extensión: ")

# separador del numero
partes = telefono.split('-')
# el número sin el prefijo y la extension
numero_sin_prefijo_y_extension = partes[1]

# el resultado
print(f"El número de teléfono sin el prefijo y la extensión es: {numero_sin_prefijo_y_extension}")