# ingresa tu correo
correo = input("Introduce tu correo electrónico: ")

# extraer el nombres antes de la arroba
nombre_usuario = correo.split('@')[0]

# creacion de nuevo correo con "ceu.es"
nuevo_correo = nombre_usuario + "@ceu.es"

# mostrar resultado
print(f"Tu nuevo correo electrónico es: {nuevo_correo}")