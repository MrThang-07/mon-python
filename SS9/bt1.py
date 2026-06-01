# (I) Phân tích
    # Câu 1:
    # Sau insert(0, "GE000"), danh sách sẽ là:
    # ['GE000', 'GE001', 'GE002', 'GE003-CANCEL', 'GE004']

    # Câu 2:
    # delivery_orders[1] = "GE002-UPDATED" sai vì sau khi chèn GE000,
    # GE002 nằm ở index 2 chứ không phải index 1.

    # Câu 3:
    # Sau khi chèn GE000 vào đầu danh sách, GE002 nằm ở index 2.

    # Câu 4:
    # delivery_orders.remove(3) bị lỗi vì remove() xóa theo giá trị,
    # trong danh sách không có phần tử nào có giá trị là 3.

    # Câu 5:
    # remove() xóa phần tử theo giá trị (value), không phải vị trí (index).

    # Câu 6:
    # Muốn xóa GE003-CANCEL:
    # delivery_orders.remove("GE003-CANCEL")

    # Câu 7:
    # pop() xóa phần tử khỏi danh sách và trả về phần tử vừa bị xóa.

    # Câu 8:
    # Chương trình lỗi khi in transferred_order vì biến này chưa được tạo.

    # Câu 9:
    # Muốn lưu đơn hàng vừa lấy ra:
    # transferred_order = delivery_orders.pop()
# (II) Viết code
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

delivery_orders.append("GE004")

delivery_orders.insert(0, "GE000")

delivery_orders[2] = "GE002-UPDATED"

delivery_orders.remove("GE003-CANCEL")

transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)