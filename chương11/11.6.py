a=[74,74,72,72,73,69,69,71,76,71]
a=[i*0.0254 for i in a ]
print(a)
print(f'ba chiều cao đầu tiên: {a[:3]}\nba chiều cao cuối cùng: {a[-3:]}')
print('chiều cao trung bình',sum(a)/len(a))
print('chiều cao lớn nhất',max(a))
print('chiều cao nhỏ nhất',min(a))
a.sort()
print('sắp xếp tăng dần',a)
a=a[::-1]
print('sắp sếp giảm dần',a)