import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Configurar el estilo
plt.style.use('seaborn')
sns.set_palette("husl")

# Leer los datos del archivo CSV
print("Leyendo datos del archivo CSV...")
df = pd.read_csv('antofagasta (1).csv', skiprows=2)

# Crear columna de fecha
df['Fecha'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])

# Seleccionar un día específico (por ejemplo, el primer día del año)
dia_especifico = datetime(2014, 1, 1)
datos_dia = df[df['Fecha'].dt.date == dia_especifico.date()]

# Crear directorio para guardar gráficos si no existe
if not os.path.exists('graficos_dni'):
    os.makedirs('graficos_dni')

# Crear el gráfico
plt.figure(figsize=(12, 8))
plt.plot(datos_dia['Fecha'].dt.hour, datos_dia['DNI'], 
         marker='o', linestyle='-', linewidth=2, markersize=8, 
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
output_file = 'graficos_dni/dni_dia_especifico.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close()

print(f"Gráfico guardado como: {output_file}")
print(f"Este gráfico muestra la radiación directa normal (DNI) para el día {dia_especifico.strftime('%d/%m/%Y')}")
print("Puedes abrir el archivo de imagen para ver el gráfico.") 