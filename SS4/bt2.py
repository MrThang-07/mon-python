tongdoanh_thu = 0
cout = 0
for i in range(1,8):
    doanh_thu=int(input(f"Nhập doanh thu ngày {i}: "))
    if doanh_thu >= 5000000 :
        cout += cout + 1
    tongdoanh_thu += doanh_thu
print("Tổng doanh thu cả tuần : ",tongdoanh_thu)
print("Doanh thu trung bình mỗi ngày : ", tongdoanh_thu/7)
print("Số ngày đạt doanh thu mục tieu (>= 5000000 VND) :",cout ,"ngày")

