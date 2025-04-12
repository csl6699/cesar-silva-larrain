import sys
print("Python version:", sys.version)

try:
    print("Intentando importar pandas...")
    import pandas as pd
    print("Pandas importado correctamente")
    
    print("Intentando importar matplotlib...")
    import matplotlib.pyplot as plt
    print("Matplotlib importado correctamente")
    
    print("Intentando importar seaborn...")
    import seaborn as sns
    print("Seaborn importado correctamente")
    
    import os

    # Configurar el estilo del gráfico
    plt.style.use('seaborn')
    sns.set_palette("husl")

    print("Leyendo el archivo CSV...")
    # Leer el archivo CSV
    df = pd.read_csv('antofagasta (1).csv', skiprows=2)
    print("Archivo CSV leído correctamente")

    print("Creando columna de fecha...")
    # Crear una columna de fecha
    df['Fecha'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    print("Columna de fecha creada correctamente")

    print("Generando el gráfico...")
    # Crear el gráfico
    plt.figure(figsize=(15, 8))
    plt.plot(df['Fecha'], df['GHI'], label='Radiación Solar Global (GHI)')
    plt.title('Radiación Solar Global en Antofagasta', fontsize=14)
    plt.xlabel('Fecha', fontsize=12)
    plt.ylabel('Radiación Solar Global (W/m²)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)

    # Rotar las etiquetas del eje x para mejor legibilidad
    plt.xticks(rotation=45)

    # Ajustar los márgenes
    plt.tight_layout()

    print("Guardando el gráfico...")
    # Guardar el gráfico
    output_file = 'radiacion_solar_antofagasta.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    
    # Mostrar el gráfico en pantalla
    print("Mostrando el gráfico...")
    plt.show()
    
    plt.close()

    # Verificar si el archivo se creó
    if os.path.exists(output_file):
        print(f"¡Éxito! El gráfico se ha guardado como: {output_file}")
        print(f"Ruta completa: {os.path.abspath(output_file)}")
    else:
        print("Error: El archivo no se creó correctamente")

except Exception as e:
    print(f"Error: {str(e)}")
    print("Detalles del error:", sys.exc_info()) 
    