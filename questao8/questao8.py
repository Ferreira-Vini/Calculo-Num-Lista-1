import math

# DADOS DO PROBLEMA

a = 0.401
b = 42.7e-6

N = 1000
T = 300
p = 3.5e7

k = 1.3806503e-23

tol = 1e-12

# FUNÇÃO

def f(V):
    return (
        p + a * (N / V) ** 2
    ) * (V - N * b) - k * N * T

# DERIVADA

def df(V):
    return (
        p
        + a * (N / V) ** 2
        - 2 * a * N**2 * (V - N * b) / V**3
    )

# BISSECÇÃO

def bisseccao(Va, Vb, tol=1e-12, max_iter=1000):

    fa = f(Va)

    for i in range(max_iter):

        V = (Va + Vb) / 2
        fV = f(V)

        if abs(Vb - Va) / 2 <= tol:
            return V, i + 1

        if fa * fV <= 0:
            Vb = V
        else:
            Va = V
            fa = fV

    raise RuntimeError("Bissecção não convergiu.")

# FALSA POSIÇÃO

def falsa_posicao(Va, Vb, tol=1e-12, max_iter=10000):

    fa = f(Va)
    fb = f(Vb)

    V_anterior = None

    for i in range(max_iter):

        V = (Va * fb - Vb * fa) / (fb - fa)
        fV = f(V)

        if V_anterior is not None:
            if abs(V - V_anterior) <= tol:
                return V, i + 1

        if fa * fV <= 0:
            Vb = V
            fb = fV
        else:
            Va = V
            fa = fV

        V_anterior = V

    raise RuntimeError("Falsa posição não convergiu.")

# NEWTON-RAPHSON

def newton_raphson(V0, tol=1e-12, max_iter=100):

    V = V0

    for i in range(max_iter):

        V_novo = V - f(V) / df(V)

        if abs(V_novo - V) <= tol:
            return V_novo, i + 1

        V = V_novo

    raise RuntimeError("Newton-Raphson não convergiu.")

# INTERVALO E CHUTE INICIAL

# O volume precisa ser maior que N*b
limite_inferior = N * b

# Limite superior escolhido para obter mudança de sinal
limite_superior = 0.1

# EXECUÇÃO DOS MÉTODOS

V_bis, iter_bis = bisseccao(
    limite_inferior,
    limite_superior,
    tol
)

V_fp, iter_fp = falsa_posicao(
    limite_inferior,
    limite_superior,
    tol
)

V_newton, iter_newton = newton_raphson(
    1.1 * limite_inferior,
    tol
)

# RESULTADOS

print("========== QUESTÃO 8 ==========")

print("\nBissecção:")
print(f"Volume = {V_bis:.15e} m³")
print(f"Iterações = {iter_bis}")
print(f"f(V) = {f(V_bis):.3e}")

print("\nFalsa posição:")
print(f"Volume = {V_fp:.15e} m³")
print(f"Iterações = {iter_fp}")
print(f"f(V) = {f(V_fp):.3e}")

print("\nNewton-Raphson:")
print(f"Volume = {V_newton:.15e} m³")
print(f"Iterações = {iter_newton}")
print(f"f(V) = {f(V_newton):.3e}")
