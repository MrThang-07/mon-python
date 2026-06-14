# 1. Đánh giá hiện trạng hệ thống cũ (Legacy Code):
#    - Spaghetti Code: Gom toàn bộ logic vào một file script duy nhất, khó mở rộng.
#    - Vi phạm PEP 8: Đặt tên biến tối nghĩa (ds, p, l), mã không đồng nhất.
#    - Thiếu tính ổn định: Crash hệ thống khi nhập sai kiểu dữ liệu (lương) hoặc API trả về thiếu trường (status, salary).
#    - Không có khả năng truy vết: Thiếu hệ thống Logging để theo dõi các thao tác của Huấn luyện viên.
#    - Lỗi logic ẩn: Tính sai quỹ lương cho tuyển thủ dự bị (Benched).

# 2. Kế hoạch & Giải pháp Nâng cấp (Architecture & Refactoring):
#    - Clean Code & SRP: Chuẩn hóa tên biến theo snake_case. Áp dụng Single Responsibility (Đơn nhiệm) bằng cách tách logic tính lương ra hàm phụ trợ `calculate_actual_pay()`.
#    - Lập trình phòng thủ (Exception Handling): Tích hợp try...except (ValueError) kết hợp vòng lặp vô hạn để ép người dùng nhập đúng số liệu. Dùng phương thức `.get()` và bẫy KeyError để xử lý dữ liệu khuyết thiếu.
#    - Logging Strategy: Ghi log ra file `roster_app.log` với chế độ nối tiếp (filemode="a"), ghi rõ cấp độ INFO (thao tác thành công), WARNING (sai logic) và ERROR (lỗi dữ liệu).
#    - Unit Testing: Xây dựng test case độc lập bảo vệ công thức tính chia đôi lương, đảm bảo hệ thống không bị sai lệch khi nâng cấp về sau.

import logging
import os

# --- CẤU HÌNH LOGGING CHUẨN ---
thu_muc_hien_tai = os.path.dirname(__file__)
duong_dan_log = os.path.join(thu_muc_hien_tai, 'roster_app.log')

