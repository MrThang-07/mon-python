products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]
def show_products(products_list):
    if len(products_list) == 0 :
        print("Cửa hàng hiện chưa có sản phẩm nào!")
        return
    print(f"{'ID':<5} | {'Tên sản phẩm':<15} | {'Giá bán':<10}")
    for item in products_list:
        print(f"{item['id']:<5} | {item['name']:<15} | {item['price']:<10}")

def add_product(products_list):
    while True:
        add_product = input("Nhập id sản phẩm mới : ").strip().upper()
        if len(add_product) == 0:
            print("Mã sản phẩm không được để trống ! nhập lại")
            continue
        else :
            break
    while True:
        add_name = input("Nhập tên sản phẩm : ").strip()
        if len(add_name) == 0:
            print("Vui lòng nhập lại không rỗng !")
            continue
        else :
            break
    while True:
        add_price = int(input("Nhập giá bán : "))
        if add_price < 0:
            print("Vui lòng nhập số nguyên lớn hơn 0 ! Nhập lại ")
            continue
        else :
            break
    new_product = {'id': add_product, 'name': add_name, 'price': add_price}
    products_list.append(new_product)
    print("Thêm sản phẩm thành công !")

def update_price(products_list):
    found = False
    find_id = input("Nhập ID sản phẩm cần thay đổi giá : ").strip().upper()
    for item in products_list:
        if item["id"] == find_id:
            found = True
            print(f"Tìm thấy sản phẩm : {item['name']} (Giá hiện tại: {item['price']})")
            while True :
                update_price =input("Nhập giá bán mới : ")
                if int(update_price) < 0:
                    print("Vui lòng nhập lại giá !")
                else:
                    break
            item["price"] = int(update_price)
            print("Cập nhật giá thành công!")
            break
    if not found:
        print(f"Không tìm thấy sản phẩm có mã [{find_id}]!")



    

        
while True:
    print("""=====================================
    QUẢN LÝ CỬA HÀNG - MINI STORE
=====================================
1. Xem danh sách sản phẩm hiện có
2. Thêm mới một sản phẩm
3. Cập nhật giá sản phẩm theo ID
4. Thoát chương trình
=====================================
""")
    choice = input("Nhập lựa chọn : ")
    match (choice):
        case "1":
            show_products(products)
        case "2":
            add_product(products)
        case "3":
            update_price(products)
        case "4":
            print("Đã thoát chương trình .")
            break
        case _:
            print("Vui lòng nhập từ 1 -4 ! ")