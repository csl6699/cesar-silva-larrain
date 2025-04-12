import csv
from datetime import datetime
import os

# Función para crear un gráfico ASCII simple
def crear_grafico_ascii(valores, max_valor, ancho=60, alto=20):
    # Encontrar el valor máximo para escalar el gráfico
    if max_valor <= 0:
        max_valor = 1  # Evitar división por cero
    
    # Crear el gráfico
    grafico = []
    for i in range(alto, 0, -1):
        linea = ""
        for valor in valores:
            # Calcular la altura de la barra
            altura = int((valor / max_valor) * alto)
            if altura >= i:
                linea += "█"  # Barra llena
            else:
                linea += " "  # Espacio vacío
        grafico.append(linea)
    
    # Añadir línea base
    base = "─" * len(valores)
    grafico.append(base)
    
    # Añadir etiquetas de hora
    etiquetas = ""
    for i in range(0, 24, 2):
        etiquetas += f"{i:2d}h".ljust(5)
    grafico.append(etiquetas)
    
    return "\n".join(grafico)

# Leer los datos del archivo CSV
print("Leyendo datos del archivo CSV...")
datos = []
with open('antofagasta (1).csv', 'r') as file:
    # Saltar las primeras dos líneas (encabezados)
    next(file)
    next(file)
    
    # Leer el resto de las líneas
    for line in file:
        valores = line.strip().split(',')
        if len(valores) >= 7:  # Asegurarse de que hay suficientes valores
            try:
                year = int(valores[0])
                month = int(valores[1])
                day = int(valores[2])
                hour = int(valores[3])
                minute = int(valores[4])
                dni = float(valores[6])  # DNI está en la séptima columna
                
                # Crear objeto de fecha
                fecha = datetime(year, month, day, hour, minute)
                
                # Añadir a la lista de datos
                datos.append((fecha, dni))
            except (ValueError, IndexError):
                continue

# Seleccionar un día específico (por ejemplo, el primer día del año)
dia_especifico = datetime(2014, 1, 1)
datos_dia = [(fecha, dni) for fecha, dni in datos if fecha.date() == dia_especifico.date()]

# Extraer horas y valores DNI
horas = [fecha.hour for fecha, _ in datos_dia]
valores_dni = [dni for _, dni in datos_dia]

# Crear un array de 24 horas con valores DNI (0 para horas sin datos)
dni_por_hora = [0] * 24
for hora, dni in zip(horas, valores_dni):
    dni_por_hora[hora] = dni

# Encontrar el valor máximo para escalar el gráfico
max_dni = max(dni_por_hora) if dni_por_hora else 1

# Crear el gráfico ASCII
grafico_ascii = crear_grafico_ascii(dni_por_hora, max_dni)

# Mostrar el gráfico en la terminal
print("\n" + "=" * 80)
print(f"RADIACIÓN DIRECTA NORMAL (DNI) EN ANTOFAGASTA - {dia_especifico.strftime('%d/%m/%Y')}")
print("=" * 80)
print(grafico_ascii)
print("=" * 80)
print(f"Valor máximo de DNI: {max_dni:.1f} W/m²")
print("=" * 80)

# Guardar el gráfico en un archivo de texto
with open('grafico_dni_ascii.txt', 'w') as f:
    f.write("=" * 80 + "\n")
    f.write(f"RADIACIÓN DIRECTA NORMAL (DNI) EN ANTOFAGASTA - {dia_especifico.strftime('%d/%m/%Y')}\n")
    f.write("=" * 80 + "\n")
    f.write(grafico_ascii + "\n")
    f.write("=" * 80 + "\n")
    f.write(f"Valor máximo de DNI: {max_dni:.1f} W/m²\n")
    f.write("=" * 80 + "\n")

print("\nGrásfico guardado en 'grafico_dni_ascii.txt'") 