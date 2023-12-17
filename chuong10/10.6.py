import cmath

def solve_quadratic_equation(a, b, c):
    # Tính delta
    delta = cmath.sqrt(b**2 - 4*a*c)

    # Tính nghiệm
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)

    return x1, x2

# Nhập hệ số của phương trình bậc 2
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm giải phương trình và hiển thị kết quả
solutions = solve_quadratic_equation(a, b, c)

print(f"Phương trình {a}x^2 + {b}x + {c} = 0 có nghiệm:")
print(f"Nghiệm x1: {solutions[0]}")
print(f"Nghiệm x2: {solutions[1]}")
