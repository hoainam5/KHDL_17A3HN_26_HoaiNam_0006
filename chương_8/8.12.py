number = int(input("nhập số cần kiểm tra: "))
if number <= 1:
     print("không phải số nguyên tố")
for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("không phải số nguyên tố")
            break
        else:
            print("là số nguyên tố")
            break 
