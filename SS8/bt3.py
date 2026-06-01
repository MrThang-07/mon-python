# (I) Phân tích :

    # 1. Phân tích Input/Output
    # Input
    # Tên người gửi (String)
    # SĐT người gửi (String)
    # Địa chỉ lấy hàng (String)
    # Tên người nhận (String)
    # SĐT người nhận (String)
    # Địa chỉ giao hàng (String)
    # Ghi chú giao hàng (String)
    # Mã đơn hàng (String)
    # Từ khóa tìm kiếm (String)
    # Từ khóa thay thế (String)
    # Output
    # Thông tin đơn hàng đã chuẩn hóa.
    # Mã đơn hàng sau chuẩn hóa.
    # SĐT đã được ẩn.
    # Kết quả tìm kiếm và thay thế từ khóa.
    # Thông báo lỗi nếu dữ liệu không hợp lệ.
# (II) Viết code 
while True:

    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Nhập dữ liệu đơn hàng")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    if int(choice) < 1 or int(choice) > 5:
        print("Lựa chọn không hợp lệ")
        continue

    match choice:

        case "1":

            sender_name = input("Nhập tên người gửi: ")
            sender_phone = input("Nhập SĐT người gửi: ")
            pickup_address = input("Nhập địa chỉ lấy hàng: ")

            receiver_name = input("Nhập tên người nhận: ")
            receiver_phone = input("Nhập SĐT người nhận: ")
            delivery_address = input("Nhập địa chỉ giao hàng: ")

            note = input("Nhập ghi chú giao hàng: ")

            if sender_name.strip() == "":
                print("Tên người gửi không được bỏ trống")
                continue

            if receiver_name.strip() == "":
                print("Tên người nhận không được bỏ trống")
                continue

            if note.strip() == "":
                print("Ghi chú giao hàng không được bỏ trống")
                continue

            print("\n===== THỐNG KÊ =====")

            print("Tên người gửi:",
                  sender_name.strip().title())

            print("Tên người nhận:",
                  receiver_name.strip().title())

            print("Địa chỉ lấy hàng:",
                  pickup_address.strip())

            print("Địa chỉ giao hàng:",
                  delivery_address.strip())

            print("Ghi chú:",
                  note.strip())

            print("Độ dài ghi chú:",
                  len(note))

            count_word = note.count(" ") + 1

            print("Số lượng từ:",
                  count_word)

            print("Ghi chú chữ thường:")
            print(note.lower())

            print("Ghi chú chữ hoa:")
            print(note.upper())

        case "2":

            order_code = input("Nhập mã đơn hàng: ")

            print("Mã đơn hàng ban đầu:",
                  order_code)

            order_code = order_code.strip()

            order_code = order_code.upper()

            order_code = order_code.replace(" ", "-")

            if not order_code.startswith("GRAB-"):
                order_code = "GRAB-" + order_code

            print("Mã đơn hàng sau chuẩn hóa:")
            print(order_code)

        case "3":

            if not sender_phone.isdigit() or len(sender_phone) != 10:
                print("Số điện thoại người gửi không hợp lệ")
            else:

                hide_sender = (
                    sender_phone[:3]
                    + "*****"
                    + sender_phone[-2:]
                )

                print("SĐT người gửi:",
                      hide_sender)

            if not receiver_phone.isdigit() or len(receiver_phone) != 10:
                print("Số điện thoại người nhận không hợp lệ")
            else:

                hide_receiver = (
                    receiver_phone[:3]
                    + "*****"
                    + receiver_phone[-2:]
                )

                print("SĐT người nhận:",
                      hide_receiver)

        case "4":

            if "note" not in locals():
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue

            find_word = input("Nhập từ khóa cần tìm: ")

            replace_word = input("Nhập từ khóa thay thế: ")

            count = note.count(find_word)

            if count == 0:
                print("Không tìm thấy từ khóa")
            else:

                note = note.replace(
                    find_word,
                    replace_word
                )

                print("Số lần xuất hiện:",
                      count)

                print("Ghi chú sau thay thế:")
                print(note)

        case "5":

            print("Thoát chương trình")
            break