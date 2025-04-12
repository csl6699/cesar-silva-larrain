import csv
import random
from datetime import datetime, timedelta

# Crear archivo CSV con datos simulados
with open('antofagasta_simulado_simple.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir encabezados
    writer.writerow(['Fecha', 'Hora', 'Radiacion_Solar', 'Temperatura', 'Humedad', 'Velocidad_Viento'])
    
    # Generar datos para un mes (31 días)
    fecha_inicio = datetime(2023, 1, 1)
    
    for dia in range(31):
        fecha_actual = fecha_inicio + timedelta(days=dia)
        
        for hora in range(24):
            # Simular radiación solar (máximo al mediodía)
            if 6 <= hora <= 18:  # Durante el día
                radiacion_base = 800 * (1 - abs(hora - 12) / 6)
                radiacion = max(0, radiacion_base + random.uniform(-100, 100))
            else:  # Durante la noche
                radiacion = 0
            
            # Simular temperatura (más caliente durante el día)
            temp_base = 20 + 5 * (1 - abs(hora - 12) / 12)
            temperatura = temp_base + random.uniform(-2, 2)
            
            # Simular humedad (mayor en la noche)
            humedad_base = 60 + 20 * (1 - abs(hora - 0) / 12)
            humedad = min(100, max(0, humedad_base + random.uniform(-10, 10)))
            
            # Simular velocidad del viento
            viento = random.uniform(0, 5)
            
            # Escribir datos en el CSV
            writer.writerow([
                fecha_actual.strftime('%Y-%m-%d'),
                f"{hora:02d}:00",
                round(radiacion, 1),
                round(temperatura, 1),
                round(humedad, 1),
                round(viento, 1)
            ])

print("Datos simulados guardados en 'antofagasta_simulado_simple.csv'")
print("Este archivo contiene datos simulados para un mes completo con mediciones cada hora.")
print("Puedes abrir este archivo en Excel para visualizar los datos.") 