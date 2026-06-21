def show_menu():
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Thêm sinh viên\n2. Hiển thị danh sách\n3. Tìm sinh viên theo mã")
    print("4. Cập nhật điểm\n5. Xóa sinh viên\n6. Sắp xếp theo điểm tăng dần")
    print("7. Tính điểm trung bình\n0. Thoát")

def add_student(students):
    student_id = input("Nhập mã: ")
    name = input("Nhập tên: ")
    try:
        score = float(input("Nhập điểm: "))
        if score < 0 or score > 10:
            raise Exception("Điểm phải từ 0 đến 10")
        students.append({"id": student_id, "name": name, "score": score})
        print("Thêm thành công!")
    except ValueError:
        print("Điểm không hợp lệ")
    except Exception as e:
        print(e)

def display_students(students):
    for s in students:
        print(f"{s['id']} - {s['name']} - {s['score']}")

def find_student(students, student_id):
    for s in students:
        if s["id"] == student_id:
            return s
    return None

def update_score(students):
    student_id = input("Nhập mã cần sửa: ")
    student = find_student(students, student_id)
    if student:
        try:
            score = float(input("Nhập điểm mới: "))
            if score < 0 or score > 10:
                raise Exception("Điểm phải từ 0 đến 10")
            student["score"] = score
            print("Cập nhật thành công!")
        except ValueError:
            print("Điểm không hợp lệ")
        except Exception as e:
            print(e)
    else:
        print("Không tìm thấy!")

def delete_student(students):
    student_id = input("Nhập mã cần xóa: ")
    student = find_student(students, student_id)
    if student:
        students.remove(student)
        print("Xóa thành công!")
    else:
        print("Không tìm thấy!")

def sort_students(students):
    students.sort(key=lambda s: s["score"])
    print("Đã sắp xếp tăng dần!")

def calculate_average(students):
    if not students: 
        return 0.0
    
    # Dùng vòng lặp cộng dồn thủ công thay cho hàm sum()
    total = 0.0
    for s in students:
        total += s["score"]
        
    return total / len(students)

def main():
    students = []
    while True:
        show_menu()
        choice = input("Chọn chức năng: ")
        if choice == "1": add_student(students)
        elif choice == "2": display_students(students)
        elif choice == "3":
            sid = input("Nhập mã cần tìm: ")
            res = find_student(students, sid)
            print(f"{res['id']} - {res['name']} - {res['score']}" if res else "Không tìm thấy!")
        elif choice == "4": update_score(students)
        elif choice == "5": delete_student(students)
        elif choice == "6": sort_students(students)
        elif choice == "7": print(f"Điểm trung bình: {calculate_average(students):.2f}")
        elif choice == "0": break
        else: print("Chọn sai, nhập lại!")

if __name__ == "__main__":
    main()