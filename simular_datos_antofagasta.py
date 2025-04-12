import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración de la ubicación
location_data = {
    'Source': 'SimSolar',
    'Location ID': '00001',
    'City': 'S1',
    'State': 'NA',
    'Country': 'Chile',
    'Latitude': -22.9234,
    'Longitude': -69.9099,
    'Time Zone': -4,
    'Elevation': 1635
}

# Función para generar radiación solar simulada
def generar_radiacion_solar(hora, mes):
    # Factores estacionales (mayor en verano, menor en invierno)
    factor_estacional = 1 + 0.3 * np.sin(2 * np.pi * (mes - 1) / 12)
    
    # Curva diaria de radiación solar (máximo al mediodía)
    hora_rad = 12  # Hora de máxima radiación
    sigma = 4      # Desviación estándar para la curva gaussiana
    radiacion_max = 1000 * factor_estacional  # Radiación máxima en W/m²
    
    # Calcular radiación para la hora actual
    radiacion = radiacion_max * np.exp(-(hora - hora_rad)**2 / (2 * sigma**2))
    
    # Añadir variabilidad aleatoria
    radiacion += np.random.normal(0, 50)
    
    # Asegurar valores no negativos
    return max(0, radiacion)

# Función para generar temperatura simulada
def generar_temperatura(hora, mes):
    # Temperatura base según el mes
    temp_base = 20 + 5 * np.sin(2 * np.pi * (mes - 1) / 12)
    
    # Variación diaria (más caliente durante el día)
    variacion_diaria = 5 * np.sin(2 * np.pi * (hora - 6) / 24)
    
    # Añadir variabilidad aleatoria
    temp = temp_base + variacion_diaria + np.random.normal(0, 1)
    
    return round(temp, 1)

# Función para generar humedad relativa simulada
def generar_humedad(hora, mes):
    # Humedad base según el mes (mayor en invierno)
    humedad_base = 60 - 20 * np.sin(2 * np.pi * (mes - 1) / 12)
    
    # Variación diaria (mayor humedad en la noche)
    variacion_diaria = 20 * np.sin(2 * np.pi * (hora - 0) / 24)
    
    # Añadir variabilidad aleatoria
    humedad = humedad_base + variacion_diaria + np.random.normal(0, 5)
    
    # Limitar entre 0 y 100
    return round(max(0, min(100, humedad)), 1)

# Función para generar velocidad del viento simulada
def generar_viento(hora, mes):
    # Velocidad base según el mes
    velocidad_base = 3 + 2 * np.sin(2 * np.pi * (mes - 1) / 12)
    
    # Variación diaria
    variacion_diaria = 2 * np.sin(2 * np.pi * (hora - 12) / 24)
    
    # Añadir variabilidad aleatoria
    velocidad = velocidad_base + variacion_diaria + np.random.normal(0, 0.5)
    
    # Asegurar valores no negativos
    return round(max(0, velocidad), 1)

# Función para generar dirección del viento simulada
def generar_direccion_viento():
    # Dirección aleatoria entre 0 y 360 grados
    return round(np.random.uniform(0, 360), 1)

# Generar datos para un año completo
fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2023, 12, 31, 23, 0)
fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='H')

# Crear DataFrame con datos simulados
datos = []

for fecha in fechas:
    hora = fecha.hour
    mes = fecha.month
    
    # Generar valores simulados
    ghi = generar_radiacion_solar(hora, mes)
    dni = ghi * 0.8  # DNI suele ser aproximadamente 80% de GHI
    dhi = ghi * 0.2  # DHI suele ser aproximadamente 20% de GHI
    
    temp = generar_temperatura(hora, mes)
    temp_rocio = temp - np.random.uniform(2, 5)  # Temperatura de rocío ligeramente menor
    humedad = generar_humedad(hora, mes)
    presion = 845 + np.random.normal(0, 1)  # Presión atmosférica en hPa
    velocidad_viento = generar_viento(hora, mes)
    direccion_viento = generar_direccion_viento()
    
    # Añadir fila al DataFrame
    datos.append({
        'Year': fecha.year,
        'Month': fecha.month,
        'Day': fecha.day,
        'Hour': fecha.hour,
        'Minute': fecha.minute,
        'GHI': round(ghi, 1),
        'DNI': round(dni, 1),
        'DHI': round(dhi, 1),
        'Tdry': round(temp, 1),
        'Tdew': round(temp_rocio, 1),
        'RH': round(humedad, 1),
        'Pres': round(presion, 1),
        'Wspd': round(velocidad_viento, 1),
        'Wdir': round(direccion_viento, 1),
        'Snow Depth': 0  # Sin nieve en Antofagasta
    })

# Crear DataFrame
df = pd.DataFrame(datos)

# Guardar datos simulados
df.to_csv('antofagasta_simulado.csv', index=False)

print("Datos simulados guardados en 'antofagasta_simulado.csv'")
print(f"Se generaron {len(df)} registros para el año 2023") 