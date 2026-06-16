


import datetime
from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta

shipments = [
    {
        "id": "TRK-001", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 10.8231, "to_lon": 106.6297, 
        "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 16.0544, "to_lon": 108.2022, 
        "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"
    },
]

def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    
    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)
    
    for s in shipments:
        distance = calculate_distance(
            s["from_lat"], s["from_lon"], 
            s["to_lat"], s["to_lon"]
        )
        
        eta = predict_eta(s["depart"], distance, speed=60)
        deadline_time = datetime.datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        
        if eta <= deadline_time:
            status = "🟢 AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            time_str = deadline_time.strftime("%H:%M:%S")
            status = f"🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {time_str})"
            
        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" + Trạng thái: {status}\n")
        
    print("========================================================")

if __name__ == "__main__":
    main()