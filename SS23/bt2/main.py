# (1)
# 1. Tác hại của from datetime import * và xung đột biến
# Tác hại: Lệnh này sẽ bê toàn bộ các hàm và tên lớp của thư viện datetime vào file hiện tại. Nếu trong mã nguồn của bạn đã có sẵn một biến toàn cục (global) tên là time = 120, câu lệnh import trên sẽ ghi đè hoàn toàn lớp datetime.time lên biến của bạn. Khi bạn gọi đến biến time để tính toán số nguyên sau đó, chương trình sẽ báo lỗi loại dữ liệu và sập ngay lập tức.

# 2. Hàm tối ưu hơn os.mkdir() để tạo thư mục lồng nhau
# Hàm tối ưu nhất là os.makedirs(path, exist_ok=True).

# Lý do: Hàm này cho phép tạo một lúc chuỗi thư mục lồng nhau (ví dụ tạo cả cụm media_vault/2026/video). Khi ta thêm tham số exist_ok=True, nếu thư mục đó đã được tạo từ trước, Python sẽ tự động bỏ qua một cách an toàn chứ không bao giờ văng lỗi FileExistsError.

# 3. Sơ đồ cây thư mục (Folder Tree) của dự án Rikkei Media
# Bạn tiến hành tạo các thư mục con và file nằm đúng vị trí như sơ đồ này:

# Plaintext
# rikkei_media/
# │
# ├── main.py
# ├── storage/
# │   ├── __init__.py
# │   ├── disk_manager.py
# │   └── io_helper.py
# └── analytics/
#     ├── __init__.py
#     └── time_validator.py
# (2)
import os
from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

# Danh sách dữ liệu thô từ phòng hậu kỳ gửi về
raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

def main():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
    
    # Bước 1: Tạo hạ tầng thư mục lưu trữ tổng bằng hàm an toàn
    safe_create_dir("media_vault/audio")
    safe_create_dir("media_vault/video")
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    print("-" * 75)
    
    success_count = 0
    total_files = len(raw_files)
    
    # Bước 2: Duyệt qua từng tệp tin để phân loại
    for file_info in raw_files:
        filename = file_info["filename"]
        size_bytes = file_info["size_bytes"]
        upload_at = file_info["upload_at"]
        
        print(f"[TỆP TIN: {filename}]")
        
        # Kiểm tra tính hợp lệ của ngày tháng qua module analytics
        valid_date = parse_and_inspect_date(upload_at)
        
        if valid_date is None:
            print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at}' không tồn tại)\n")
            continue
            
        # Tính toán dung lượng block qua module storage
        blocks = calculate_disk_blocks(size_bytes)
        
        # Phân loại thư mục dựa trên đuôi mở rộng của tệp tin (.mp3 hay .mp4)
        if filename.endswith(".mp3"):
            category = "audio"
        else:
            category = "video"
            
        print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
        print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")
        print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{category}')\n")
        
        success_count += 1
        
    print("========================================================")
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{total_files} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    main()