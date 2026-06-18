# (1) Phân tích
# 1. Sơ đồ cấu trúc mối quan hệ kế thừa
# Hệ thống được thiết kế theo mô hình kiến trúc phân cấp chuẩn OOP:

# Champion (ABC): Đóng vai trò là lớp cơ sở trừu tượng (Abstract Base Class) tối cao. Lớp này định hình khung xương (thuộc tính chung champion_id, name, base_hp, base_atk và các toán tử).

# Warrior và Mage: Là các lớp con cụ thể (Concrete Classes) kế thừa toàn bộ các đặc tính sinh tồn từ Champion, đồng thời bổ sung các thuộc tính độc bản (shield_bonus của Warrior, ability_power của Mage) để cá nhân hóa lối chơi.
# 2. Tính Đa hình (Polymorphism) hoạt động ra sao?Phương thức calculate_skill_damage() là minh chứng rõ ràng nhất cho tính đa hình:Cơ chế: Máy chủ chỉ cần phát ra một tín hiệu duy nhất là gọi hàm calculate_skill_damage(). Tuy nhiên, tướng hệ Warrior sẽ phản hồi bằng sát thương vật lý gồng giáp ($ATK \times 2 + Giáp$), còn tướng hệ Mage sẽ phản hồi bằng sát thương phép bùng nổ ($ATK \times AP$).Lợi ích mở rộng: Sau này, khi Studio muốn cập nhật thêm hệ Assassin (Sát thủ) hay Ranger (Cung thủ), bạn chỉ cần tạo lớp con mới kế thừa từ Champion và viết riêng công thức tính sát thương vào hàm calculate_skill_damage(). Toàn bộ mã nguồn cốt lõi của máy chủ điều phối trận đấu và tính chiến lực không cần phải sửa đổi hay chèn thêm bất kỳ một dòng if-else nào!
# 3. Cơ chế hoạt động nạp chồng toán tử __add__ với số nguyên
# Khi thực hiện tính tổng chiến lực cả đội, chúng ta thường dùng hàm sum() hoặc một vòng lặp chạy từ biến tích lũy ban đầu bằng 0 (ví dụ: total = 0, sau đó total = total + champion).

# Để máy tính không ném ra lỗi TypeError khi lấy con số 0 (kiểu int) cộng với một đối tượng Champion, hàm __add__(self, other) cần phải kiểm tra kiểu dữ liệu một cách thông minh bằng phương thức isinstance().

# Nếu other là một quân cờ Champion, nó sẽ lấy chiến lực của self cộng với chiến lực của other. Nếu other là một con số (int hoặc float), nó sẽ cộng trực tiếp chiến lực của self với con số đó.         
# (2) Viết code     
from abc import ABC, abstractmethod