logging.basicConfig(
    filename=duong_dan_log,
    filemode="a",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# --- DỮ LIỆU BAN ĐẦU ---
roster = [
    {"player_id": "P01", "name": "Faker", "role": "Mid Lane", "salary": 5000.0, "status": "Active"},
    {"player_id": "P02", "name": "Oner", "role": "Jungle", "salary": 3500.0, "status": "Active"},
    {"player_id": "P03", "name": "Ruler", "role": "ADC", "salary": 6000.0, "status": "Benched"}
]



def display_roster(roster_list):
    """Chức năng 1: Hiển thị đội hình"""
    logging.info("Coach viewed the team roster.")
    
    if not roster_list:
        print("\nĐội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<12} | {'Trạng thái'}")
    print("-" * 80)
    
    for p in roster_list:
        # Bẫy 1: Dữ liệu rỗng KeyError cho trạng thái
        status = p.get("status", "Unknown")
        name_display = p["name"]
        
        if status == "Benched":
            name_display += " [DỰ BỊ]"
            
        print(f"{p['player_id']:<8} | {name_display:<20} | {p['role']:<15} | {p['salary']:<12,.1f} | {status}")


def sign_player(roster_list):
    """Chức năng 2: Chiêu mộ tuyển thủ"""
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    p_id = input("Nhập mã tuyển thủ: ").strip().upper()
    
    # Kiểm tra trùng mã
    for p in roster_list:
        if p["player_id"] == p_id:
            print(f"\nLỗi: Mã tuyển thủ {p_id} đã tồn tại.")
            logging.warning(f"Failed to sign player - Duplicate player ID {p_id}")
            return
            
    name = input("Nhập tên tuyển thủ: ").strip()
    role = input("Nhập vị trí thi đấu: ").strip()
    
    # Bẫy lỗi nhập lương
    while True:
        try:
            salary_input = float(input("Nhập mức lương hàng tháng: "))
            if salary_input <= 0:
                print("\nLương phải là số dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nLương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")
            
    new_player = {
        "player_id": p_id,
        "name": name,
        "role": role,
        "salary": salary_input,
        "status": "Active"
    }
    roster_list.append(new_player)
    
    print(f"\nThành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary_input}")


def update_player_status(roster_list):
    """Chức năng 3: Cập nhật lương & trạng thái"""
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    p_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()
    
    target_player = None
    for p in roster_list:
        if p["player_id"] == p_id:
            target_player = p
            break
            
    if not target_player:
        print(f"\nKhông tìm thấy tuyển thủ mang mã {p_id}.")
        logging.warning(f"Failed to update player - Player ID {p_id} not found")
        return
        
    print(f"\nTuyển thủ: {target_player['name']}")
    print(f"Vị trí: {target_player['role']}")
    print(f"Lương hiện tại: {target_player['salary']:,.1f}")
    print(f"Trạng thái hiện tại: {target_player['status']}")
    
    print("\nBạn muốn cập nhật:")
    print("1. Cập nhật lương")
    print("2. Cập nhật trạng thái thi đấu")
    choice = input("Chọn chức năng cập nhật (1-2): ").strip()
    
    if choice == "1":
        while True:
            try:
                new_salary = float(input("Nhập mức lương mới: "))
                if new_salary <= 0:
                    print("\nLương phải là số dương. Vui lòng nhập lại.")
                    continue
                old_salary = target_player["salary"]
                target_player["salary"] = new_salary
                print(f"\nThành công: Đã cập nhật lương cho tuyển thủ {p_id}.")
                logging.info(f"Updated player {p_id} salary from {old_salary} to {new_salary}")
                break
            except ValueError:
                print("\nLương phải là số hợp lệ. Vui lòng nhập lại.")
                
    elif choice == "2":
        print("\nChọn trạng thái mới:\n1. Active\n2. Benched")
        st_choice = input("Nhập lựa chọn trạng thái (1-2): ").strip()
        if st_choice == "1":
            target_player["status"] = "Active"
        elif st_choice == "2":
            target_player["status"] = "Benched"
        else:
            print("Lựa chọn không hợp lệ.")
            return
            
        print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {p_id}.")
        logging.info(f"Updated player {p_id} status to {target_player['status']}")
    else:
        print("Lựa chọn không hợp lệ.")


def calculate_actual_pay(player_dict):
    """
    Hàm Helper: Tính lương thực nhận (Benched nhận 50%)
    Có thể bứt ra để Unit Test độc lập.
    """
    salary = player_dict["salary"] # Sẽ ném KeyError nếu thiếu
    status = player_dict.get("status", "Active")
    
    if status == "Benched":
        return salary * 0.5
    return salary


def generate_payroll_report(roster_list):
    """Chức năng 4: Báo cáo quỹ lương"""
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    
    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return
        
    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | {'Lương thực nhận'}")
    print("-" * 80)
    
    total_payroll = 0.0
    for p in roster_list:
        try:
            actual_pay = calculate_actual_pay(p)
            total_payroll += actual_pay
            print(f"{p['player_id']:<8} | {p['name']:<15} | {p['status']:<10} | {p['salary']:<12,.1f} | {actual_pay:,.1f}")
        except KeyError as e:
            print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
            logging.error(f"Missing key while generating payroll report: {e}")
            
    print("-" * 80)
    print(f"Tổng quỹ lương hàng tháng: {total_payroll:,.1f}")
    logging.info(f"Generated monthly payroll report. Total: {total_payroll}")


# ==========================================
# MENU ĐIỀU HƯỚNG CHÍNH
# ==========================================
def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_roster(roster)
        elif choice == "2":
            sign_player(roster)
        elif choice == "3":
            update_player_status(roster)
        elif choice == "4":
            generate_payroll_report(roster)
        elif choice == "5":
            print("\nĐã thoát hệ thống. Tạm biệt!")
            logging.info("System closed and exited.")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")

if __name__ == "__main__":
    main()