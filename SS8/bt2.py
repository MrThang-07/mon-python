# (I) Phân tích 
    # 1. Phân tích Input/Output
    # Input
    # Tên shop (String)
    # Tên sản phẩm (String)
    # Mô tả sản phẩm (String)
    # Danh mục sản phẩm (String)
    # Danh sách từ khóa (String)
    # Mã giảm giá (String)
    # Từ khóa cần tìm và thay thế (String)
    # Lựa chọn menu (Integer)
    # Output
    # Thông tin sản phẩm sau khi chuẩn hóa.
    # Độ dài mô tả sản phẩm.
    # Số lượng từ khóa.
    # Kết quả chuẩn hóa tên shop.
    # Thông báo mã giảm giá hợp lệ/không hợp lệ.
    # Mô tả sau khi tìm kiếm và thay thế từ khóa.
    # Thông báo lỗi khi dữ liệu không hợp lệ.
    # Thông báo thoát chương trình.
    # 2. Đề xuất giải pháp
    # Sử dụng vòng lặp while để hiển thị menu.
    # Dùng if...elif...else xử lý các chức năng.
    # Sử dụng các hàm xử lý chuỗi như:
    # strip()
    # lower()
    # upper()
    # title()
    # split()
    # join()
    # replace()
    # count()
    # Kiểm tra dữ liệu nhập để xử lý các trường hợp lỗi.
# (II)   Viết code :
current_description = ""

while True:

    print("\n===== MENU =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ!")
        continue

    if choice == 1:

        shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        product_name = input("Nhập tên sản phẩm: ")

        description = input("Nhập mô tả sản phẩm: ")

        if description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        category = input("Nhập danh mục sản phẩm: ")

        keywords = input("Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): ")

        shop_name = shop_name.strip()
        product_name = product_name.strip().title()
        description = description.strip()
        category = category.strip().lower()

        current_description = description

        keyword_count = 1

        if keywords.strip() == "":
            keyword_count = 0
        else:
            for char in keywords:
                if char == ",":
                    keyword_count += 1

        print("\n===== BÁO CÁO THỐNG KÊ =====")
        print("Tên shop:", shop_name)
        print("Tên sản phẩm:", product_name)
        print("Mô tả:", description)
        print("Độ dài mô tả:", len(description))
        print("Danh mục:", category)
        print("Danh sách từ khóa:", keywords)
        print("Số lượng từ khóa:", keyword_count)
        print("Mô tả chữ thường:", description.lower())
        print("Mô tả chữ hoa:", description.upper())

    elif choice == 2:

        shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        print("Tên shop ban đầu:", shop_name)

        shop_name = shop_name.strip()
        shop_name = shop_name.lower()
        shop_name = shop_name.replace(" ", "-")

        if shop_name.find("shop-") != 0:
            shop_name = "shop-" + shop_name

        print("Tên shop sau chuẩn hóa:", shop_name)

    elif choice == 3:

        code = input("Nhập mã giảm giá: ")

        if code == "":
            print("Mã giảm giá không được rỗng")

        elif " " in code:
            print("Mã giảm giá không được chứa khoảng trắng")

        elif len(code) < 6 or len(code) > 12:
            print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")

        elif code != code.upper():
            print("Mã giảm giá phải được viết hoa toàn bộ")

        elif not code.isalnum():
            print("Mã giảm giá chỉ được chứa chữ cái và chữ số")

        elif code.find("SALE") != 0:
            print("Mã giảm giá phải bắt đầu bằng SALE")

        else:
            print("Mã giảm giá hợp lệ")

    elif choice == 4:

        if current_description == "":
            print("Chưa có mô tả sản phẩm!")
            continue

        find_word = input("Nhập từ khóa cần tìm: ")
        replace_word = input("Nhập từ khóa thay thế: ")

        count = current_description.count(find_word)

        if count == 0:
            print("Không tìm thấy từ khóa")

        else:
            new_description = current_description.replace(find_word, replace_word)

            print("Số lần xuất hiện của từ khóa:", count)
            print("Mô tả sau khi thay thế:")
            print(new_description)

    elif choice == 5:
        print("Thoát chương trình")
        break