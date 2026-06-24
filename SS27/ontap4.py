class DeliveryOrder:
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery_cost = 0.0
        self.delivery_status = ""
        self.update_order_info()

    def calculate_total_cost(self):
        self.total_delivery_cost = (self.base_fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery_cost < 100000:
            self.delivery_status = "Đơn hàng Tiêu chuẩn (Nội thành)"
        elif self.total_delivery_cost < 300000:
            self.delivery_status = "Đơn hàng Cận tỉnh"
        elif self.total_delivery_cost < 600000:
            self.delivery_status = "Đơn hàng Đường dài (Cần giám sát)"
        else:
            self.delivery_status = "Đơn hàng Đặc biệt (Ưu tiên cao - Rủi ro cao)"

    def update_order_info(self):
        self.calculate_total_cost()
        self.classify_delivery_status()


class OrderManager:
    def __init__(self):
        self.orders = []

    def find_order_by_id(self, order_id):
        for o in self.orders:
            if o.order_id == order_id:
                return o
        return None

    def validate_float(self, prompt):
        while True:
            try:
                val = float(input(prompt).strip())
                if val <= 0:
                    print(">> Lỗi: Giá trị phải lớn hơn 0!")
                    continue
                return val
            except ValueError:
                print(">> Lỗi: Vui lòng nhập đúng định dạng số thực!")

    def validate_int(self, prompt, min_val, max_val):
        while True:
            try:
                val = int(input(prompt).strip())
                if min_val <= val <= max_val:
                    return val
                else:
                    print(f">> Lỗi: Giá trị phải nằm trong đoạn từ {min_val} đến {max_val}!")
                    continue
            except ValueError:
                print(">> Lỗi: Vui lòng nhập đúng định dạng số nguyên!")

    def show_all_orders(self):
        if not self.orders:
            print(">> Lỗi: Hệ thống chưa có vận đơn nào!")
            return
        print(f"{'Mã Đơn':<10}| {'Tên người nhận':<20}| {'Cước nền':<15}| {'Khoảng cách':<15}| {'Phụ phí':<15}| {'Tổng chi phí':<15}| {'Trạng thái đơn':<35}|")
        for item in self.orders:
            print("-" * 130)
            print(f"{item.order_id:<10}| {item.receiver_name:<20}| {item.base_fee:<15.1f}| {item.distance:<15}| {item.surcharge:<15.1f}| {item.total_delivery_cost:<15.1f}| {item.delivery_status:<35}|")

    def add_order(self):
        order_id = input("Nhập mã vận đơn mới: ").strip().upper()
        if not order_id:
            print(">> Lỗi: Mã vận đơn không được để rỗng!")
            return
        if self.find_order_by_id(order_id):
            print(">> Lỗi: Mã vận đơn đã tồn tại!")
            return

        receiver_name = input("Nhập tên người nhận: ").strip().title()
        if not receiver_name:
            print(">> Lỗi: Tên người nhận không được để rỗng!")
            return

        base_fee = self.validate_float("Nhập cước phí nền (>0): ")
        distance = self.validate_int("Nhập khoảng cách giao hàng (1-5000 km): ", 1, 5000)
        surcharge = self.validate_float("Nhập phụ phí (>0): ")

        new_order = DeliveryOrder(order_id, receiver_name, base_fee, distance, surcharge)
        self.orders.append(new_order)
        print(">> Thành công: Đã thêm vận đơn mới thành công.")

    def update_order(self):
        order_id = input("Nhập mã vận đơn cần cập nhật: ").strip().upper()
        order = self.find_order_by_id(order_id)
        if not order:
            print(">> Lỗi: Không tìm thấy vận đơn cần cập nhật!")
            return

        order.base_fee = self.validate_float("Nhập cước phí nền mới: ")
        order.distance = self.validate_int("Nhập khoảng cách mới (1-5000 km): ", 1, 5000)
        order.surcharge = self.validate_float("Nhập phụ phí mới: ")
        order.update_order_info()
        print(">> Thành công: Đã cập nhật thông tin vận đơn!")

    def delete_order(self):
        order_id = input("Nhập mã vận đơn cần xóa: ").strip().upper()
        order = self.find_order_by_id(order_id)
        if not order:
            print(">> Lỗi: Không tìm thấy mã vận đơn cần xóa!")
            return

        choice = input("Bạn có chắc muốn xóa vận đơn này khỏi hệ thống không? (Y/N): ").strip().upper()
        if choice == "Y":
            self.orders.remove(order)
            print(">> Thành công: Đã xóa vận đơn khỏi hệ thống.")
        else:
            print(">> Đã hủy thao tác xóa.")

    def search_by_receiver(self):
        if not self.orders:
            print(">> Lỗi: Hệ thống chưa có vận đơn nào!")
            return

        input_name = input("Nhập tên người nhận cần tìm kiếm: ").strip().upper()
        list_share = []
        for o in self.orders:
            if input_name in o.receiver_name.upper():
                list_share.append(o)

        if not list_share:
            print(">> Không tìm thấy vận đơn phù hợp!")
            return
        else:
            print(f"{'Mã Đơn':<10}| {'Tên người nhận':<20}| {'Cước nền':<15}| {'Khoảng cách':<15}| {'Phụ phí':<15}| {'Tổng chi phí':<15}| {'Trạng thái đơn':<35}|")
            for item in list_share:
                print("-" * 130)
                print(f"{item.order_id:<10}| {item.receiver_name:<20}| {item.base_fee:<15.1f}| {item.distance:<15}| {item.surcharge:<15.1f}| {item.total_delivery_cost:<15.1f}| {item.delivery_status:<35}|")


def main():
    manager = OrderManager()
    while True:
        print("""================ MENU ================
1. Hiển thị danh sách vận đơn trong hệ thống
2. Nhập vận đơn mới
3. Cập nhật thông tin vận đơn
4. Xóa vận đơn khỏi hệ thống
5. Tìm kiếm vận đơn theo tên người nhận
6. Thoát
=====================================
""")
        choice = input("Nhập lựa chọn của bạn: ").strip()
        match choice:
            case "1":
                manager.show_all_orders()
            case "2":
                manager.add_order()
            case "3":
                manager.update_order()
            case "4":
                manager.delete_order()
            case "5":
                manager.search_by_receiver()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")
                return
            case _:
                print(">> Lỗi: Vui lòng nhập lựa chọn từ 1 - 6!")


if __name__ == "__main__":
    main()