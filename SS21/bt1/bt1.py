import logging
logging.basicConfig(
    filename = "loogging.log",
    filemode = "a",
    level= logging.INFO,
    format = " %(asctime)s - %(levelname)s - %(message)s"
)

def  deposit():
    add_monney = input("Nhập số tiền cần nạp : ").strip()
    while True:
        try:
            int_monney = int(add_monney)
            if int_monney <= 0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(f"InvalidAmountError: Attempted to process {int_monney} VND")
                
        except ValueError as e: 
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error(f"ValueError: Invalid numeric input for deposit {e}")
        
while True :
    print("""========== VÍ MOMO GIẢ LẬP ==========
1. Nạp tiền vào ví
2. Chuyển tiền
3.  Xem số dư hiện tại
4. Thoát chương trình 
===============================================
""")
    choice = input("Nhập lựa chọn của bạn : ").strip()
    match (choice):
        case "1":
            deposit()
        case "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ")
            logging.info("System shutdown")
            break
        case _:
            print("Vui lòng nhập 1 - 4 !")
            