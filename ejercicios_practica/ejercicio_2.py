# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores

# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...

print("ejercicio 1")
colores = ['rojo', 'naranja', 'verde', 'azul']
for i in colores:
    print(i)


# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...
print("ejercicio 2")
colores = ['rojo', 'naranja', 'verde', 'azul']
colores_len = len(colores)
for i in range(colores_len):
    colores_i = colores[i]
    print(colores_i)
print("terminamos!")