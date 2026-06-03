# (1) PHÂN TÍCH LỖI 
    # Dựa trên mã nguồn hiện tại (Legacy Code), các câu hỏi phân tích lỗi được trả lời cụ thể như sau:

    # Dictionary employee gồm những key nào?

    # Gồm 4 key: "employee_id", "full_name", "department", và "status".

    # Vì sao dòng employee_id = employee[0] gây lỗi? Dictionary có truy cập phần tử bằng index giống list không?

    # Dòng này gây lỗi KeyError: 0 vì chương trình đang tìm kiếm một key có tên là số 0 trong khi dictionary không có key này.

    # Dictionary không truy cập phần tử bằng chỉ số vị trí (index) giống như list; nó truy cập dữ liệu dựa vào tên các định danh (key).

    # Muốn lấy mã nhân viên "NV001", cần viết lệnh như thế nào?

    # Cần viết: employee_id = employee["employee_id"]

    # Vì sao dòng full_name = employee["name"] gây lỗi? Key đúng để lấy họ tên nhân viên là gì?

    # Dòng này gây lỗi KeyError: 'name' vì trong dictionary không tồn tại key nào tên là "name".

    # Key đúng để lấy họ tên nhân viên là "full_name".

    # Vì sao dòng employee["employee_status"] = "official" chưa cập nhật đúng trạng thái nhân viên? Muốn cập nhật trạng thái nhân viên, cần dùng key nào?

    # Dòng này chưa đúng vì nó đang tạo ra một key hoàn toàn mới tên là "employee_status" thay vì sửa key cũ. Lúc này trạng thái gốc "status": "probation" vẫn bị giữ nguyên.

    # Muốn cập nhật trạng thái nhân viên, cần dùng đúng key gốc là "status".

    # Vì sao dòng employee.append("base_salary", 15000000) gây lỗi? Dictionary có phương thức append() không?

    # Dòng này gây lỗi AttributeError vì đối tượng dictionary trong Python không có phương thức .append(). Phương thức này chỉ dành cho list.

    # Muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh như thế nào?

    # Cần viết: employee["base_salary"] = 15000000

    # Vì sao dòng del employee["team"] gây lỗi? Muốn xóa thông tin phòng ban, cần dùng key nào?

    # Dòng này gây lỗi KeyError: 'team' vì hệ thống không tìm thấy key nào tên là "team" để xóa.

    # Muốn xóa thông tin phòng ban, cần dùng chính xác key "department".
# (2) . Viết Code 
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]

full_name = employee["full_name"]

employee["status"] = "official"

employee["base_salary"] = 15000000

del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)