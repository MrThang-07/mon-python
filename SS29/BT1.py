import logging
from abc import ABC, abstractmethod

# Cấu hình logging thay vì in thô cho các luồng vết hệ thống
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("RikkeiSmartFactory")

# ==========================================
# 1. THIẾT KẾ KIẾN TRÚC LỚP (OOP BLUEPRINT)
# ==========================================

class BaseDevice(ABC):
    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1000000

    def __init__(self, device_code, device_name, **kwargs):
        if not self.validate_device_code(device_code):
            raise ValueError("ERR-IOT-01")
        self.device_code = device_code
        self.device_name = device_name  # Gọi qua setter để chuẩn hóa
        self.__operating_hours = 0
        super().__init__(**kwargs)

    @property
    def device_name(self):
        return self.__device_name

    @device_name.setter
    def device_name(self, value):
        # Chuẩn hóa: Xóa khoảng trắng thừa và in hoa
        self.__device_name = " ".join(value.split()).upper()

    @property
    def operating_hours(self):
        return self.__operating_hours

    def add_operating_hours(self, hours):
        if not isinstance(hours, (int, float)) or hours <= 0:
            raise ValueError("ERR-IOT-03")
        self.__operating_hours += hours

    @abstractmethod
    def track_performance(self):
        pass

    @abstractmethod
    def run_diagnostic(self):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseDevice):
            raise TypeError("ERR-IOT-04")
        return self.operating_hours + other.operating_hours

    def __lt__(self, other):
        if not isinstance(other, BaseDevice):
            raise TypeError("ERR-IOT-04")
        return self.operating_hours < other.operating_hours

    @staticmethod
    def validate_device_code(device_code):
        return len(device_code) == 10 and device_code[0].isalpha()

    @classmethod
    def update_maintenance_cost(cls, new_cost):
        cls.base_maintenance_cost = new_cost


class ProductionRobot(BaseDevice):
    def __init__(self, **kwargs):
        self.completed_products = 0
        super().__init__(**kwargs)

    def track_performance(self):
        # Tính toán hiệu suất giả định (OEE)
        if self.operating_hours > 0:
            oee = (self.completed_products / (self.operating_hours * 100)) * 100
        else:
            oee = 0.0
        return f"Chỉ số hiệu suất thiết bị tổng thể (OEE): {round(oee, 1)}%"

    def run_diagnostic(self):
        if self.completed_products > 10000:
            return f"Cảnh báo: Sản lượng đạt {self.completed_products}, cần bảo dưỡng định kỳ!"
        return "Trạng thái: Hoạt động ổn định."


class ThermalSensor(BaseDevice):
    def __init__(self, **kwargs):
        self.current_temperature = 0.0
        self.safety_threshold = 80.0
        super().__init__(**kwargs)

    def track_performance(self):
        margin = self.safety_threshold - self.current_temperature
        return f"Nhiệt độ hiện hành: {self.current_temperature} độ C. Biên độ an toàn: {margin} độ C."

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return f"Nguy hiểm: Vượt ngưỡng nhiệt! (Nhiệt độ hiện tại: {self.current_temperature} độ C / Ngưỡng an toàn: {self.safety_threshold} độ C)"
        return "Trạng thái: Nhiệt độ trong ngưỡng an toàn."


class HybridSmartActuator(ProductionRobot, ThermalSensor):
    # Kế thừa đa hình theo MRO: HybridSmartActuator -> ProductionRobot -> ThermalSensor -> BaseDevice -> object
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def track_performance(self):
        oee_status = super(ProductionRobot, self).track_performance() # Gọi hàm của ProductionRobot
        temp_status = super(ThermalSensor, self).track_performance() # Gọi hàm của ThermalSensor (thông qua MRO)
        return f"{oee_status}\n{temp_status}"

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
             return f"Nguy hiểm: Vượt ngưỡng nhiệt! (Nhiệt độ hiện tại: {self.current_temperature} độ C / Ngưỡng an toàn: {self.safety_threshold} độ C)"
        if self.completed_products > 10000:
             return f"Cảnh báo: Sản lượng đạt {self.completed_products}, cần bảo dưỡng định kỳ!"
        return "Trạng thái: Lai (Hybrid) hoạt động ổn định toàn phần."


# ==========================================
# 2. CỔNG NGOẠI VI & HÀM DUCK TYPING
# ==========================================

