câu 1 :
mssv = input("Nhập mã số sinh vien :")
que_quan = input("Nhập quê quán  ( tên tỉnh / thành phố) : ")
vung_1 = ["Hà Nội","TP.HCM"]
vung_2 = ["Đà Nẵng", "Hải Phòng","Cần Thơ"]
if que_quan in vung_1 :
    vung = "Vùng 1"
elif que_quan in vung_2 :
    vung = "Vùng 2"
else :
    vung = "Mở Rộng"

print(f"Sinh viên có MSSV{mssv.upper()} thuộc vùng tuyển sinh {vung}")

so_ky_tu = len(que_quan.replace(" ", ""))
print(f"Tổng số ký tự của quê quán (không tính khoảng trắng) là: {so_ky_tu}")

câu 2 :
chieu_cao = [1.65 , 1.72, 1.58, 1.80, 1.60, 1.75, 1.68]

chieu_cao.append(1.85)
chieu_cao.insert(2, 1.63)
chieu_cao.sort()
print("Danh sách sau khi sắp xếp :",chieu_cao)

tuple_max_min = (max(chieu_cao) , min(chieu_cao))
print("tuple : ",tuple_max_min)

câu 3 :
san_pham = int(input("Nhạt số lượng sản phẩm hoàn thành : "))
tien_thuong = 0
thong_bao = ""
if san_pham < 100 :
    tien_thuong = 0
    thong_bao = "Không có tiền thưởng (0 VND)."
elif 100 <= san_pham < 150:
    so_sp_thuong = san_pham - 99 
    tien_thuong = so_sp_thuong * 50000
    thong_bao = "Thưởng 50,000 VND trên mỗi sản phẩm "
else :
    tien_thuong = 3000000
    thong_bao = "Thưởng cố định trọn gói (Từ 150 sản phẩm trở lên)"

print(f"Số tiền thưởng năng suất nhân viên nhận được: {tien_thuong:,} VND")
print(f"Thông báo: {thong_bao}")

# câu 4 
chuoi_dau_vao = input("Nhập vào chuỗi các số nguyên (cách nhau bằng dấu cách):")
danh_sach_chuoi = chuoi_dau_vao.split()
danh_sach_goc = []
for chuoi in danh_sach_chuoi:
    so_nguyen = int(chuoi)
    danh_sach_goc.append(so_nguyen)

danh_sach_1 = []
danh_sach_2 = []

for so in danh_sach_goc:
    if so < 0 and so % 2 != 0:
        danh_sach_1.append(so)
    if so % 3 == 0:
        danh_sach_2.append(so)

print(f"Danh sách 1 (Các số lẻ âm): {danh_sach_1} | Số lượng: {len(danh_sach_1)}")
print(f"Danh sách 2 (Các số chia hết cho 3): {danh_sach_2} | Số lượng: {len(danh_sach_2)}")


