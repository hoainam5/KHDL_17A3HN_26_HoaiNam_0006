from datetime import datetime
import calendar
day=int(input('Nhập ngày:'))
month=int(input('nhập tháng:'))
year=int(input('Nhập năm:'))
print('Ngày tháng năm vừa nhập là:',datetime(year,month,day))
if calendar.isleap(year):
    print(f'năm {year} là năm nhuận')
else:
    print(f'năm {year} không phải là năm nhuận')
days_of_week = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
print(f'{day} - {month} - {year} là {days_of_week[calendar.weekday(year,month,day)]}')
print(f'Số ngày trong tháng {month} là:',calendar.monthrange(year, month)[1])