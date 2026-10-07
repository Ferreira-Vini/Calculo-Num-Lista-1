import sys
import math

# Epsilon da máquina
eps = sys.float_info.epsilon


# Função da questão:
# -1/x^3 - 1/x^2 = E
#
# Transformamos em:
# f(x) = -1/x^3 - 1/x^2 - E = 0
def f(x, E):
    return -1 / x**3 - 1 / x**2 - E


# Derivada de f(x)
def df(x):
    return 3 / x**4 + 2 / x**3


# Critério de parada pedido no enunciado:
#
# |x_(n+1) - x_n| <= eps * max(1, |x_(n+1)|)
def convergiu(x_novo, x_antigo):
    return abs(x_novo - x_antigo) <= eps * max(1, abs(x_novo))


# Encontra automaticamente um intervalo [a, b]
# que contenha a raiz positiva.
def encontrar_intervalo(E):

    # Como E < 0
    # começamos com um limite superior positivo.
    b = max(1.0, 2 / math.sqrt(-E))

    # Queremos f(b) > 0
    while f(b, E) <= 0:
        b *= 2

    # Agora vamos diminuir b até encontrar
    # um ponto onde f(a) < 0.
    a = b

    while f(a, E) > 0:
        a /= 2

    return a, b

# MÉTODO DA BISSECÇÃO

def bisseccao(E, max_iter=10000):

    a, b = encontrar_intervalo(E)

    fa = f(a, E)

    x_antigo = None

    for i in range(1, max_iter + 1):

        x = (a + b) / 2
        fx = f(x, E)

        # Critério de parada
        if x_antigo is not None:
            if convergiu(x, x_antigo):
                return x, i

        # Atualização do intervalo
        if fa * fx <= 0:
            b = x
        else:
            a = x
            fa = fx

        x_antigo = x

    raise RuntimeError("Bissecção não convergiu.")

# MÉTODO DA FALSA-POSIÇÃO

def falsa_posicao(E, max_iter=10000):

    a, b = encontrar_intervalo(E)

    fa = f(a, E)
    fb = f(b, E)

    x_antigo = None

    for i in range(1, max_iter + 1):

        # Fórmula da falsa-posição
        x = (a * fb - b * fa) / (fb - fa)

        fx = f(x, E)

        # Critério de parada
        if x_antigo is not None:
            if convergiu(x, x_antigo):
                return x, i

        # Atualização do intervalo
        if fa * fx <= 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        x_antigo = x

    raise RuntimeError("Falsa-posição não convergiu.")

# MÉTODO DE NEWTON-RAPHSON

def newton_raphson(E, max_iter=1000):

    a, b = encontrar_intervalo(E)

    # Escolhemos o limite inferior como aproximação inicial.
    x = a

    for i in range(1, max_iter + 1):

        # Fórmula de Newton-Raphson
        x_novo = x - f(x, E) / df(x)

        # Critério de parada
        if convergiu(x_novo, x):
            return x_novo, i

        x = x_novo

    raise RuntimeError("Newton-Raphson não convergiu.")

# PROGRAMA PRINCIPAL

print("========== QUESTÃO 9 ==========")

E = float(input("Digite um valor negativo para E: "))

if E >= 0:
    raise ValueError("O valor de E deve ser negativo.")


# Encontrar intervalo
a, b = encontrar_intervalo(E)

print(f"\nE = {E}")
print(f"eps = {eps:.17e}")
print(f"Intervalo inicial = [{a:.15e}, {b:.15e}]")


# Bissecção
x_bis, iter_bis = bisseccao(E)

print("\n--- Bissecção ---")
print(f"x = {x_bis:.15e}")
print(f"f(x) = {f(x_bis, E):.3e}")
print(f"Iterações = {iter_bis}")


# Falsa-posição
x_fp, iter_fp = falsa_posicao(E)

print("\n--- Falsa-posição ---")
print(f"x = {x_fp:.15e}")
print(f"f(x) = {f(x_fp, E):.3e}")
print(f"Iterações = {iter_fp}")


# Newton-Raphson
x_newton, iter_newton = newton_raphson(E)

print("\n--- Newton-Raphson ---")
print(f"x = {x_newton:.15e}")
print(f"f(x) = {f(x_newton, E):.3e}")
print(f"Iterações = {iter_newton}")


# Comparação
print("\n========== COMPARAÇÃO ==========")
print(f"Bissecção:       {iter_bis} iterações")
print(f"Falsa-posição:   {iter_fp} iterações")
print(f"Newton-Raphson:  {iter_newton} iterações")