class Champion(ABC):
    """
    Lớp cơ sở trừu tượng (Abstract Base Class) đại diện cho một quân cờ tổng quát.
    Chứa các thuộc tính chung và các phép nạp chồng toán tử so sánh, tính toán chiến lực.
    """
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        
        # Bẫy lỗi 2: Tự động đưa về giá trị mặc định 100 nếu nhập số <= 0
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Phương thức trừu tượng tính sát thương kỹ năng.
        Bắt buộc các lớp con (hệ/tộc) phải tự override lại.
        """
        pass

    def get_combat_power(self):
        """
        Tính điểm chiến lực tổng hợp của quân cờ theo công thức:
        Chiến lực = HP + (Sát thương kỹ năng * 1.5)
        """
        return int(self.base_hp + (self.calculate_skill_damage() * 1.5))

    def __add__(self, other):
        """
        Nạp chồng toán tử + để cộng dồn điểm chiến lực.
        Hỗ trợ cộng giữa 2 Champion hoặc cộng dồn với một con số (int/float).
        """
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        """
        Nạp chồng toán tử cộng đảo ngược (Right-add).
        Giúp xử lý phép toán kiểu: 0 + Champion (phục vụ chạy vòng lặp sum từ số 0).
        """
        return self.__add__(other)

    def __gt__(self, other):
        """
        Nạp chồng toán tử > để so sánh điểm chiến lực giữa 2 quân cờ.
        """
        if not isinstance(other, Champion):
            return NotImplemented
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    """
    Lớp con cụ thể đại diện cho hệ Chiến binh (Warrior).
    Có thuộc tính riêng là lượng giáp cộng thêm (shield_bonus).
    """
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus if shield_bonus >= 0 else 0

    def calculate_skill_damage(self):
        """Ghi đè tính sát thương: ATK * 2 + Giáp cộng thêm"""
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    """
    Lớp con cụ thể đại diện cho hệ Pháp sư (Mage).
    Có thuộc tính riêng là hệ số sức mạnh phép thuật (ability_power).
    """
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power if ability_power > 0 else 1.0

    def calculate_skill_damage(self):
        """Ghi đè tính sát thương: ATK * Hệ số SMPT"""
        return self.base_atk * self.ability_power


# =========================================================================
# LUỒNG ĐIỀU PHỐI CHƯƠNG TRÌNH CHÍNH (MAIN APPLICATION)
# =========================================================================

# Bể tướng ban đầu (champion_pool) theo yêu cầu đề bài
champion_pool = [
    Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
    Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
    Mage("MAG01", "Rikkei Wizard", 800, 500, 1.5)
]

def find_champion_by_id(champ_id):
    """Hàm tiện ích quét tìm quân cờ trong bể tướng theo mã id."""
    for champ in champion_pool:
        if champ.champion_id == champ_id:
            return champ
    return None

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH AUTO-BATTLER =====")
        print("1. Hiển thị bể tướng hiện có")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực Đội Hình Ra Sân")
        print("5. Thoát chương trình")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
            print(f"{'Mã':<8} | {'Tên tướng':<18} | {'Hệ':<8} | {'HP':<5} | {'ATK':<5} | {'Chỉ số riêng':<15} | {'Chiến lực'}")
            print("-" * 85)
            for c in champion_pool:
                if isinstance(c, Warrior):
                    class_type = "Warrior"
                    unique_info = f"Armor: {c.shield_bonus}"
                else:
                    class_type = "Mage"
                    unique_info = f"AP: {c.ability_power}"
                
                print(f"{c.champion_id:<8} | {c.name:<18} | {class_type:<8} | {c.base_hp:<5} | {c.base_atk:<5} | {unique_info:<15} | {c.get_combat_power()}")
            print("-" * 85)
            
        elif choice == "2":
            print("\n--- THÊM QUÂN CỜ MỚI ---")
            print("1. Hệ Warrior (Chiến binh)")
            print("2. Hệ Mage (Pháp sư)")
            type_choice = input("Chọn hệ muốn tạo (1-2): ").strip()
            
            if type_choice not in ["1", "2"]:
                print("Hệ tướng lựa chọn không hợp lệ!")
                continue
                
            champ_id = input("Nhập mã tướng: ").strip().upper()
            
            # Bẫy lỗi 4: Chống trùng lặp mã ID quân cờ trong danh sách
            if find_champion_by_id(champ_id) is not None:
                print(f" Lỗi: Mã tướng '{champ_id}' đã tồn tại trong bể tướng!")
                continue
                
            name = input("Nhập tên tướng: ").strip()
            
            # Bẫy lỗi ngoại lệ try-except đề phòng người dùng nhập chữ vào ô số
            try:
                hp = int(input("Nhập HP: ").strip())
                atk = int(input("Nhập ATK: ").strip())
                
                if type_choice == "1":
                    armor = int(input("Nhập Armor (Giáp cộng thêm): ").strip())
                    new_champ = Warrior(champ_id, name, hp, atk, armor)
                else:
                    ap = float(input("Nhập Hệ số sức mạnh phép thuật (AP): ").strip())
                    new_champ = Mage(champ_id, name, hp, atk, ap)
                    
                champion_pool.append(new_champ)
                print(f"\nThêm tướng thành công!")
                print(f"Mã: {new_champ.champion_id} | Tên: {new_champ.name} | Chiến lực: {new_champ.get_combat_power()}")
                
            except ValueError:
                print("Lỗi: Sai kiểu dữ liệu! Vui lòng nhập số nguyên cho HP/ATK/Armor và số thập phân cho AP.")
                
        elif choice == "3":
            print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")
            id1 = input("Nhập mã tướng thứ nhất: ").strip().upper()
            id2 = input("Nhập mã tướng thứ hai: ").strip().upper()
            
            champ1 = find_champion_by_id(id1)
            champ2 = find_champion_by_id(id2)
            
            # Bẫy lỗi 3: Kiểm tra mã tướng có tồn tại hay không
            if champ1 is None:
                print(f"Mã tướng {id1} không hợp lệ, hủy bỏ so sánh!")
                continue
            if champ2 is None:
                print(f" Mã tướng {id2} không hợp lệ, hủy bỏ so sánh!")
                continue
                
            type1 = "Warrior" if isinstance(champ1, Warrior) else "Mage"
            type2 = "Warrior" if isinstance(champ2, Warrior) else "Mage"
            
            print("\nThông tin so sánh:")
            print(f"{champ1.champion_id} - {champ1.name} | Hệ: {type1} | Chiến lực: {champ1.get_combat_power()}")
            print(f"{champ2.champion_id} - {champ2.name} | Hệ: {type2} | Chiến lực: {champ2.get_combat_power()}")
            
            # Sử dụng nạp chồng toán tử > để so sánh trực tiếp 2 đối tượng
            if champ1 > champ2:
                print(f"\nKết quả: {champ1.champion_id} - {champ1.name} mạnh hơn {champ2.champion_id} - {champ2.name}.")
            elif champ2 > champ1:
                print(f"\nKết quả: {champ2.champion_id} - {champ2.name} mạnh hơn {champ1.champion_id} - {champ1.name}.")
            else:
                print("\nKết quả: Hai quân cờ có chiến lực ngang nhau!")
                
        elif choice == "4":
            print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")
            raw_input = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: ")
            
            # Tách chuỗi nhập vào thành danh sách các mã đơn lẻ
            input_ids = [champ_id.strip().upper() for champ_id in raw_input.split(",") if champ_id.strip()]
            
            if not input_ids:
                print("Danh sách nhập vào trống trống!")
                continue
                
            print("\nDanh sách đội hình:")
            total_power = 0
            count = 1
            
            for champ_id in input_ids:
                champ = find_champion_by_id(champ_id)
                
                # Bẫy lỗi 3: Nếu nhập mã sai, thông báo bỏ qua và chạy tiếp chứ không để sập app
                if champ is None:
                    print(f"{count}. [BỎ QUA] Mã tướng {champ_id} không tồn tại trong hệ thống!")
                    count += 1
                    continue
                    
                type_name = "Warrior" if isinstance(champ, Warrior) else "Mage"
                print(f"{count}. {champ.champion_id} - {champ.name} | Chiến lực: {champ.get_combat_power()}")
                
                # Kích hoạt toán tử nạp chồng + để cộng dồn trực tiếp object vào biến số nguyên
                total_power = total_power + champ
                count += 1
                
            print(f"\n Tổng chiến lực đội hình: {total_power}")
            
        elif choice == "5":
            print("\nCảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
            break
        else:
            print(" Lựa chọn không hợp lệ! Vui lòng chọn số từ 1 đến 5.")

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                          