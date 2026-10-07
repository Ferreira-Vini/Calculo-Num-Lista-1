import math
import sys

# EPSILON DA MÁQUINA

eps = sys.float_info.epsilon

# FUNÇÃO

def f(x, E):
    return -1 / x**3 - 1 / x**2 - E
  
# DERIVADA

def df(x):
    return 3 / x**4 + 2 / x**3

# CRITÉRIO DE PARADA

def convergiu(x_novo, x_antigo):
    return abs(x_novo - x_antigo) <= eps * max(
        1,
        abs(x_novo)
    )

# ENCONTRA UM INTERVALO COM MUDANÇA DE SINAL

def encontrar_intervalo(E):

    if E >= 0:
        raise ValueError("E deve ser negativo.")

    # Começamos com um intervalo positivo
    a = 1e-10
    b = 1.0

    # Procuramos um intervalo [a,b]
    # onde exista mudança de sinal
    while f(a, E) * f(b, E) > 0:
        b *= 2

        if b > 1e10:
            raise RuntimeError(
                "Não foi possível encontrar um intervalo."
            )

    return a, b

# BISSECÇÃO

def bisseccao(E, max_iter=10000):

    a, b = encontrar_intervalo(E)

    fa = f(a, E)

    x_antigo = None

    for i in range(max_iter):

        x = (a + b) / 2
        fx = f(x, E)

        if x_antigo is not None:

            if convergiu(x, x_antigo):
                return x, i + 1

        if fa * fx <= 0:

            b = x

        else:

            a = x
            fa = fx

        x_antigo = x

    raise RuntimeError("Bissecção não convergiu.")
  
# FALSA POSIÇÃO

def falsa_posicao(E, max_iter=10000):

    a, b = encontrar_intervalo(E)

    fa = f(a, E)
    fb = f(b, E)

    x_antigo = None

    for i in range(max_iter):

        x = (a * fb - b * fa) / (fb - fa)

        fx = f(x, E)

        if x_antigo is not None:

            if convergiu(x, x_antigo):
                return x, i + 1

        if fa * fx <= 0:

            b = x
            fb = fx

        else:

            a = x
            fa = fx

        x_antigo = x

    raise RuntimeError("Falsa posição não convergiu.")

# NEWTON-RAPHSON

def newton_raphson(E, max_iter=1000):

    a, b = encontrar_intervalo(E)

    # Chute inicial
    x = (a + b) / 2

    for i in range(max_iter):

        x_novo = x - f(x, E) / df(x)

        # Evita valores inválidos
        if x_novo <= 0 or not math.isfinite(x_novo):
            x_novo = (a + b) / 2

        if convergiu(x_novo, x):
            return x_novo, i + 1

        # Mantém a raiz dentro do intervalo
        if f(a, E) * f(x_novo, E) <= 0:

            b = x_novo

        else:

            a = x_novo

        x = x_novo

    raise RuntimeError("Newton-Raphson não convergiu.")

# PROGRAMA PRINCIPAL

E = float(input("Digite um valor negativo para E: "))

if E >= 0:
    raise ValueError("O valor de E precisa ser negativo.")


# Executa os três métodos

x_bis, iter_bis = bisseccao(E)

x_fp, iter_fp = falsa_posicao(E)

x_newton, iter_newton = newton_raphson(E)


# RESULTADOS

print("\n========== QUESTÃO 9 ==========")

print(f"E = {E}")
print(f"eps da máquina = {eps:.17e}")


print("\nBissecção:")
print(f"x = {x_bis:.15f}")
print(f"Iterações = {iter_bis}")
print(f"f(x) = {f(x_bis, E):.3e}")


print("\nFalsa posição:")
print(f"x = {x_fp:.15f}")
print(f"Iterações = {iter_fp}")
print(f"f(x) = {f(x_fp, E):.3e}")


print("\nNewton-Raphson:")
print(f"x = {x_newton:.15f}")
print(f"Iterações = {iter_newton}")
print(f"f(x) = {f(x_newton, E):.3e}")
