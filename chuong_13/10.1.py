f=open(input('Nhập tên tập tin:\n'))
a=f.readlines()
f.close()
print('Nội dung tập tin:')
for i in a:
    print(i,end='')