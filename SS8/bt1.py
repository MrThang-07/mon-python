while True:
    print("--- HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK ---")
    print("1.Nhập và phân tích thông tin video ")
    print("2.Chuẩn hóa tên tài khoản")
    print("3.Kiểm tra hashtag không hợp lệ")
    print("4.Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")

    choice = (input("Mời bạn chọn chức năng 1- 5 : "))
    match (choice) :
        case "1":
            user_name = input("Nhập tên tài khoản : ")
            title = input("Nhập tieeu đề video : ")
            descripstion = input("Nhập mô tả video : ")
            list_hashtag = input("Nhập sanh sách hashtag (Ccahs nhau dấu phẩy ) : ")
            print("=========================")
            print(f"Tên tài khoản : {user_name.strip()}")
            print(f"Tên tiêu đề : {title.title().strip()}")
            print(f"Mô tả : {descripstion.strip()}")
            print(f"Độ dài mô tả : {len(descripstion)}" )
            cout_space = descripstion.count(" ") + 1
            print(f"Số lượng từ trong mô tổ : {cout_space}")
            list_temp = list_hashtag.split(",")
            new_list_hashtag = "".join(list_temp)
            print(f"Danh sách hashtag: {new_list_hashtag}")
            cout_hashtag = len(list_temp)
            print(f"Số lượng hashtag là : {cout_hashtag}")
            print(f"Mô tả video được chuyển toàn bộ sang chữ thường : {descripstion.lower()} ")
            print(f"Mô tả video được chuyển toàn bộ sang chữ hoa : {descripstion.upper()}")

        case "2":
            print(f"Tên tài khoản trước khi chuẩn hóa {user_name}")
            print(f"Tên tài khoản sau khi chuẩn hóa : {("@" + user_name).lower()}")
        case "3":
            hashtag = input("Nhập hashtag: ")
            if (hashtag == ""):
                print("Không được rỗng !")
               
            elif not hashtag.startswith("#"):
                print("Phải bắt đầu #")
             
            elif (" " in hashtag) :
                print("Không chứa khoảng trắng ")
            elif (len(hashtag) < 2):
                print("Phải chứa tối thiểu 2 kí tự ")
            else :
                print("Hashtag hợp lệ")
                list_hashtag = list_hashtag + hashtag
                print(f"Danh sách hashtag mới {list_hashtag}")

        case "4":
            find_word = input("Nhập từ khóa cần tìm : ")
            cout_word = descripstion.count(find_word)
            if cout_word > 0 :
            
                descripstion = descripstion.replace(find_word,"Từ khóa mới")
                print(f"MÔ tả thay thế : {descripstion}")
                print(f"Số lần xuất hiện {cout_word}")
            else:
                print("Từ khóa khôg tìm thấy !")
        case "5":
            print("Đã thoát chương trình !")
            break
        case _:
            print("Lựa chọn không hợp lệ ")