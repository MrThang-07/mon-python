# (1) Phân tích
# Tính Đa hình (Polymorphism) thể hiện qua vòng lặp for:

# Vòng lặp for hero in team_heroes: hero.use_ultimate() thể hiện tính đa hình ở chỗ: Hệ thống máy chủ phát ra cùng một thông điệp (gọi tên hàm use_ultimate()), nhưng các đối tượng khác nhau (Mage và Assassin) sẽ tự động phản hồi theo các cách khác nhau (Pháp sư thì gọi ra Mưa Sao Băng, Sát thủ thì kích hoạt Ám Sát). Máy chủ hoàn toàn không cần quan tâm hay kiểm tra class cụ thể của từng hero, chỉ cần biết chúng đều tuân theo khuôn mẫu của Hero.

# Thời điểm văng lỗi của code cũ và thảm họa trải nghiệm:

# Ở code cũ, game chỉ văng lỗi vào thời điểm Runtime khi giao tranh tổng đã bắt đầu và vòng lặp chạy đến đối tượng Assassin.

# Thảm họa: Việc báo lỗi muộn này là thảm họa vì người chơi đã tốn thời gian tìm trận, đợi loading, chuẩn bị chiến thuật xong xuôi, rồi game mới bất ngờ crash văng ra ngoài. Đối với nhà phát hành, lỗi này cực khó dò vì nếu người chơi không chọn tướng Assassin thì game không sập, dẫn đến việc lọt lưới các lỗi nghiêm trọng khi phát hành.

# Thời điểm văng lỗi khi dùng thư viện abc:

# Khi áp dụng chuẩn ABC và @abstractmethod, nếu lớp Assassin quên ghi đè hàm use_ultimate(), Python sẽ chặn đứng chương trình và văng lỗi TypeError ngay tại thời điểm khởi tạo đối tượng (Lúc loading ván đấu: Assassin()). Bạn thậm chí không thể tạo ra cái xác của đối tượng đó để nhét vào danh sách team_heroes.

# Nguyên lý Fail Fast thể hiện ra sao?

# Nguyên lý Fail Fast (Thất bại sớm) quy định rằng hệ thống phải báo lỗi ngay khi có sai sót nhỏ nhất xuất hiện, thay vì để nó âm thầm chạy tiếp rồi phát nổ sau đó. Áp dụng ABC giúp lập trình viên phát hiện ra việc thiếu code ngay từ giai đoạn lắp ráp trận đấu (Compile/Initialization time), đảm bảo code đẩy lên máy chủ luôn toàn vẹn cấu trúc 100%.
# (2) Viết  code
from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def use_ultimate(self):
        pass


class Mage(Hero):
    def use_ultimate(self):
        print( "Pháp Sư tung chiêu: MƯA SAO BĂNG!")


class Assassin(Hero):
    def use_ultimate(self):
        print("Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


print("--- LOADING TRẬN ĐẤU ---")
team_heroes = [Mage(), Assassin()]
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
for hero in team_heroes:
    hero.use_ultimate()