def f(x):
  return x ** 2 + 1


def g(x):
  return 2 * x - 3


def composicao_fg(x):
  return f(g(x))


def composicao_gf(x):
  return g(f(x))


def composicao_ff(x):
  return f(f(x))


def composicao_gg(x):
  return g(g(x))


x = int(4)
resultado_fg = composicao_fg(x)
resultado_gf = composicao_gf(x)
resultado_ff = composicao_ff(x)
resultado_gg = composicao_gg(x)


print(x)
print(resultado_fg)
print(resultado_gf)
print(resultado_gg)
print(resultado_ff)