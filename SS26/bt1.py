# (1) Phân tích
# Giải thích lỗi AttributeError tại dòng print(f"Chiến binh {w1.name}..."):

# Nguyên nhân: Trong Python, khi lớp con Warrior định nghĩa hàm khởi tạo __init__, nó đã vô tình ghi đè (override) hoàn toàn hàm khởi tạo của lớp cha Character. Vì lập trình viên cũ quên không gọi hàm super().__init__(name, hp, attack_power), bộ não của Python không hề chạy đoạn code gán self.name, self.hp, self.attack_power. Kết quả là đối tượng w1 sinh ra bị "rỗng ruột", hoàn toàn không tồn tại thuộc tính name trong bộ nhớ, dẫn đến sập nguồn.

# Cách gọi trực tiếp lớp cha không dùng super() (Không khuyến khích):

# Ta có thể gọi trực tiếp bằng tên lớp cha và truyền thủ công đối tượng self vào như thế này:
# Character.__init__(self, name, hp, attack_power)

# (Cách này không được khuyến khích vì nếu sau này lớp cha đổi tên hoặc dự án nâng cấp lên đa kế thừa, code sẽ bị gãy cấu trúc rất nguy hiểm).

# Lỗi xuất hiện tại dòng if w1 > w2: và lý do dấu > vô tác dụng:

# Nếu sửa xong Lỗi 1, chương trình sẽ sập tại đây với lỗi TypeError (cụ thể: TypeError: '>' not supported between instances of 'Warrior' and 'Warrior').

# Lý do: Python mặc định chỉ biết so sánh các kiểu dữ liệu nguyên bản của hệ thống (như số nguyên, số thực, chuỗi). Khi ta tự tạo ra một Class mới (Warrior), Python hoàn toàn không biết tiêu chí để bảo 1 chiến binh "lớn hơn" chiến binh khác là dựa vào lượng máu, dựa vào tên chữ cái, hay dựa vào giáp.

# Dunder method cần khai báo và số lượng tham số:

# Để kích hoạt dấu >, ta phải nạp chồng toán tử bằng Magic method __gt__ (Greater Than).

# Hàm này nhận vào đúng 2 tham số: self (đối tượng chiến binh bên trái dấu >) và other (đối tượng chiến binh bên phải dấu >).
# (2) Viết code 
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        if not isinstance(other, Warrior):
            return NotImplemented
        return self.get_total_power() > other.get_total_power()


w1 = Warrior("Arthur", 1000, 150, 50)
w2 = Warrior("Lancelot", 900, 180, 10)

print(f"Chiến binh {w1.name} xuất trận!")

if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")