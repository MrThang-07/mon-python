raw_cart = [
    {"id": "SP1", "ten": " Áo sơ mi nam ", "gia": 150000, "sl": 2, "danh_muc": "Thời trang"},
    {"id": "SP2", "ten": "Quần tây ", "gia": 250000, "sl": 1, "danh_muc": "Thời trang"},
    {"id": "SP3", "ten": " Giày thể thao ", "gia": 450000, "sl": 1, "danh_muc": "Giày dép"},
    {"id": "SP4", "ten": "Tất cổ ngắn ", "gia": 30000, "sl": 5, "danh_muc": "Phụ kiện"}
]

for item in raw_cart:
    item["ten"] = item["ten"].strip()
    item["tong_tien"] = item["gia"] * item["sl"]

raw_cart.append({
    "id": "SP5",
    "ten": "Áo khoác",
    "gia": 320000,
    "sl": 1,
    "danh_muc": "Thời trang",
    "tong_tien": 320000
})

for item in raw_cart[:]:
    if item["id"] == "SP4":
        raw_cart.remove(item)

print("--- KẾT QUẢ BÀI 1 ---")
print("[")
for item in raw_cart:
    print(f"  {item},")
print("]\n")

danh_muc_duy_nhat = {item["danh_muc"] for item in raw_cart}
sp_lon_hon_200k = [item["ten"] for item in raw_cart if item["tong_tien"] > 200000]

print("--- KẾT QUẢ BÀI 2 ---")
print(f"Danh mục duy nhất (Set): {danh_muc_duy_nhat}")
print(f"Sản phẩm > 200k (List Comprehension): {sp_lon_hon_200k}")