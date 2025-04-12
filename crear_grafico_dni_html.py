import csv
from datetime import datetime
import os

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

# Leer el archivo HTML plantilla
with open('grafico_dni.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Reemplazar los datos en el archivo HTML
html_content = html_content.replace(
    'const horas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23];',
    f'const horas = {list(range(24))};'
)

html_content = html_content.replace(
    'const valoresDNI = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];',
    f'const valoresDNI = {dni_por_hora};'
)

# Guardar el archivo HTML con los datos reales
with open('grafico_dni_real.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Grásfico HTML creado con datos reales: grafico_dni_real.html")
print(f"Este archivo muestra la radiación directa normal (DNI) para el día {dia_especifico.strftime('%d/%m/%Y')}")
print("Puedes abrir el archivo en tu navegador web para ver el gráfico.") 