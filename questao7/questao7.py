import math

# Função de iteração

def g(x, a):
    return x * (x**2 + 3 * a) / (3 * x**2 + a)

# Derivada da função de iteração

def g_prime(x, a):
    return 3 * (x**2 - a)**2 / (3 * x**2 + a)**2

# Método de ponto fixo

def ponto_fixo(a, x0, tol=1e-12, max_iter=100):

    if a <= 0:
        raise ValueError("O valor de a deve ser positivo.")

    if x0 == 0:
        raise ValueError(
            "x0 = 0 permanece em 0 e não converge para sqrt(a)."
        )

    x = x0
    raiz_exata = math.sqrt(a)

    print("Iteração       x                    Erro")
    print("-" * 55)

    for k in range(max_iter):

        x_novo = g(x, a)

        erro_iteracao = abs(x_novo - x)
        erro_exato = abs(x_novo - raiz_exata)

        print(
            f"{k + 1:3d}       "
            f"{x_novo:.15f}       "
            f"{erro_exato:.3e}"
        )

        if erro_iteracao <= tol:
            return x_novo, k + 1

        x = x_novo

    raise RuntimeError("O método não convergiu.")

# Dados do exemplo

a = 4.0
x0 = 1.0

raiz, iteracoes = ponto_fixo(a, x0)

# Resultados

raiz_exata = math.sqrt(a)

print("\n========== QUESTÃO 7 ==========")

print(f"a = {a}")
print(f"x0 = {x0}")

print(f"\nRaiz exata:")
print(f"sqrt(a) = {raiz_exata:.15f}")

print("\nAproximação:")
print(f"x = {raiz:.15f}")

print(f"\nNúmero de iterações = {iteracoes}")

print("\nAnálise da convergência:")

print(
    f"g'(sqrt(a)) = "
    f"{g_prime(raiz_exata, a):.3e}"
)

print(
    "\nComo g'(sqrt(a)) = 0, a convergência "
    "é mais rápida que uma convergência linear."
)
