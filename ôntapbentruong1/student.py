class Student:
    def __init__(self, student_id, name, class_name):
        self.id = student_id
        self.name = name
        self.class_name = class_name

    def show_info(self):
        print(f"{self.id} | {self.name} | {self.class_name}")