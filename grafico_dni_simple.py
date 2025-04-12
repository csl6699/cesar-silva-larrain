import csv
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Crear directorio para guardar gráficos si no existe
if not os.path.exists('graficos_dni'):
    os.makedirs('graficos_dni')

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

# Crear el gráfico
plt.figure(figsize=(12, 8))
plt.plot(horas, valores_dni, marker='o', linestyle='-', linewidth=2, markersize=8, 
         color='orange', label='DNI (Radiación Directa Normal)')

# Personalizar el gráfico
plt.title(f'Radiación Directa Normal (DNI) en Antofagasta - {dia_especifico.strftime("%d/%m/%Y")}', 
          fontsize=16)
plt.xlabel('Hora del día', fontsize=14)
plt.ylabel('Radiación Directa Normal (W/m²)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

# Establecer límites del eje x para mostrar todas las horas del día
plt.xlim(0, 23)

# Añadir etiquetas de hora en el eje x
plt.xticks(range(0, 24, 2))

# Ajustar los márgenes
plt.tight_layout()

# Guardar el gráfico
output_file = 'graficos_dni/dni_dia_especifico_simple.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close()

print(f"Gráfico guardado como: {output_file}")
print(f"Este gráfico muestra la radiación directa normal (DNI) para el día {dia_especifico.strftime('%d/%m/%Y')}")
print("Puedes abrir el archivo de imagen para ver el gráfico.") 