import sympy as sp

# déclaration des variables symboliques
k, dt, dx, theta = sp.symbols('k dt dx theta')

# définition de r
r = k*dt/dx**2

# définition du facteur d'amplification
A = 1 - 2*r*(1-sp.cos(theta))

print(A)

x,dx = sp.symbols('x dx')

T = sp.Function('T')

developpement = sp.series(
    T(x+dx),
    dx,
    0,
    3
)

print(developpement)