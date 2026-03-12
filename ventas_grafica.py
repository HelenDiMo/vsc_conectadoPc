import matplotlib.pyplot as plt # type: ignore

# Preparamos los datos
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
ventas = [120, 85, 150, 200, 170]

# Creamos la gráfica de barras
plt.bar(dias, ventas, color='pink')

# Personalizamos la gráfica
plt.title('Ventas de la semana')
plt.xlabel('Días de la semana')
plt.ylabel('Número de productos vendidos')

# Mostrar el resultado
plt.show()