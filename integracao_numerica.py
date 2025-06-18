import numpy as np

# Regra do Trapézio
def regra_trapezio(f, a, b, n):
    """
    Parâmetros da função:
    f - Função a ser integrada
    a, b - Limites de integração
    n - número de subintervalos da regra de trapézios
    """
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        soma += f(a + i * h)
    return h * soma

# Integral I.1: Ex(x, 2, 1) de 1 a -2

def f1(x):
    return (45*x + 135) / ((x+3)**2 + 5)**1.5
# Integral I.2: Ey(-2, y, 1) de 2 a 5

def f2_pontual(y):
    return (45*y - 180) / ((y-4)**2 + 2)**1.5

def f2_linha(y):
    return 36 / (y-1)

def f2(y):
    return f2_linha(y) + f2_pontual(y)

# Integral I.3: Ez(-2, 5, z)

def f3_pontual(z):
    return 45*z / (2 + z**2)**1.5

def f3_linha(z):
    if z == 1 and (5-1) == 0: # Condição original de singularidade da linha de carga
        return 0
    return 36*(z-1) / (16 + (z-1)**2)

def f3(z):
    return f3_linha(z) + f3_pontual(z)



n_subintervalos = 54

integral1 = regra_trapezio(f1, 1, -2, n_subintervalos)
integral2 = regra_trapezio(f2, 2, 5, n_subintervalos)
integral3 = regra_trapezio(f3, 1, 3, n_subintervalos)

V_AB = integral1 + integral2 + integral3
V_A = 100
V_B = V_A - V_AB

print(f"{V_B:.2f}")
