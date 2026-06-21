class Student:
    def __init__(self,id,name,theory_score,practice_score ,project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score =practice_score 
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = ""
    @property
    def id(self):
        return self.__id   
    @property
    def name(self):
        return self.__name
    @property
    def theory_score(self):
        return self.__theory_score
    @property
    def practice_score(self):
        return self.__practice_score
    @property
    def project_score(self):
        return self.__project_score
    @property
    def final_score(self):
        return self.__final_score
    @property
    def academic_rank(self):
        return self.__academic_rank
    def update_theory_score(self,theory_score):
        self.theory_score = theory_score
    def update_practice_score(self,practice_score):
        self.practice_score = practice_score
    def update_project_score(self,project_score):
        self.project_score = project_score
    def calculate_final_score(self):
        self.__final_score = (self.theory_score * 0.2) + (self.practice_score * 0.3) + (self.project_score * 0.5) 

    def classify_academic_rank(self):
        if self.__final_score >= 8.5:
            self.__academic_rank = "giỏi"
        elif self.__final_score >= 7 :
            self.__academic_rank = "khá"
        elif self.__final_score >= 5:
            self.__academic_rank = "trung bình"
        elif self.__final_score < 5 and self.__final_score >= 0:
            self.__academic_rank = "yếu"
    
class StudentManager:
    def __init__(self):
        self.students : list[Student] = []
    def add_student(self):
        stu_id = input("Nhập id :")
        if not stu_id:
            print("Không có mã sv ")
            return
        for stu in self.students:
            if stu.id == stu_id:
                print("Mã sv bị trùng")
                return
        stu_name = input("Nhập Teen sv : ")
        if not stu_name:
            print("Không có tên sv ")
            return
        stu_theory_score = float("Nhập điểm lý thuyết : ")
        stu_practice_score = float("nhập điẻm thực hành : ")
        stu_project_score = float(input("Nhập điểm đồ án : "))
        if not stu_theory_score >= 0 and stu_theory_score <= 10 :
            print("Điểm không hợp lệ ")
            return
        if not stu_practice_score >= 0 and stu_practice_score <= 10 :
            print("Điểm không hợp lệ ")
            return
        if not stu_project_score >= 0 and stu_project_score <= 10 :
            print("Điểm không hợp lệ ")
            return
        new_student = Student(stu_id,stu_name,stu_theory_score,stu_practice_score,stu_project_score)
        new_student.calculate_final_score()
        new_student.classify_academic_rank()
        self.students.append(new_student)
        print("Thêm vào thành công")
    def show_all(self):
        print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<20} | {'Điểm Thực Hành':<20} | {'Điểm Đồ Án':<20} | {'Điểm Tổng Kết':<20} | {'Học Lực':<10}")
        for stu in self.students :
            print(f"{stu.id :<10} | {stu.name :<20} | {stu.theory_score :<20 } | {stu.practice_score:<20} | {stu.project_score:<20} | {stu.final_score:<20} | {stu.academic_rank:<10}")
    def update_students(self):
        stu_id = input("Nhập mã sv cần cập nhật")
        for stu in self.students:
            if stu.id == id:
                stu_theory_score = float("Nhập điểm lý thuyết : ")
                stu_practice_score = float("nhập điẻm thực hành : ")
                stu_project_score = float(input("Nhập điểm đồ án : "))
                if not stu_theory_score >= 0 and stu_theory_score <= 10 :
                    print("Điểm không hợp lệ ")
                    return
                if not stu_practice_score >= 0 and stu_practice_score <= 10 :
                    print("Điểm không hợp lệ ")
                    return
                if not stu_project_score >= 0 and stu_project_score <= 10 :
                    print("Điểm không hợp lệ ")
                    return
                stu.update_theory_score(stu_theory_score)
                stu.update_practice_score(stu_practice_score)
                stu.update_project_score(stu_project_score)
                print("Cập nhật thành công")
        else:
            print("Không tìm thấy sv")
            return
    def delete_student(self):
        
        


            

        