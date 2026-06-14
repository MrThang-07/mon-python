# (1) Phân tích
# 1. Vấn đề của mã nguồn cũ (Legacy Code):
#    - Crash hệ thống: Lỗi chia cho 0 (ZeroDivisionError) khi tuyển thủ có Deaths = 0.
#    - Crash dữ liệu: Lỗi ép kiểu (ValueError) khi API trả về chữ thay vì số.
#    - Vi phạm Clean Code: Tên biến tối nghĩa (ds, x, k, d..); dồn cục logic tính toán và in ấn vào cùng một chỗ.

# 2. Giải pháp Refactor áp dụng:
#    - Self-documenting code: Đổi tên biến thành tiếng Anh chuẩn, rõ nghĩa (player_stats, kills, deaths...).
#    - Nguyên tắc DRY (Don't Repeat Yourself): Tách rời công thức toán học thành hàm độc lập `calculate_kda()` để dễ tái sử dụng và bảo trì.
#    - Exception Handling: Dùng `try...except` chặn đứng ZeroDivisionError và ValueError, kết hợp lệnh `continue` để hệ thống bỏ qua lỗi và tiếp tục tính điểm cho tuyển thủ tiếp theo mà không bị sập.
# (2) Viết code 
# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
data = [
    ("Faker", "10", "2", "8"),      
    ("ShowMaker", "15", "0", "10"), 
    ("Chovy", "12", "ba", "5")     ]

def calculate_kda(kills, deaths, assists):
    """Hàm độc lập chuyên xử lý toán học để tính KDA"""
    return (kills + assists) / deaths

def process_kda_rankings(player_stats_list):
    """Hàm xử lý luồng hiển thị và bẫy lỗi"""
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player_stats in player_stats_list:
        name = player_stats[0]
        kills_str = player_stats[1]
        deaths_str = player_stats[2]
        assists_str = player_stats[3]
        
        try:
            # Bước 1: Ép kiểu dữ liệu (Nơi có thể sinh ra ValueError)
            kills = int(kills_str)
            deaths = int(deaths_str)
            assists = int(assists_str)
            
            # Bước 2: Gọi hàm tính toán (Nơi có thể sinh ra ZeroDivisionError)
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")
            
        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
            continue # Bỏ qua vòng lặp hiện tại, tiếp tục xử lý người tiếp theo
            
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")
            continue 

    print("--- HOÀN TẤT ---")

process_kda_rankings(data)