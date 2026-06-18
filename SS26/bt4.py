# 1. Phân tích bài toán 
# Input (Dữ liệu và hành động đầu vào):

# Thông tin khởi tạo sinh vật: name (chuỗi), bonus_atk (số nguyên), bonus_speed (số nguyên).

# Hành động tương tác: Toán tử cộng + giữa hai đối tượng với nhau (obj1 + obj2) hoặc giữa đối tượng với một kiểu dữ liệu khác (obj1 + 100).

# Output (Kết quả xuất ra):

# Giao diện Console hiển thị danh sách đội hình kèm chỉ số đặc trưng tương ứng của từng loài.

# Trả về một đối tượng sinh vật mới có cùng Class sau khi lai tạo thành công (Tên ghép, Cấp độ + 1, Chỉ số cộng dồn).

# Chuỗi văn bản mô tả hành động tung chiêu thức khi kích hoạt Đa hình.

# Ngăn chặn và văng ra lỗi hệ thống (TypeError) khi vi phạm quy tắc thiết kế kiến trúc.

# 2. Đề xuất giải pháp (Architecture & Logic)
# Vượt bẫy 1 (Chặn khởi tạo trực tiếp lớp cha): Sử dụng thư viện abc biến Companion thành một Abstract Base Class. Bằng việc gắn decorator @abstractmethod cho hàm unleash_skill(), Python sẽ chặn đứng ngay lập tức bất kỳ nỗ lực nào muốn New một đối tượng Companion trơ trọi.

# Vượt bẫy 2 (Dị giáo lai tạo): Trong phương thức nạp chồng toán tử __add__(self, other), ta không dùng isinstance() vì hàm đó chấp nhận cả lớp con kế thừa. Ta phải sử dụng điều kiện nghiêm ngặt: type(self) == type(other). Nếu sai, lập tức chủ động raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!").

# Vượt bẫy 3 (Nút thắt MRO & Đa kế thừa của Dragon): Để luồng chạy __init__ của Dragon có thể đi xuyên suốt qua cả hai nhánh Pet và Mount mà không bị đứt gánh giữa đường, chúng ta bắt buộc phải áp dụng kiến trúc Kế thừa hợp tác (Cooperative Inheritance) bằng cách sử dụng tham số từ khóa kwargs phối hợp cùng super().__init__(kwargs).
# 2. Viết code 
from abc import ABC, abstractmethod

class Companion(ABC):
    def __init__(self, name, level=1, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.level = level

    @abstractmethod
    def unleash_skill(self):
        pass

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")
        
        new_name = f"{self.name} {other.name}"
        new_level = max(self.level, other.level) + 1
        
        if isinstance(self, Dragon):
            return Dragon(
                name=new_name,
                level=new_level,
                bonus_atk=self.bonus_atk + other.bonus_atk,
                bonus_speed=self.bonus_speed + other.bonus_speed
            )
        elif isinstance(self, Pet):
            return Pet(name=new_name, level=new_level, bonus_atk=self.bonus_atk + other.bonus_atk)
        elif isinstance(self, Mount):
            return Mount(name=new_name, level=new_level, bonus_speed=self.bonus_speed + other.bonus_speed)


class Pet(Companion):
    def __init__(self, name, bonus_atk, level=1, **kwargs):
        super().__init__(name=name, level=level, **kwargs)
        self.bonus_atk = bonus_atk

    def unleash_skill(self):
        print(f">> {self.name} gầm gừ: Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")


class Mount(Companion):
    def __init__(self, name, bonus_speed, level=1, **kwargs):
        super().__init__(name=name, level=level, **kwargs)
        self.bonus_speed = bonus_speed

    def unleash_skill(self):
        print(f">> {self.name} hí vang: Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")


class Dragon(Pet, Mount):
    def __init__(self, name, bonus_atk, bonus_speed, level=1):
        super().__init__(name=name, level=level, bonus_atk=bonus_atk, bonus_speed=bonus_speed)

    def unleash_skill(self):
        print(f">> {self.name} thị uy:")
        Pet.unleash_skill(self)
        Mount.unleash_skill(self)


# =========================================================================
# KỊCH BẢN CHẠY THỬ NGHIỆM ĐỂ KIỂM TRA CHỐNG BẪY HỆ THỐNG
# =========================================================================

if __name__ == "__main__":
    print("--- KIỂM TRA BẪY 1: KHỞI TẠO LỚP TRỪU TƯỢNG ---")
    try:
        c = Companion("Lỗi")
    except TypeError as e:
        print(f" Thành công bẫy được lỗi ABC: {e}\n")

    print("--- KHỞI TẠO DỮ LIỆU THỬ NGHIỆM ---")
    p1 = Pet("Sói Trắng", bonus_atk=50)
    p2 = Pet("Sói Đen", bonus_atk=60)
    m1 = Mount("Hắc Mã", bonus_speed=20)
    
    print(f"Khởi tạo {p1.name} thành công.")
    print(f"Khởi tạo {p2.name} thành công.")
    print(f"Khởi tạo {m1.name} thành công.\n")

    print("--- KIỂM TRA TÍNH NĂNG LAI TẠO HỢP LỆ ---")
    p3 = p1 + p2
    print(f">> Lai tạo thành công! Nhận được: {p3.name} (Cấp {p3.level}, Atk: +{p3.bonus_atk})\n")

    print("--- KIỂM TRA BẪY 2: DỊ GIÁO LAI TẠO (SAI LOÀI / SAI KIỂU) ---")
    try:
        error_mix = p1 + m1
    except TypeError as e:
        print(f"Thành công bẫy được lỗi sai loài: {e}")
        
    try:
        error_int = p1 + 100
    except TypeError as e:
        print(f"Thành công bẫy được lỗi cộng với số: {e}\n")

    print("--- KIỂM TRA BẪY 3: ĐA KẾ THỪA MRO CỦA ĐỐI TƯỢNG DRAGON ---")
    d1 = Dragon("Rồng Lửa", bonus_atk=500, bonus_speed=200)
    print(f"Khởi tạo {d1.name} thành công.")
    print(f" -> Chỉ số tấn công (Atk): +{d1.bonus_atk}")
    print(f" -> Chỉ số tốc độ (Speed): +{d1.bonus_speed}\n")

    print("--- KIỂM TRA TÍNH ĐA HÌNH (POLYMORPHISM) KHI XUẤT CHIẾN ---")
    equipped = [p3, m1, d1]
    for idx, beast in enumerate(equipped, 1):
        if isinstance(beast, Dragon):
            type_label = "Dragon"
        elif isinstance(beast, Pet):
            type_label = "Pet"
        else:
            type_label = "Mount"
        
        atk_info = f" | Atk: +{beast.bonus_atk}" if hasattr(beast, "bonus_atk") else ""
        speed_info = f" | Speed: +{beast.bonus_speed}" if hasattr(beast, "bonus_speed") else ""
        print(f"{idx}. [{type_label}] {beast.name} | Cấp: {beast.level}{atk_info}{speed_info}")
        
    print("\n--- KÍCH HOẠT TRẠNG THÁI CHIẾN ĐẤU (UNLEASH SKILL) ---")
    for beast in equipped:
        beast.unleash_skill()