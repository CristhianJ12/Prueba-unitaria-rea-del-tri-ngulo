import math
def area_base_altura(base, altura):
    area = 0.5 * base * altura
    return area

def area_lados(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

casos_prueba = [
    (12, 6), # Caso 3
    (9, 4),  # Caso 4
    (15, 10),# Caso 5
    (5, 12, 13),   # Caso 6
    (8, 15, 17),   # Caso 7
    (3, 4, 5),     # Caso 8
    (6, 8, 10),    # Caso 9
    (9, 12, 15)    # Caso 10
]

for i, caso in enumerate(casos_prueba, 1):
    print("Caso de prueba", i)
    if len(caso) == 2:
        base, altura = caso
        area = area_base_altura(base, altura)
        print("Área del triángulo con base y altura conocidas:", area)
    elif len(caso) == 3:
        a, b, c = caso
        area = area_lados(a, b, c)
        print("Área del triángulo con longitudes de los tres lados conocidos:", area)
    print()