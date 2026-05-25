# (1) Phân tích lỗi (Bug Analysis)
#     1. Dò luồng thực thi (Trace code) với heart_rate = 135
#         Khi nhập giá trị heart_rate = 135, Python sẽ kiểm tra các điều kiện từ trên xuống dưới:
#             Điều kiện 1 (if heart_rate > 100): Máy tính kiểm tra $135 > 100$. Điều kiện này ĐÚNG (True).

#             Hệ thống ngay lập tức nhảy vào thực hiện lệnh bên trong: print("Priority: YELLOW...").

#             Sau khi một nhánh trong cấu trúc if-elif-else đã thỏa mãn,
#             Python sẽ thoát hoàn toàn khỏi cấu trúc rẽ nhánh đó và bỏ qua toàn bộ các nhánh elif hoặc else phía dưới.
#     2. Khái niệm "Luồng thực thi từ trên xuống dưới" của if-elif-else
#         Trong Python, cấu trúc if-elif-else hoạt động theo nguyên tắc loại trừ tuần tự:

#             Máy tính kiểm tra các nhánh theo thứ tự từ trên xuống dưới.

#             Nhánh nào thỏa mãn đầu tiên sẽ được chọn để chạy.

#             Khi đã có một nhánh chạy, các nhánh còn lại (cho dù có đúng về mặt toán học) cũng sẽ bị ngó lơ hoàn toàn.
#     3. Nguyên nhân khối lệnh RED bị bỏ qua
#         Do lập trình viên đặt điều kiện rộng hơn (> 100) lên phía trên điều kiện hẹp hơn (> 120).
#         Vì mọi số lớn hơn 120 thì chắc chắn đều lớn hơn 100, nên tất cả các ca nguy kịch (nhịp tim 130, 140, 150...)
#         đều bị nhánh if heart_rate > 100 "đón chặn" trước và phân loại sai thành màu VÀNG (YELLOW). Khối lệnh RED ở dưới không bao giờ có cơ hội được chạm tới.
# (2) Sửa lỗi
print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:  
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100: 
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")