# (I) phân tích 
        # Câu 1:
    # Sau insert(0, "GE100-FAST"), danh sách sẽ là:
    # ['GE100-FAST', 'GE101', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']

    # Câu 2:
    # express_orders[1] = "GE102-UPDATED" sửa nhầm GE101 vì sau khi chèn
    # GE100-FAST vào đầu, GE101 nằm ở index 1.

    # Câu 3:
    # GE102-WRONG nằm ở index 2.

    # Câu 4:
    # express_orders.pop(3) xóa phần tử ở vị trí 3.
    # Cách làm này phụ thuộc vào vị trí phần tử nên dễ sai.

    # Câu 5:
    # Muốn xóa GE103-CANCEL nên dùng:
    # express_orders.remove("GE103-CANCEL")

    # Câu 6:
    # pop() không truyền index sẽ lấy phần tử cuối danh sách.

    # Câu 7:
    # current_order = express_orders.pop()
    # lấy GE104 thay vì GE100-FAST.

    # Câu 8:
    # Muốn lấy đơn hàng đầu tiên:
    # current_order = express_orders.pop(0)

    # Câu 9:
    # Cần sửa index cập nhật GE102-WRONG,
    # dùng remove() để xóa GE103-CANCEL
    # và dùng pop(0) để lấy đơn hàng đầu tiên.
# (II) viết code :
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

express_orders.append("GE104")

express_orders.insert(0, "GE100-FAST")

express_orders[2] = "GE102-UPDATED"

express_orders.remove("GE103-CANCEL")

current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)