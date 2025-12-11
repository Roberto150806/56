
# =======================================================
# EJERCICIO 1: MENÚ (ULTRA SIMPLE)
# =======================================================
op = ''
while op != '4':
    print("\n1. Contar palabras\n2. Mostrar palabras\n3. Mayúsculas\n4. Salir")
    op = input("Opción: ")
    
    if op == '1':
        f = input("Frase: ")
        print(f"Palabras: {len(f.split())}")
    elif op == '2':
        f = input("Frase: ")
        for p in f.split():
            print(p)
    elif op == '3':
        f = input("Frase: ")
        print(f.upper())
    elif op == '4':
        print("Adiós.")
    else:
        print("Inválida.")

# =======================================================
# EJERCICIO 2: NOTAS DE EXÁMENES (ULTRA SIMPLE)
# =======================================================
print("\n" * 2 + "--- EJERCICIO 2 ---")
p1 = float(input("Nota Parcial 1: "))
p2 = float(input("Nota Parcial 2: "))
media = (p1 + p2) / 2

if media >= 5 and p1 >= 4 and p2 >= 4:
    print("APROBADO")
else:
    print("NO APROBADO")
    if p1 < 4:
        print("Repetir Parcial 1")
    if p2 < 4:
        print("Repetir Parcial 2")


# =======================================================
# EJERCICIO 3: FIZZBUZZ (ULTRA SIMPLE)
# =======================================================
print("\n" * 2 + "--- EJERCICIO 3 ---")
for n in range(1, 51):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# =======================================================
# EJERCICIO 4: ANÁLISIS DE INTERVALO (ULTRA SIMPLE)
# =======================================================
print("\n" * 2 + "--- EJERCICIO 4 ---")
while True:
    inf = int(input("Límite inferior: "))
    sup = int(input("Límite superior: "))
    if inf <= sup:
        break
    print("Inferior > Superior. Intenta de nuevo.")

suma = 0
fuera = 0
igual = False

print("Introduce números (0 para terminar).")
while True:
    num = int(input("Número: "))
    if num == 0:
        break

    if inf < num < sup: # Dentro del intervalo abierto
        suma += num
    else:
        fuera += 1 # Fuera del intervalo
        if num == inf or num == sup:
            igual = True

print(f"\nSuma dentro: {suma}")
print(f"Conteo fuera: {fuera}")
print("Igual a límites:", "SÍ" if igual else "NO")
