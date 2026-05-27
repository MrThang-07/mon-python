total_money = int(input("Nhập tổng tiền hóa đơn ban đầu : "))

if (total_money >= 500000) :
    total_monneygiam = total_money * 0.1
    total_money  = total_money - (total_money * 0.1)
else :
    total_monneygiam = total_money * 0 
print("Số tiền được giảm : ", total_monneygiam,"VND")
print("Tổng tiền khách phải trả là : ",total_money,"VND")
    
