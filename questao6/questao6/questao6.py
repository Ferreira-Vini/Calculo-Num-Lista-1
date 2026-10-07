import math

# Dados do problema
l2 = 10
l1 = 8
gamma = 3 * math.pi / 5


# Função da equação não linear
def f(alpha):
    beta = math.pi - gamma - alpha

    return (
        l2 * math.cos(beta) / math.sin(beta) ** 2
        - l1 * math.cos(alpha) / math.sin(alpha) ** 2
    )


# Derivada da função
def df(alpha):
    beta = math.pi - gamma - alpha

    return (
        l2 * (1 + math.cos(beta) ** 2) / math.sin(beta) ** 3
        + l1 * (1 + math.cos(alpha) ** 2) / math.sin(alpha) ** 3
    )


# Método de Newton-Raphson
def newton_raphson(alpha0, tol=1e-12, max_iter=100):
    alpha = alpha0

    for k in range(max_iter):
        alpha_new = alpha - f(alpha) / df(alpha)
        erro = abs(alpha_new - alpha)

        if erro <= tol:
            return alpha_new, k + 1

        alpha = alpha_new

    raise RuntimeError("Newton-Raphson não convergiu.")


# Método da bissecção
def bisseccao(a, b, tol=1e-12, max_iter=1000):
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError("O intervalo não possui mudança de sinal.")

    x_antigo = None

    for k in range(max_iter):
        x = (a + b) / 2
        fx = f(x)

        if x_antigo is not None and abs(x - x_antigo) <= tol:
            return x, k + 1

        if fa * fx <= 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        x_antigo = x

    raise RuntimeError("Bissecção não convergiu.")


# Newton-Raphson
alpha_newton, iter_newton = newton_raphson(0.5)

# Bissecção
alpha_bisseccao, iter_bisseccao = bisseccao(0.5, 0.6)


# Cálculo do comprimento da barra
beta = math.pi - gamma - alpha_newton

L = (
    l2 / math.sin(beta)
    + l1 / math.sin(alpha_newton)
)


# Resultados
print("========== QUESTÃO 6 ==========")

print("\nNewton-Raphson:")
print(f"alpha = {alpha_newton:.15f} rad")
print(f"alpha = {math.degrees(alpha_newton):.10f} graus")
print(f"Iterações = {iter_newton}")
print(f"f(alpha) = {f(alpha_newton):.3e}")

print("\nBissecção:")
print(f"alpha = {alpha_bisseccao:.15f} rad")
print(f"Iterações = {iter_bisseccao}")
print(f"f(alpha) = {f(alpha_bisseccao):.3e}")

print("\nComprimento máximo da barra:")
print(f"L = {L:.15f}")
