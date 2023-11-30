import cmath

def solve_quadratic_equation(a, b, c):
    # Tính delta
    delta = cmath.sqrt(b**2 - 4*a*c)
    print(delta)
    # Tính nghiệm
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)

    return abs(x1), abs(x2)

a = 1
b = -3
c = 2

solutions = solve_quadratic_equation(a, b, c)

print(f"Phương trình bậc 2: {a}x^2 + {b}x + {c} = 0")
print(f"Nghiệm x1: {solutions[0]}")
print(f"Nghiệm x2: {solutions[1]}")
