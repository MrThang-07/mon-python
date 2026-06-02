# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. Phân tích Input / Output
# Dữ liệu hệ thống (Input): Mảng một chiều playlist = [] dạng danh sách (list) lưu trữ chuỗi tên bài hát (str).

# Dữ liệu người dùng nhập (Input từ bàn phím):

# choice, sub_choice: Lựa chọn tính năng tại menu chính và menu phụ (Kiểu str).

# ten_bai_hat, ten_xoa: Tên bài hát để thêm hoặc tìm kiếm xóa (Kiểu str).

# vi_tri_str: Vị trí nhập dưới dạng chuỗi số, cần kiểm tra tính hợp lệ trước khi chuyển đổi sang số nguyên (int).

# Kết quả hiển thị (Output màn hình): Các thông báo trạng thái thành công/thất bại và giao diện danh sách bài hát đánh số thứ tự từ 1 tăng dần.

#  2. Đề xuất giải pháp thực hiện
# Điều hướng luồng chạy: Kết hợp vòng lặp vô hạn while True: và hai tầng cấu trúc rẽ nhánh match-case lồng nhau để xử lý menu chính và menu phụ một cách trực quan, mạch lạc.

# Xử lý chuỗi (String): Sử dụng phương thức .strip() để làm sạch dữ liệu nhập đầu vào và .isdigit() tại các bước chèn/xóa để ngăn chặn triệt để lỗi crash chương trình khi người dùng vô tình nhập chữ vào ô số.

# Xử lý danh sách (List methods):

# .append(): Dùng cho trường hợp thêm vào cuối danh sách phát.

# .insert(index, item): Dùng để chèn bài hát vào vị trí mong muốn với công thức index = vi_tri - 1.

# .remove(): Tìm kiếm và xóa trực tiếp theo tên bài hát (phân biệt hoa thường).

# .pop(index): Loại bỏ và trả về tên bài hát bị xóa theo số thứ tự vị trí tương ứng.

# .sort(): Sắp xếp động toàn bộ các chuỗi trong danh sách theo thứ tự bảng chữ cái từ A đến Z.
# (2) Viết code



playlist = []

while True: 
    print("\n========== MENU QUẢN LÝ DANH SÁCH PHÁT ==========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp danh sách phát (A-Z)")
    print("5. Thoát chương trình")
    print("==================================================")
    
    choice = input("Nhập lựa chọn của bạn: ").strip()
    match choice:
        case "1":
            print("\n--- Thêm Bài Hát---")
            print("1. Thêm vào cuối danh sách")
            print("2. Chèn vào vị trí cụ thể ")
            sub_choice = input("Nhập lựa chọn : ").strip()

            match sub_choice:
                case "1":
                    ten_bai_hat = input("Nhập tên bài hát: ").strip()
                    if ten_bai_hat == "":
                        print("Lỗi: Tên bài hát không được để trống!")
                    else:
                        playlist.append(ten_bai_hat)
                        print(f"Thanh công: Đã thêm bài hát '{ten_bai_hat}' vào cuối danh sách.")
                        print(f"Số lượng bài hát hiện tại : {len(playlist)}")
                case "2" :
                    if len(playlist) == 0:
                        ten_bai_hat = input("Danh sách đang trống. Nhập tên bài hát để thêm vào đầu: ").strip()
                        if ten_bai_hat != "":
                            playlist.append(ten_bai_hat)
                            print(f"Thành công: Đã thêm bài hát '{ten_bai_hat}' vào vị trí đầu tiên.")
                        else:
                            print("Lỗi: Tên bài hát không được để trống!")
                    else:
                        vi_tri_str = input(f"Nhập số thứ tự muốn chèn (từ 1 đến {len(playlist) + 1}): ").strip()
                        if not vi_tri_str.isdigit():
                            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
                        else:
                            vi_tri =int(vi_tri_str)
                            if vi_tri < 1 or vi_tri > len(playlist) + 1:
                                print("Vị trí không hợp lệ.")
                            else:
                                ten_bai_hat = input("Nhập tên bài hát: ").strip()
                                if ten_bai_hat == "":
                                    print("Lỗi: Tên bài hát không được để trống!")
                                else:
                                    playlist.insert(vi_tri - 1, ten_bai_hat)
                                    print(f"Thành công: Đã chèn bài hát '{ten_bai_hat}' vào vị trí thứ {vi_tri}.")
                                    print(f"Số lượng bài hát hiện tại: {len(playlist)}")
                case _:
                    print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
        case "2":
            print("\n--- Danh Sách Phát ---")
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống")
            else:
                stt = 1
                for b_hat in playlist:
                    print(f"{stt}. {b_hat}")
                    stt += 1
                print(f"\nToorng số bài hát: {len(playlist)}")
        case "3":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n--- XÓA BÀI HÁT ---")
                print("1. Xóa theo tên bài hát")
                print("2. Xóa theo số thứ tự")
                sub_choice = input("Nhập lựa chọn: ").strip()

                match sub_choice:
                    case "1":
                        ten_xoa = input("Nhập chính xác tên bài hát muốn xóa: ").strip()     
                        if ten_xoa in playlist:
                            playlist.remove(ten_xoa)
                            print(f"Đã xóa bài hát [{ten_xoa}] khỏi danh sách.")
                        else:
                            print("Không tìm thấy bài hát danh sách phát.")
                    case "2":
                        vi_tri_str = input(f"Nhập số thứ tự bài hát muốn xóa (1 đến {len(playlist)}): ").strip()
                        if not vi_tri_str.isdigit():
                            print("Lựa chọn không hợp lệ , vui lòng nhập số nguyên")
                        else:
                            vi_tri = int(vi_tri_str)
                            if vi_tri < 1 or vi_tri > len(playlist):
                                print("Vị trí không hợp lệ")
                            else:
                                ten_da_xoa = playlist.pop(vi_tri - 1)
                                print(f"Đã xóa bài hát [{ten_da_xoa}] khỏi danh sách.")
                    case _:
                        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên ")
        case "4":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống !")
            else:
                playlist.sort()
                print("\nĐã sắp xếp lại danh sách phát theo thứ tự bảng chữ cái (A-Z) thành công!")
        case "5":
            print("\nCảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break  
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")     
        