# bt 1

name = input("Nhập tên của bạn: ")
print(f"Hello, {name}")
# bt2

age = int(input("Nhập tuổi của bạn: "))
print(f"You are {age} years old")
# bt3

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
tong = a + b
print(f"Tổng của hai số là: {tong}")

# bt4

length = float(input("Nhập chiều dài: "))
width = float(input("Nhập chiều rộng: "))
area = length * width

print(f"Diện tích hình chữ nhật là: {area}")
# bt5
name = "John"
age = 20
score = 8.5
is_student = True
print(f"Kiểu dữ liệu của name: {type(name)}")
print(f"Kiểu dữ liệu của age: {type(age)}")
print(f"Kiểu dữ liệu của score: {type(score)}")
print(f"Kiểu dữ liệu của is_student: {type(is_student)}")
# bt6
r = float(input("Nhập bán kính r: "))
C = 2 * 3.14 * r
print(f"Chu vi hình tròn là: {C}")
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# bt7
phan_nguyen = a // b
phan_du = a % b
print(f"Phần nguyên của {a} chia {b} là: {phan_nguyen}")
print(f"Phần dư của {a} chia {b} là: {phan_du}")
# bt8
n = int(input("Nhập một số nguyên: "))
if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẻ")
    # bt9
age = int(input("Nhập tuổi: "))
if age >= 16:
    print("đủ tuổi làm căn cước công dân")
else:
    print("không đủ tuổi")
# bt10
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))

diem_tb = (toan + van + anh) / 3

print(f"Điểm trung bình là: {diem_tb}")
# bt11 
diem_tb = float(input("Nhập điểm trung bình: "))


if diem_tb >= 8.0:
    print("Xếp loại: Good")
elif diem_tb >= 6.5:
    print("Xếp loại: Fair")
elif diem_tb >= 5.0:
    print("Xếp loại: Average")
else:
    print("Xếp loại: Weak")

# bt12
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c

print(f"Số lớn nhất trong 3 số là: {so_lon_nhat}")
# bt14
n = int(input("Nhập số nguyên dương n: "))
print(f"Các số từ 1 đến {n} là:")
for i in range(1, n + 1):
    print(i, end=" ") 
print() 
# bt15
n = int(input("Nhập số nguyên dương n: "))

tong = 0

for i in range(1, n + 1):
    tong = tong + i  

print(f"Tổng các số từ 1 đến {n} là: {tong}")
# bt16
n = int(input("Nhập một số nguyên n: "))

print(f"--- BẢNG CỬU CHƯƠNG {n} ---")

for i in range(1, 11):
    ket_qua = n * i
    print(f"{n} x {i} = {ket_qua}")
# bt17

n = int(input("Nhập số nguyên dương n: "))

dem = 0

for i in range(1, n + 1):
    if i % 2 == 0: 
        dem += 1   

print(f"Từ 1 đến {n} có {dem} số chẵn.")
# bt18
chuoi = input("Nhập một chuỗi: ")
do_dai = len(chuoi)

print(f"Độ dài của chuỗi là: {do_dai}")
