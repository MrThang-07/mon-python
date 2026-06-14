print("========== BÀI 1: TÌM SẢN PHẨM THEO TÊN ==========")
products = [
    {"name": "Laptop", "price": 15000000},
    {"name": "Mouse", "price": 200000},
    {"name": "Keyboard", "price": 500000}
]

ten_tim_kiem = input("Nhập tên sản phẩm cần tìm: ").strip()
tim_thay = False

for p in products:
    if p["name"].lower() == ten_tim_kiem.lower():
        print(f"=> Giá của {p['name']} là: {p['price']} VNĐ")
        tim_thay = True
        break

if tim_thay == False:
    print("=> Không tìm thấy")


print("\n========== BÀI 2: LỌC HỌC SINH ĐẠT YÊU CẦU ==========")
students_b2 = [
    {"name": "An", "score": 8.5},
    {"name": "Bình", "score": 6.0},
    {"name": "Chi", "score": 9.0},
    {"name": "Dũng", "score": 5.5}
]

hoc_sinh_gioi = [] 

for hs in students_b2:
    if hs["score"] >= 8.0:
        hoc_sinh_gioi.append(hs) 

print("Danh sách học sinh đạt yêu cầu (Điểm >= 8.0):")
for hs in hoc_sinh_gioi:
    print(f"- {hs['name']} ({hs['score']} điểm)")


print("\n========== BÀI 3: TÍNH TỔNG TIỀN GIỎ HÀNG ==========")
cart = [
    {"name": "Sách", "price": 50000, "quantity": 2},
    {"name": "Bút", "price": 5000, "quantity": 10},
    {"name": "Vở", "price": 12000, "quantity": 5}
]

tong_toan_bo = 0

for item in cart:
    tien_tung_mon = item["price"] * item["quantity"]
    print(f"- {item['name']}: {item['quantity']} cái x {item['price']}đ = {tien_tung_mon}đ")
    
   
    tong_toan_bo += tien_tung_mon

print(f"Tổng tiền toàn bộ giỏ hàng: {tong_toan_bo}đ")


print("\n========== BÀI 4: THỐNG KÊ SINH VIÊN THEO LỚP ==========")
students_b4 = [
    {"name": "An", "class": "Python01"},
    {"name": "Bình", "class": "Python02"},
    {"name": "Chi", "class": "Python01"},
    {"name": "Dũng", "class": "Python03"},
    {"name": "Hà", "class": "Python02"}
]

thong_ke = {}

for hs in students_b4:
    ten_lop = hs["class"]
    
    if ten_lop in thong_ke:
        thong_ke[ten_lop] += 1
    # Nếu lớp chưa có thì tạo mới và gán bằng 1
    else:
        thong_ke[ten_lop] = 1

print("Kết quả thống kê:")
print(thong_ke)


print("\n========== BÀI 5: QUẢN LÝ KHO HÀNG ==========")
inventory = [
    {"id": 1, "name": "Laptop", "quantity": 5},
    {"id": 2, "name": "Mouse", "quantity": 20},
    {"id": 3, "name": "Keyboard", "quantity": 10}
]


san_pham_moi = {"id": 4, "name": "Monitor", "quantity": 15}
inventory.append(san_pham_moi)
print("=> Đã thêm Monitor vào kho.")


id_cap_nhat = 2
for sp in inventory:
    if sp["id"] == id_cap_nhat:
        sp["quantity"] = 50
        print(f"=> Đã cập nhật số lượng của id {id_cap_nhat}.")
        break


id_xoa = 3
for i in range(len(inventory)):
    if inventory[i]["id"] == id_xoa:
        inventory.pop(i)
        print(f"=> Đã xóa sản phẩm có id {id_xoa}.")
        break


print("\nDanh sách kho hàng hiện tại:")
for sp in inventory:
    print(f"ID: {sp['id']} | Tên: {sp['name']} | Số lượng: {sp['quantity']}")