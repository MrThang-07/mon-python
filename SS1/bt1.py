# 1. Phân Tích Lỗi (Bug Analysis)
#   Dò luồng thực thi (Trace code):
#       Hệ thống khởi tạo và gán giá trị từ bàn phím vào 3 biến rất chính xác:
#            name_patient nhận giá trị: "Nguyễn Văn A"
#            age nhận giá trị: 25
#            symptom nhận giá trị: "Đau đầu"
#   Tuy nhiên, ở phần in kết quả (--- PHIẾU KHÁM BỆNH ---), các biến bị truyền sai vị trí:
#       print('Tên bệnh nhân:', symptom) -> In ra nhãn "Tên bệnh nhân" nhưng lại truyền biến triệu chứng (symptom).
#       print('Tuổi:', name_patient) -> In ra nhãn "Tuổi" nhưng lại truyền biến tên (name_patient).
#       print('Triệu chứng:', age) -> In ra nhãn "Triệu chứng" nhưng lại truyền biến tuổi (age).
#   Nguyên nhân gây lỗi logic: Người viết mã nguồn cũ đã nhầm lẫn khi truyền tham số vào hàm print(). 
#   Các nhãn hiển thị (String literal) không khớp với biến (Variable) chứa giá trị tương ứng.
#   Vì Python chỉ kiểm tra cú pháp chứ không thể hiểu được "ngữ nghĩa" của chữ bạn viết, 
#   nên chương trình vẫn chạy bình thường và xuất ra kết quả sai lệch.Ngoài ra, 
#   trong Python chúng ta không cần dùng dấu phẩy ; ở cuối câu lệnh.
#2. Mã Nguồn Sửa Lỗi (Fixed Code cho VS Code)
print('---HỆ THỐNG TIẾO NHẬN BỆNH NHÂN---')
name_patient = input('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bênh: ')

print(' -- PHIẾU KHÁM BỆNH --')
print('Tên bệnh nhân: ', name_patient)
print('Tuổi: ', age)
print('Triệu chứng: ', symptom)