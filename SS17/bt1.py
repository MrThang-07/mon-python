raw_logs = [] 
processed_logs = []


def input_processing(raw_list):
    input_one = input("Nhập vào một đoạn log : ")
    bang_quy_doi = str.maketrans("","","!@#$")
    ket_qua = input_one.translate(bang_quy_doi)
    raw_list = ket_qua.split(";")
    count = len(raw_list)
    print(f"Đã làm sạch và lưu {count} dòng log vào hệ thống")
    return raw_list

def litter_list(raw):
    if len(raw) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return
    processed =[item for item in raw if "ERROR" in item.upper() or "CRITICAL" in item.upper()]
    count = len(processed)
    print("--- LỌC CẢNH BÁO ---")
    print(f"Tìm thấy {count} cảnh báo nguy hiểm:")
    for i in processed:
        print(f"- {i}")
    return processed

def mask_ip(word):
    if "." in word:
        parts = word.split(".")
        if len(parts) == 4:
            parts[2] = "*"
            parts[3] = "*"
            return ".".join(parts)
    return word

def mask_logs_system(processed_list):
    if len(processed_list) == 0:
        print("Chưa có dữ liệu log cảnh báo nguy hiểm. Vui lòng thực hiện chức năng 2 trước!")
        return []

    masked_list = []
    for log in processed_list:
        words = log.split(" ")
        updated_words = []
        for word in words:
            clean_word = mask_ip(word)
            updated_words.append(clean_word)
        masked_log = " ".join(updated_words)
        masked_list.append(masked_log)
    print("\n--- MÃ HÓA IP ---")
    print("Báo cáo log an toàn:")
    stt = 1
    for log in masked_list:
        print(f"{stt}. {log}")
        stt += 1
        
    return masked_list
while True :
    print("""============= SECURITY LOG ANALYZER =============
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
=================================================
""")
    choice = input("Chọn chức năng (1-4): ")
    match (choice):
        case "1":
            raw_logs = input_processing(raw_logs)
        case "2":
            processed_logs = litter_list(raw_logs)
        case "3":
            secured_logs = mask_logs_system(processed_logs)
        case "4":
            print("Cảm ơn bạn đã sử dụng hệ thống Security Log Analyzer!")
            break
        case _:
            print("Vui lòng nhập 1 - 4 !")
