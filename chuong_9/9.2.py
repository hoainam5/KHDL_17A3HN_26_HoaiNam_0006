nam=int(input("Nhập năm:"))
def tinh_can(nam):
    a=nam%10
    if a==0:
        can="Canh"
    if a==1:
        can="Tân"
    if a==2:
        can="Nhâm"
    if a==3:
        can="Quý"
    if a==4:
        can="Giáp"
    if a==5:
        can="Ất"
    if a==6:
        can="Bính"
    if a==7:
        can="Đinh"
    if a==8:
        can="Mậu"
    if a==9:
        can="Kỳ"
    return can
def tinh_chi(nam):
    a=nam%12
    if a==0:
        chi="Thân"
    if a==1:
        chi="Dậu"
    if a==2:
        chi="Tuất"
    if a==3:
        chi="Hợi"
    if a==4:
        chi="Tý"
    if a==5:
        chi="Sửu"
    if a==6:
        chi="Dần"
    if a==7:
        chi="Mão"
    if a==8:
        chi="Thìn"
    if a==9:
        chi="Tỵ"
    if a==10:
        chi="Ngọ"
    if a==11:
        chi="Mùi"
    return chi 
print("Năm",nam,"là",tinh_can(nam),tinh_chi(nam))