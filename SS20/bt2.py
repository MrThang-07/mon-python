# (1) Phân tích 
# 1. Vấn đề của mã nguồn cũ (Legacy Code):
#    - Crash do thiếu dữ liệu (IndexError): Xảy ra khi cố truy cập phần tử không tồn tại trong Tuple (hồ sơ bị khuyết trường MMR).
#    - Crash do dữ liệu bẩn (ValueError): Xảy ra khi dùng hàm int() ép kiểu một chuỗi chữ cái ("N/A") sang số nguyên.
#    - Vi phạm Clean Code: Dùng các biến viết tắt tối nghĩa (ds, p, t, m, r...); nhồi nhét cả việc tính toán và hiển thị vào một hàm duy nhất.

# 2. Giải pháp Refactor áp dụng:
#    - Self-documenting code: Đổi tên biến sang tiếng Anh chuẩn, tự giải thích ý nghĩa (player_records, matches, mmr...).
#    - Nguyên tắc Modular (Tách hàm): Rút trích công thức tính điểm thưởng sang hàm độc lập `calculate_bonus()` để tái sử dụng.
#    - Exception Handling: Sử dụng cấu trúc `try...except` để bẫy IndexError và ValueError. Dùng lệnh `continue` để hệ thống tự động bỏ qua hồ sơ lỗi và tính tiếp cho người sau mà không bị sập
# (2) Viết code 

data = [
    ("Levi", 120, 2500),    
    ("SofM", 150),           
    ("Optimus", 100, "N/A")  
]

def calculate_bonus(matches, mmr):
    """Hàm độc lập tính toán điểm thưởng RP"""
    return (matches * 10) + (int(mmr) * 0.5)

def process_end_season_bonus(player_records):
    """Hàm duyệt danh sách và bẫy lỗi dữ liệu"""
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for record in player_records:
       
        name = record[0] 
        
        try:
            # Có nguy cơ xảy ra IndexError nếu record không có phần tử thứ 2 hoặc 3
            matches = record[1]
            mmr = record[2]
            
            # Có nguy cơ xảy ra ValueError nếu mmr là chữ
            bonus = calculate_bonus(matches, mmr)
            
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue  # Bỏ qua và chạy tiếp người sau
            
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue  

    print("--- HOÀN TẤT ---")

# Chạy hệ thống
process_end_season_bonus(data)