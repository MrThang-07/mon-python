class PTITStudent:
    def __init__(self, name , gpa):
        self.name = name
        self.gpa = gpa
    def say_hi(sefl):
        print(f"Tôi là {sefl.name}, tôi chào cả lớp nha !")
    def sort_student(sefl):
        if sefl.gpa > 3.6:
            print("Suất Xắc")
        elif sefl.gpa > 3.2:
            print("Giỏi")
        elif sefl.gpa > 3.0:
            print("Khá")
        else:
            print("Trung bình")


student_rikkei = PTITStudent("Khiêm", 3.2) 
student_tuxa = PTITStudent("Trứ", 3.7)
student_chinhquy = PTITStudent("Khoa", 4.0)
print(student_rikkei.name ,student_rikkei.gpa)
student_rikkei.say_hi()
student_rikkei.sort_student()