import logging
#  khai báo chỗ lưu
logging.basicConfig(
    filename = "data.log",
    filemode = "a", # "w" ghi đè dữ liệu , "a" ghi tiếp nối dữ liệu
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def payment(number_bank : str, money = int):
    if money <= 0:
        print("Số tiền không được phép âm ")
        logging.warning("Thanh toán số tiền âm!")
        return
    try:
        # raise từ khóa khai báo
        # raise ConnectionError("Mất kết nối!")
        raise ValueError("Lỗi kiểu dữ liệu")
        print(f"Tài khoản {number_bank} thanh toán thành công số tiền {money}")
    #  Exception bắt lỗi chung / as đặt tên
    except Exception as e:
        print(f"Lỗi hệ thống {e}")
        return
    # chạy khi khối try không có lỗi
    else: 
        print("Đã thành công")
        logging.info("Tài khoản thanh toán thành công")
    # chạy bất kể đúng hay sai
    finally:  
        print("Giao dịch hoàn tất")
payment("199199",-11111)

# for i in range(2, 10):
#     print(f"====BẢNG CỬU CHƯƠNG {i}====")
#     for j in range(1,11):
#         result = i * j
#         print(f"{i} x {j} = {result}")
# cách tìm lỗi nhấn bên trái số dấu chấm , nhấn nút tam giác có con bọ , nhấn run and debug nhấn
# logging dùng để lưu trữ dữ liệu khi lỗi
