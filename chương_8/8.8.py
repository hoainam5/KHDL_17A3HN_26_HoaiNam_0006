room = int(input('nhập số phòng: '))
if room == 1:t=1260000
if room == 2:t=1550000
if room == 3:t=1830000
if room == 4:t=1830000
if room == 5:t=2120000
if room == 6:t=2120000
if room == 7:t=2540000
if room == 8:t=4800000
dem = int(input('nhập số đêm: '))
tien = t*dem
if dem >=2 and dem <= 3:
    tien=t*dem-t*dem*25/100
elif dem >=4:
    tien=t*dem-t*dem*30/100
print(f'số tiền phải trả {int(tien)}')