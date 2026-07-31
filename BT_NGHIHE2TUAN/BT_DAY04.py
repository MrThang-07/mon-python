raw_registers = [
    {
        "name": "  Nguyen Van An  ",
        "email": "an.nguyen@gmail.com",
        "phone": "0987654321",
    },
    {
        "name": "Tran Thi Bich",
        "email": "bich_gmail.com",
        "phone": "0912345678",
    },
    {
        "name": "Le Hoang Cuong",
        "email": "cuong@rikkei.edu.vn",
        "phone": "0123456789",
    },
    {
        "name": "  Pham Minh Dung ",
        "email": "dung@gmail.com  ",
        "phone": "0355667788",
    },
]

orders = [
    {
        "id": "DH01",
        "total": "12500000",
        "discount_code": "VIP10",
        "is_vip": True,
    },
    {
        "id": "DH02",
        "total": "450000",
        "discount_code": "INVALID",
        "is_vip": False,
    },
    {
        "id": "DH03",
        "total": "ABC_ERROR",
        "discount_code": "",
        "is_vip": False,
    },
    {
        "id": "DH04",
        "total": "8500000",
        "discount_code": "VIP20",
        "is_vip": True,
    },
]


def validate_registration_input(name, email, phone):
    clean_name = name.strip()
    clean_email = email.strip().lower()
    clean_phone = phone.strip()

    if "@" not in clean_email:
        return clean_name, clean_email, clean_phone, "KHÔNG HỢP LỆ (Thiếu '@')"

    valid_prefixes = ("03", "05", "07", "08", "09")
    if not (
        len(clean_phone) == 10
        and clean_phone.isdigit()
        and clean_phone.startswith(valid_prefixes)
    ):
        return (
            clean_name,
            clean_email,
            clean_phone,
            "KHÔNG HỢP LỆ (Sai đầu số VN)",
        )

    return clean_name, clean_email, clean_phone, "HỢP LỆ"


def safe_process_invoice(order_id, raw_total, discount_code, is_vip):
    try:
        total = float(raw_total)
        discount = 0
        if is_vip and discount_code == "VIP10":
            discount = total * 0.10
        elif is_vip and discount_code == "VIP20":
            discount = total * 0.20

        price_after_discount = total - discount
        vat = price_after_discount * 0.10
        final_total = price_after_discount + vat

        if final_total >= 10000000:
            classification = "HÓA ĐƠN LỚN (VIP)"
        else:
            classification = "HÓA ĐƠN THƯỜNG"

        ck_label = (
            f"CK ({discount_code}): {int(discount):,}"
            if discount > 0
            else f"CK: {int(discount)}"
        )
        print(
            f"[{order_id}] Tiền hàng: {int(total):,} | {ck_label} | VAT 10%: {int(vat):,} -> Tổng: {int(final_total):,} VNĐ [{classification}]"
        )
    except ValueError:
        print(
            f"Xử lý lỗi [{order_id}]: Số tiền '{raw_total}' không hợp lệ! Bỏ qua đơn hàng."
        )


print("BÁO CÁO CHUẨN HÓA & VALIDATE THÔNG TIN ĐĂNG KÝ")
for idx, reg in enumerate(raw_registers, start=1):
    name, email, phone, status = validate_registration_input(
        reg["name"], reg["email"], reg["phone"]
    )
    print(f"[{idx}] {name} | Email: {email} | SĐT: {phone} -> Trạng thái: {status}")

print("\nBÁO CÁO XỬ LÝ HÓA ĐƠN AN TOÀN (TRY-EXCEPT & VAT)")
for order in orders:
    safe_process_invoice(
        order["id"], order["total"], order["discount_code"], order["is_vip"]
    )