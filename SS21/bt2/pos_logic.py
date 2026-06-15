import logging

# 1. Thực đơn đồ uống mặc định
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

# 2. Định nghĩa các lỗi tùy chỉnh (Custom Exceptions) theo đề bài
class ItemNotFoundError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

# 3. Hàm hiển thị thực đơn
def view_menu():
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in DRINK_MENU.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")

# 4. Hàm xử lý thêm món vào giỏ hàng
def add_to_order(current_order, drink_code, quantity):
    """
    Kiểm tra mã nước và số lượng. Nếu sai ném ra lỗi, nếu đúng thì thêm vào giỏ.
    """
    if drink_code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {drink_code}")
        raise ItemNotFoundError()
        
    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise InvalidQuantityError()
        
    logging.info(f"Added {quantity} of {drink_code} to order")
    
    # Nếu món đã có trong giỏ, chỉ cần cộng dồn số lượng lên
    for order_item in current_order:
        if order_item["drink_code"] == drink_code:
            order_item["quantity"] += quantity
            return DRINK_MENU[drink_code]["name"]
            
    # Nếu là món mới, thêm một dictionary mới vào giỏ hàng
    item_details = DRINK_MENU[drink_code]
    current_order.append({
        "drink_code": drink_code,
        "name": item_details["name"],
        "price": item_details["price"],
        "quantity": quantity
    })
    return DRINK_MENU[drink_code]["name"]

# 5. Hàm tính tổng tiền giỏ hàng
def calculate_total(current_order):
    total = 0
    for item in current_order:
        total += item["price"] * item["quantity"]
    return total