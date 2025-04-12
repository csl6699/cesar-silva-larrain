import sys
print("Python version:", sys.version)

try:
    print("Intentando importar pandas...")
    import pandas as pd
    print("Pandas importado correctamente")
    
    print("Intentando importar plotly...")
    import plotly.express as px
    import plotly.io as pio
    print("Plotly importado correctamente")
    
    print("Leyendo el archivo CSV...")
    # Leer el archivo CSV
    df = pd.read_csv('antofagasta (1).csv', skiprows=2)
    print("Archivo CSV leído correctamente")

    print("Creando columna de fecha...")
    # Crear una columna de fecha
    df['Fecha'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    print("Columna de fecha creada correctamente")

    print("Generando el gráfico...")
    # Crear el gráfico con plotly
    fig = px.line(df, x='Fecha', y='GHI', 
                  title='Radiación Solar Global en Antofagasta',
                  labels={'GHI': 'Radiación Solar Global (W/m²)', 'Fecha': 'Fecha'},
                  template='plotly_white')
    
    # Mejorar el diseño
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        legend_font_size=12,
        height=600,
        width=1000
    )
    
    # Guardar como HTML (se abrirá en el navegador)
    print("Guardando el gráfico como HTML...")
    pio.write_html(fig, 'radiacion_solar_antofagasta.html')
    
    # Guardar como imagen
    print("Guardando el gráfico como imagen...")
    pio.write_image(fig, 'radiacion_solar_antofagasta.png')
    
    print("¡Éxito! El gráfico se ha guardado como:")
    print("1. radiacion_solar_antofagasta.html (abre este archivo en tu navegador)")
    print("2. radiacion_solar_antofagasta.png")

except Exception as e:
    print(f"Error: {str(e)}")
    print("Detalles del error:", sys.exc_info()) 