class MQTTEngineGateway:
    def process_stream(self, device):
        logger.info("[Hệ thống MQTT Engine]: Đang khởi tạo băng thông kết nối dữ liệu IoT...")
        logger.info("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
        logger.info(f"Dữ liệu của thiết bị {device.device_code} đã được đóng gói và xuất chuỗi luồng thành công.")

class ERPReportGateway:
    def process_stream(self, device):
        logger.info("[Hệ thống ERP]: Đang đồng bộ CSDL quản trị doanh nghiệp...")
        logger.info("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
        logger.info(f"Dữ liệu của thiết bị {device.device_code} đã được đồng bộ vào ERP thành công.")

def export_telemetry_data(data_gateway, device_object):
    # Loosely Coupled: Chỉ cần object có hàm process_stream (Duck Typing)
    if not hasattr(data_gateway, 'process_stream') or not callable(data_gateway.process_stream):
        raise TypeError("ERR-IOT-05")
    data_gateway.process_stream(device_object)


# ==========================================
# 3. KỊCH BẢN LUỒNG NGHIỆP VỤ (CLI MENU)
# ==========================================

def display_menu():
    print("\n--- RIKKEI SMART FACTORY IOT SIMULATOR ---")
    print("1. Đăng ký & Khởi tạo thiết bị IoT mới")
    print("2. Xem thông tin thiết bị & Thứ tự kế thừa (MRO)")
    print("3. Check-in giờ vận hành & Cập nhật hiệu suất")
    print("4. Thực thi quy trình tự chẩn đoán kỹ thuật")
    print("5. Cộng gộp thời gian tải & So sánh hao mòn")
    print("6. Xuất dữ liệu vận hành ra Cổng ngoại vi")
    print("7. Thoát chương trình")

def main():
    devices_list = []
    current_device = None

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-7): ").strip()

        if choice == '1':
            print("--- ĐĂNG KÝ THIẾT BỊ IOT MỚI ---")
            print("1. Production Robot (Robot sản xuất lắp ráp)")
            print("2. Thermal Sensor (Cảm biến nhiệt độ)")
            print("3. Hybrid Smart Actuator (Thiết bị truyền động lai)")
            
            type_choice = input("Chọn phân loại thiết bị (1-3): ").strip()
            if type_choice not in ['1', '2', '3']:
                print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng.")
                continue

            code = input("Nhập mã thiết bị 10 ký tự: ").strip()
            name = input("Nhập tên thiết bị: ").strip()

            try:
                if type_choice == '1':
                    new_dev = ProductionRobot(device_code=code, device_name=name)
                elif type_choice == '2':
                    new_dev = ThermalSensor(device_code=code, device_name=name)
                elif type_choice == '3':
                    new_dev = HybridSmartActuator(device_code=code, device_name=name)
                
                devices_list.append(new_dev)
                current_device = new_dev
                print(f"[Thành công]: Đăng ký {new_dev.__class__.__name__} thành công!")
                print(f"Tên thiết bị: {current_device.device_name}")
            except ValueError as e:
                if str(e) == "ERR-IOT-01":
                    print("[Lỗi] (ERR-IOT-01): Mã thiết bị không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng tiền tố quy định.")

        elif choice == '2':
            if current_device is None:
                print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                continue
            
            print("--- THÔNG TIN THIẾT BỊ HIỆN TẠI ---")
            print(f"Loại thiết bị: {current_device.__class__.__name__}")
            print(f"Nhà máy: {current_device.factory_name}")
            print(f"Mã thiết bị: {current_device.device_code}")
            print(f"Tên thiết bị: {current_device.device_name}")
            print(f"Số giờ vận hành: {current_device.operating_hours} giờ")
            
            if hasattr(current_device, 'completed_products'):
                print(f"Sản phẩm hoàn thành: {current_device.completed_products} sản phẩm")
            if hasattr(current_device, 'current_temperature'):
                print(f"Nhiệt độ hiện tại: {current_device.current_temperature} độ C")
                
            # Trích xuất MRO
            mro_names = [cls.__name__ for cls in current_device.__class__.__mro__]
            print(f"[Hệ thống MRO]: {' -> '.join(mro_names)}")

        elif choice == '3':
            if current_device is None:
                print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                continue
            
            print("--- GHI NHẬN SỐ LIỆU VẬN HÀNH ---")
            try:
                hours_str = input("Nhập số giờ chạy mới phát sinh: ")
                if not hours_str.replace('.', '', 1).isdigit() or float(hours_str) <= 0:
                     raise ValueError("ERR-IOT-03")
                hours = float(hours_str)
                current_device.add_operating_hours(hours)

                if hasattr(current_device, 'completed_products'):
                    prod_str = input("Nhập số lượng sản phẩm hoàn thành mới bổ sung: ")
                    if not prod_str.isdigit() or int(prod_str) < 0:
                        raise ValueError("ERR-IOT-03")
                    current_device.completed_products += int(prod_str)
                
                if hasattr(current_device, 'current_temperature'):
                    temp_str = input("Nhập nhiệt độ môi trường hiện tại: ")
                    try:
                        temp = float(temp_str)
                        current_device.current_temperature = temp
                    except ValueError:
                         raise ValueError("ERR-IOT-03")

                print("[Thành công]: Đã cập nhật số liệu vận hành.")
                print(f"Tổng số giờ chạy tích lũy: {current_device.operating_hours} giờ.")
                
                # Gọi Đa hình (Polymorphism)
                print(current_device.track_performance())

            except ValueError as e:
                if str(e) == "ERR-IOT-03":
                    print("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
                else:
                    print("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")

        elif choice == '4':
            if current_device is None:
                print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                continue
            
            print("--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
            # Gọi đa hình run_diagnostic
            diag_result = current_device.run_diagnostic()
            if "Cảnh báo" in diag_result or "Nguy hiểm" in diag_result:
                print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
            print(f"Kết quả chẩn đoán: {diag_result}")
            print(f"Định mức chi phí bảo trì hệ thống dự kiến: {current_device.base_maintenance_cost:,.0f} VND")

        elif choice == '5':
            if current_device is None:
                print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                continue
            
            if len(devices_list) < 2:
                print("Chưa có đủ 2 thiết bị trong hệ thống để so sánh.")
                continue

            print("--- KIỂM KÊ & SO SÁNH TẢI (OPERATOR OVERLOADING) ---")
            print(f"Thiết bị hiện tại (A): {current_device.device_code} (Số giờ chạy: {current_device.operating_hours} giờ)")
            
            print("Danh sách thiết bị có thể so sánh:")
            for idx, dev in enumerate(devices_list):
                if dev != current_device:
                    print(f"[{idx}] {dev.device_code} ({dev.device_name} - Số giờ chạy: {dev.operating_hours} giờ)")
            
            try:
                target_idx = int(input("Chọn số ID [?] của thiết bị đối ứng (B): "))
                target_device = devices_list[target_idx]
                
                if current_device < target_device:  # Gọi __lt__
                    comp_text = "ÍT HƠN"
                else:
                    comp_text = "LỚN HƠN HOẶC BẰNG"
                print(f"[Kết quả So sánh (__lt__)]: Hao mòn (số giờ chạy) của thiết bị A {comp_text} thiết bị B.")
                
                total_hours = current_device + target_device  # Gọi __add__
                print(f"[Kết quả Tổng hợp (__add__)]: Tổng thời gian tải vận hành của cả 2 thiết bị là: {total_hours} giờ.")
                
            except (ValueError, IndexError):
                print("[Lỗi]: Lựa chọn ID thiết bị không hợp lệ.")
            except TypeError as e:
                if str(e) == "ERR-IOT-04":
                    print("[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")

        elif choice == '6':
            if current_device is None:
                print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                continue
            
            print("--- XUẤT DỮ LIỆU VẬN HÀNH RA CỔNG NGOẠI VI ---")
            print("1. Xuất dữ liệu qua cổng MQTT (Cloud Stream)")
            print("2. Đồng bộ số liệu vào hệ thống quản trị ERP")
            print("3. Cổng ngoại vi giả mạo (Dùng để test lỗi)")
            
            gw_choice = input("Chọn cổng kết nối ngoại vi (1-3): ").strip()
            
            gateway = None
            if gw_choice == '1':
                gateway = MQTTEngineGateway()
            elif gw_choice == '2':
                gateway = ERPReportGateway()
            elif gw_choice == '3':
                class FakeGateway: pass
                gateway = FakeGateway() # Không có process_stream
                
            if gateway:
                try:
                    export_telemetry_data(gateway, current_device)
                except TypeError as e:
                    if str(e) == "ERR-IOT-05":
                        print("[Lỗi] (ERR-IOT-05): Xung đột kiến trúc! Không thể xuất dữ liệu do cấu hình cổng ngoại vi không tương thích.")
            else:
                print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng.")

        elif choice == '7':
            print("Cảm ơn bạn đã sử dụng hệ thống Quản lý Thiết bị Rikkei Smart Factory IoT Pro!")
            break
            
        else:
            print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")

if __name__ == "__main__":
    main()