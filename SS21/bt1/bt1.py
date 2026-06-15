import logging
import os

current_dir = os.path.dirname(__file__)
log_path = os.path.join(current_dir, "momo_transactions.log")

logging.basicConfig(
    filename=log_path,
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class InvalidAmountError(Exception): pass
class InsufficientBalanceError(Exception): pass

class Wallet:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        print("\n--- NẠP TIỀN VÀO VÍ ---")
        while True:
            add_money = input("Nhập số tiền cần nạp : ").strip()
            try:
                int_money = int(add_money)
                if int_money <= 0:
                    print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                    logging.error(f"InvalidAmountError: Attempted to process {int_money} VND.")
                    break
                self.balance += int_money
                print(f"\nNạp tiền thành công: +{int_money:,} VND")
                print(f"Số dư hiện tại: {self.balance:,} VND")
                logging.info(f"Deposit successful: +{int_money} VND. Current Balance: {self.balance}")
                break
            except ValueError as e:
                print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
                logging.error(f"ValueError: Invalid numeric input for deposit. {e}")

    def transfer(self):
        print("\n--- CHUYỂN TIỀN ---")
        phone = input("Nhập số điện thoại người nhận: ").strip()
        if len(phone) != 10 or not phone.isdigit():
            print("Lỗi: Số điện thoại phải đúng định dạng 10 số.")
            return

        try:
            amount = int(input("Nhập số tiền cần chuyển: ").strip())
            if amount <= 0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
                return
            if amount > self.balance:
                print("\nGiao dịch thất bại: Số dư của bạn không đủ.")
                print(f"Số dư hiện tại: {self.balance:,} VND")
                logging.error(f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {self.balance} VND.")
                return
                
            if amount >= 10000000:
                logging.warning(f"High value transaction detected: {amount} VND to {phone}")
                
            self.balance -= amount
            print(f"\nChuyển tiền thành công tới số điện thoại {phone}.")
            print(f"Số tiền đã chuyển: {amount:,} VND")
            print(f"Số dư còn lại: {wallet.balance:,} VND")
            logging.info(f"Transfer successful: -{amount} VND to {phone}. Current Balance: {self.balance}")
        except ValueError:
            print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")

    def check_balance(self):
        print("\n--- SỐ DƯ VÍ MOMO ---")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        logging.info(f"Balance checked. Current Balance: {self.balance}")

wallet = Wallet()

while True:
    print("""========== VÍ MOMO GIẢ LẬP ==========
1. Nạp tiền vào ví
2. Chuyển tiền
3. Xem số dư hiện tại
4. Thoát chương trình 
===============================================""")
    
    choice = input("Nhập lựa chọn của bạn : ").strip()
    
    match choice:
        case "1":
            wallet.deposit()
        case "2":
            wallet.transfer()
        case "3":
            wallet.check_balance()
        case "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ")
            logging.info("System shutdown")
            break
        case _:
            print("Vui lòng nhập 1 - 4 !")