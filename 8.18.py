def is_perfect_number(number):
    if number <= 0:
        return False

    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == number

num = int(input("Nhập một số nguyên dương: "))

if is_perfect_number(num):
    print(f"{num} là số hoàn hảo.")
else:
    print(f"{num} không phải là số hoàn hảo.")
