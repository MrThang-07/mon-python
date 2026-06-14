# (1) Phân tích
# 1. Vấn đề của mã nguồn cũ (Legacy Code):
#    - Spaghetti Code: Nhồi nhét toàn bộ logic vào một vòng lặp while khổng lồ, vi phạm PEP 8.
#    - Crash hệ thống: Không có cơ chế bắt lỗi khi người dùng gõ chữ thay vì số (ValueError) hoặc khi API trả về thiếu dữ liệu (KeyError).
#    - Thiếu giám sát: Không có hệ thống Logging, không thể truy vết khi xảy ra lỗi.
#    - Lỗi logic (Bug ẩn): Tỷ số 0-0 tự động bị gán mác "Completed" sai nghiệp vụ.

# 2. Giải pháp Refactor & Nâng cấp áp dụng:
#    - Modularization: Tách các chức năng thành hàm độc lập (display, add, update, report) để dễ bảo trì.
#    - Exception Handling toàn diện: Sử dụng try...except bảo vệ hệ thống khỏi lỗi ép kiểu và dữ liệu bẩn từ API.
#    - Hệ thống Logging chuyên nghiệp: Ghi vết toàn bộ thao tác (INFO, WARNING, ERROR) vào file với `filemode="a"` (ghi nối tiếp không mất dữ liệu cũ). Đặt lệnh log chuẩn xác sau khi hoàn tất tiến trình.
#    - Defensive Programming & Testing: Thiết lập "bảo vệ vòng ngoài" (Early Return) cho hàm determine_winner() và tích hợp Unit Test để bảo vệ logic cốt lõi.
# ======================================================================
# (2) Viết code :




import logging

# CẤU HÌNH LOGGING
logging.basicConfig(
    filename='tournament_app.log',
    filemode = "a",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s",
    
)


matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]

def display_matches(match_list):
    
    logging.info("User viewed the match list.")
    
    if not match_list:
        print("\nHiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10} | {'Đội A':<15} | {'Đội B':<15} | {'Tỷ số':<7} | {'Trạng thái'}")
    print("-" * 70)
    
    for match in match_list:
        try:
            # Dùng try-except bẫy lỗi KeyError trường hợp API thiếu dữ liệu
            match_id = match["match_id"]
            team_a = match["team_a"]
            team_b = match["team_b"]
            score_a = match["score_a"]
            score_b = match["score_b"]
            status = match["status"]
            score_display = f"{score_a}-{score_b}"
            
            print(f"{match_id:<10} | {team_a:<15} | {team_b:<15} | {score_display:<7} | {status}")
        except KeyError as e:
            logging.error(f"Missing data key in match record: {e}")
            print(f"Lỗi: Hồ sơ trận đấu bị thiếu thông tin quan trọng ({e}).")

def add_match(match_list):
   
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    match_id = input("Nhập mã trận đấu: ").strip()
    
    if not match_id:
        print("\nMã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    for match in match_list:
        if match.get("match_id") == match_id:
            print(f"\nLỗi: Mã trận đấu {match_id} đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if not team_a or not team_b:
        print("\nTên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    match_list.append(new_match)
    
    print(f"\nThành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully.")

def get_valid_score(prompt):
    """
    Hàm phụ trợ: Ép người dùng nhập điểm số hợp lệ (số nguyên >= 0).
    """
    while True:
        try:
            score = int(input(prompt).strip())
            if score < 0:
                print("\nĐiểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score}")
                continue
            return score
        except ValueError as e:
            print("\nĐiểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: {e}")

def update_score(match_list):
   
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip().upper()
    
    target_match = None
    for match in match_list:
        if match.get("match_id") == match_id:
            target_match = match
            break

    if not target_match:
        print(f"\nKhông tìm thấy trận đấu mang mã {match_id}.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return

    print(f"\nTrận đấu: {target_match['team_a']} vs {target_match['team_b']} ({target_match['status']})")
    
    score_a = get_valid_score("Nhập điểm Đội A: ")
    score_b = get_valid_score("Nhập điểm Đội B: ")

    target_match["score_a"] = score_a
    target_match["score_b"] = score_b

    
    if score_a == 0 and score_b == 0:
        confirm = input("\nTỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").strip().lower()
        if confirm == 'y':
            target_match["status"] = "Completed"
        else:
            target_match["status"] = "Pending"
    else:
        target_match["status"] = "Completed"

    print(f"\nThành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logging.info(f"Match {match_id} score updated successfully.")

def determine_winner(match):
    """
    Hàm phụ trợ: Xác định kết quả trận đấu dựa trên dictionary truyền vào.
    Trả về tên đội thắng, 'Draw', hoặc 'Not Started'.
    """
    if match.get("status") == "Pending":
        return "Not Started"
        
    score_a = match.get("score_a", 0)
    score_b = match.get("score_b", 0)

    if score_a > score_b:
        return match.get("team_a")
    elif score_b > score_a:
        return match.get("team_b")
    else:
        return "Draw"

def generate_report(match_list):
    """
    Chức năng 4: Báo cáo thống kê giải đấu.
    Chỉ liệt kê các trận đã hoàn thành.
    """
    
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    
    completed_count = 0
    for match in match_list:
        if match.get("status") == "Completed":
            winner = determine_winner(match)
            team_a = match.get("team_a")
            team_b = match.get("team_b")
            score_a = match.get("score_a")
            score_b = match.get("score_b")
            
            print(f"{match['match_id']}: {team_a} {score_a}-{score_b} {team_b} | Kết quả: {winner}")
            completed_count += 1

    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")
        
    print(f"\nTổng số trận đã hoàn thành: {completed_count}")
    logging.info("User generated tournament report.")
def main():
    """
    Vòng lặp tương tác chính của hệ thống.
    Điều hướng menu và xử lý lỗi chọn sai chức năng.
    """
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_matches(matches)
        elif choice == "2":
            add_match(matches)
        elif choice == "3":
            update_score(matches)
        elif choice == "4":
            generate_report(matches)
        elif choice == "5":
            print("\nĐã thoát chương trình. Tạm biệt!")
            logging.info("System closed and exited.")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")
            logging.warning("Invalid menu choice selected.")

if __name__ == "__main__":
    main()