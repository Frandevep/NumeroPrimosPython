# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):  # Solo hasta la raíz cuadrada
        if numero % i == 0:
            return False
    return True

# Pedimos un número al usuario
num = int(input("Ingresa un número entero: "))

# Verificamos si es primo o no
if es_primo(num):
    print(num, "es un número primo.")
else:
    print(num, "NO es un número primo.")
