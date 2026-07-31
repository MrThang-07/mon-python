orders = [
    {"id": "DH01", "name": "iPhone 15 Pro Max", "price": 32000000},
    {"id": "DH02", "name": "Tai nghe AirPods Pro", "price": 5500000},
    {"id": "DH03", "name": "MacBook Pro M3 Max", "price": 65000000},
    {"id": "DH04", "name": "Chuot khong day", "price": 450000},
    {"id": "DH05", "name": "Samsung Galaxy S24", "price": 22000000},
]

tong_doanh_thu = 0
so_don_vip = 0
don_cao_nhat = orders[0]
don_thap_nhat = orders[0]
is_suspicious = False
don_rui_ro = None

for order in orders:
    gia = order["price"]
    tong_doanh_thu += gia

    if gia >= 15000000:
        so_don_vip += 1

    if gia > don_cao_nhat["price"]:
        don_cao_nhat = order
    if gia < don_thap_nhat["price"]:
        don_thap_nhat = order

    if gia > 50000000:
        is_suspicious = True
        don_rui_ro = order

print("--- KẾT QUẢ BÀI 1 ---")
print(f"Tong doanh thu: {tong_doanh_thu:,} VND")
print(f"So don hang VIP (>= 15tr): {so_don_vip} don")
print(
    f"Don hang gia tri CAO NHAT: {don_cao_nhat['id']} - {don_cao_nhat['name']} ({don_cao_nhat['price']:,} VND)"
)
print(
    f"Don hang gia tri THAP NHAT: {don_thap_nhat['id']} - {don_thap_nhat['name']} ({don_thap_nhat['price']:,} VND)"
)
if is_suspicious and don_rui_ro:
    print(
        f"CANH BAO RUI RO: Phat hien don {don_rui_ro['id']} co gia tri {don_rui_ro['price']:,} VND > 50tr!"
    )
print(f"KET LUAN CAM CO: Co is_suspicious = {is_suspicious}\n")


students = [
    {
        "id": "SV01",
        "name": " Nguyen Van An ",
        "email": " an.nguyen@rikkei.edu.vn ",
        "phone": " 0987654321 ",
    },
    {
        "id": "SV02",
        "name": "Tran Thi Bich",
        "email": "bich_gmail.com",
        "phone": "0912345678",
    },
    {
        "id": "SV03",
        "name": "Le Hoang Cuong",
        "email": "cuong@gmail.com",
        "phone": "09876abcde",
    },
    {
        "id": "SV04",
        "name": "Pham Minh Dung",
        "email": "dung@gmail.com",
        "phone": "0355667788",
    },
]

print("--- KẾT QUẢ BÀI 2 ---")
for sv in students:
    name = sv["name"].strip()
    email = sv["email"].strip()
    phone = sv["phone"].strip()

    is_valid_email = (
        email.count("@") == 1
        and "@" in email
        and (email.endswith(".com") or email.endswith(".edu.vn"))
    )
    is_valid_phone = (
        len(phone) == 10 and phone.startswith("0") and phone.isdigit()
    )

    if is_valid_email and is_valid_phone:
        status = "HO SO HOP LE"
    elif not is_valid_email:
        status = "KHONG HOP LE (Thieu @)"
    else:
        status = "KHONG HOP LE (SDT chua chu)"

    print(
        f"[{sv['id']}] {name} | Email: {email} | SDT: {phone} -> {status}"
    )