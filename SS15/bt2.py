# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 1. Phân định cơ chế truyền dữ liệu (Arguments vs Global Variables)
# Khi nào thao tác trực tiếp với Global Variables: * Hàm display_balances() chỉ đọc giá trị từ bộ nhớ tổng để hiển thị.

# Các hàm ghi nhận thay đổi trực tiếp vào tài sản chung của hệ thống như deposit_money() (nạp tiền) và execute_withdrawal() (thực thi trừ tiền) bắt buộc phải dùng từ khóa global để chỉnh sửa trực tiếp hai biến toàn cục user_account_balance và atm_vault_balance.

# Khi nào cần truyền dữ liệu qua Arguments (Tham số):

# Hàm check_withdrawal_rules(amount) cần tính độc lập để kiểm tra một số tiền bất kỳ (amount) do người dùng nhập vào xem có hợp lệ hay không trước khi quyết định xử lý.

# Hàm execute_withdrawal(total_deduction, amount_to_dispense) nhận dữ liệu số tiền cần trừ và số tiền thực tế nhả ra từ cây ATM để đảm bảo tính chính xác và an toàn thông tin, không bị lẫn lộn giữa tiền gốc và chi phí phát sinh.
# (2)  Viết code 

atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balances():
    """
    In ra màn hình số dư tài khoản của khách hàng và số tiền mặt trong cây ATM.
    
    Tham số đầu vào: Không có.
    Giá trị trả về: Không có (None).
    """
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")

def deposit_money(amount):
    """
    Xử lý nạp tiền mặt vào tài khoản cá nhân và cập nhật hòm tiền ATM.
    
    Tham số đầu vào:
        amount (int): Số tiền khách hàng muốn nạp vào máy.
    Giá trị trả về:
        bool: Trả về True đại diện cho giao dịch thành công.
    """
    global user_account_balance, atm_vault_balance
    user_account_balance = user_account_balance + amount
    atm_vault_balance = atm_vault_balance + amount
    return True

def check_withdrawal_rules(amount):
    """
    Kiểm tra các quy định, điều kiện an toàn và ranh giới hạn mức khi rút tiền.
    
    Tham số đầu vào:
        amount (int): Số tiền khách hàng yêu cầu rút.
    Giá trị trả về:
        str: Trả về "INSUFFICIENT_FUNDS", "ATM_OUT_OF_CASH" hoặc "OK".
    """
    fee = 1100
    total_deduction = amount + fee
    
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    elif amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    else:
        return "OK"

def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện trừ tiền trong tài khoản người dùng và đẩy tiền mặt ra khỏi máy ATM.
    
    Tham số đầu vào:
        total_deduction (int): Tổng số tiền bị trừ trong thẻ bao gồm cả phí.
        amount_to_dispense (int): Số tiền mặt vật lý máy ATM nhả ra cho khách.
    Giá trị trả về:
        Không có (None).
    """
    global user_account_balance, atm_vault_balance
    user_account_balance = user_account_balance - total_deduction
    atm_vault_balance = atm_vault_balance - amount_to_dispense

def main():
    while True:
        print("""
============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================""")
        
        choice = input("Vui lòng chọn giao dịch (1-4): ").strip()
        
        match choice:
            case "1":
                display_balances()
                
            case "2":
                print("\n--- NẠP TIỀN ---")
                amount_str = input("Nhập số tiền muốn nạp: ").strip()
                
                # Bẫy lỗi nhập chữ bằng cách dùng phương thức .isdigit()
                if not amount_str.isdigit():
                    print("Số tiền không hợp lệ.")
                    continue
                    
                amount = int(amount_str)
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                    continue
                    
                deposit_money(amount)
                print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
                
            case "3":
                print("\n--- RÚT TIỀN ---")
                amount_str = input("Nhập số tiền cần rút: ").strip()
                
                if not amount_str.isdigit():
                    print("Số tiền không hợp lệ.")
                    continue
                    
                amount = int(amount_str)
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                    continue
                    
                # Bẫy lỗi tiền rút bắt buộc phải là bội số của 50,000đ
                if amount % 50000 != 0:
                    print("Số tiền rút phải là bội số của 50,000")
                    continue
                    
                
                status = check_withdrawal_rules(amount)
                
                if status == "INSUFFICIENT_FUNDS":
                    print("Giao dịch thất bại: Số dư tài khoản của bạn không đủ điều kiện thanh toán.")
                elif status == "ATM_OUT_OF_CASH":
                    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                elif status == "OK":
                    fee = 1100
                    total_deduction = amount + fee
                    
                    print("Giao dịch đang xử lý...")
                    execute_withdrawal(total_deduction, amount)
                    
                    print(f"Phí giao dịch: {fee:,} VND")
                    print(f"Bạn đã rút thành công {amount:,} VND.")
                    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")
                    
            case "4":
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break
                
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4.")
                
        input("\nNhấn Enter để tiếp tục giao dịch tiếp theo...")

main()