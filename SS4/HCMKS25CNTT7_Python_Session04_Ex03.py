hoadon = int(input("Nhập số lượng hóa đơn trong ca : "))
max = 0 
min = 0
for i in range(1,hoadon + 1):
    giatri_hoadon =int(input(f"Nhập giá trị hóa đơn thứ {i} : "))
    if i == 1 :
        max = giatri_hoadon
        min = giatri_hoadon
    else :
        if max < giatri_hoadon :
            max = giatri_hoadon
        if min > giatri_hoadon :
            min = giatri_hoadon
print(f"Hóa đơn có giá trị cao nhất : {max} VND " )
print(f"Hóa đơn có giá trị thấp nhất : {min} VND")