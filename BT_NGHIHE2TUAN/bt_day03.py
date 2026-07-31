inventory = [
    {"id": "SP1", "ten": "Tai nghe Sony", "gia": 1200000, "danh_muc": "Phụ kiện"},
    {"id": "SP2", "ten": "Chuột không dây", "gia": 450000, "danh_muc": "Phụ kiện"},
    {"id": "SP3", "ten": "Bàn phím Cơ", "gia": 950000, "danh_muc": "Phụ kiện"},
    {
        "id": "SP4",
        "ten": "Màn hình Dell 27 inch",
        "gia": 4500000,
        "danh_muc": "Thiết bị",
    },
    {
        "id": "SP5",
        "ten": "Sạc dự phòng 20000mAh",
        "gia": 350000,
        "danh_muc": "Phụ kiện",
    },
]

students = [
    {"name": "An", "gpa": 7.2},
    {"name": "Bình", "gpa": 9.5},
    {"name": "Cường", "gpa": 6.8},
    {"name": "Dũng", "gpa": 8.4},
]


def linear_search_filter(cart, target_category, max_price):
    result = []
    for item in cart:
        if item["gia"] <= max_price and item["danh_muc"] == target_category:
            result.append(item)
    return result


def bubble_sort_students(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j]["gpa"] < arr[j + 1]["gpa"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


print("KẾT QUẢ LỌC SẢN PHẨM (LINEAR SEARCH MULTI-CRITERIA)")
danh_muc_tim = "Phụ kiện"
gia_toi_da = 1000000
print(f"Danh mục tìm kiếm: {danh_muc_tim} | Giá tối đa: {gia_toi_da:,} VNĐ")

ket_qua_loc = linear_search_filter(inventory, danh_muc_tim, gia_toi_da)
print(f"Tìm thấy {len(ket_qua_loc)} sản phẩm phù hợp:")
for sp in ket_qua_loc:
    print(f"  -> [{sp['id']}] {sp['ten']} | Giá: {sp['gia']:,} VNĐ")
print()


print("BẢNG XẾP HẠNG SINH VIÊN (BUBBLE SORT - GPA GIẢM DẦN)")
bubble_sort_students(students)
for index, sv in enumerate(students, start=1):
    print(f"Top {index}: {sv['name']} - {sv['gpa']} điểm")