b=input('nhập tên tập tin:\n')
f=open(b,'w+',encoding='utf-8')
f.write(input('Nhập nội dung\n')+'\n')
while True:
    i=int(input('bạn có muốn tiếp tục ghi nộp dung vào file? 1: có; 0: Không\n'))
    if i==1:
        f.write(input('Nhập nội dung\n')+'\n')
    else:
        break
f.seek(0)
print(f'Đã ghi nội dung vào tập tin {b}')
a=f.read()
f.close()
print(a)