from module10_2 import *
f=open(input('Nhập tên tập tin:\n'))
a=f.read()
f.close()
print(a)
print('-----Report: Lines/ Words/ Chars-----')
print(f'Lines: {dong(a)}, Words: {tu(a)}, chars: {kitu(a)}')