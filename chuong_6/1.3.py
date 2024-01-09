cac_mat_hang={'con sâu':30000,
              'sữa vina milk':25000,
              'con sói':31000,
              'đá':500000,
              'áo lọt khe':100000
            }
print('có các mặt hàng sau:')
for i in cac_mat_hang:
    print(i,': ',cac_mat_hang[i])
a=input('nhập tên sản phẩm mà bạn muốn mua: ')
b=int(input('nhập sô lượng muốn mua: '))
so_tien_phai=str(cac_mat_hang[a]*b)
k=0
for i in range(len(so_tien_phai)-1,-1,-1):
    k+=1
    if k==3:
        if so_tien_phai[:i]!='':
            k=0
            so_tien_phai=so_tien_phai[:i]+','+so_tien_phai[i:]
print('tên mặt hàng: ',a)
print('số lượng: ',b)
print('đơn giá: ',cac_mat_hang[a])
print('tiền phải trả: ',so_tien_phai,'vnđ')
