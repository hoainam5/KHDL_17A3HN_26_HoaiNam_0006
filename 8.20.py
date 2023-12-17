import math

def taylor_approximation(x, tolerance=1e-4):
    result = 1.0  
    term = x      
    n = 1
    while abs(term) > tolerance:
        result += term
        n += 1
        term = (term * x) / n
    return result
x_value = int(input('nhập x : '))
approximation = taylor_approximation(x_value)

print(f"Giá trị gần đúng: {round(approximation,5)}")