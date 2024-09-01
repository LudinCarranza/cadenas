frase = input("Introduce una frase: ")


vocal = input("Introduce una vocal: ")

vocal = vocal.lower()

frase_modificada = frase.replace(vocal, vocal.upper())

print(f"La frase modificada es: {frase_modificada}")
