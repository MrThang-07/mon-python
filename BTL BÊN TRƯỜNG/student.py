from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    @abstractmethod
    def show_info(self):
        pass

class Student(Person):
    def __init__(self, student_id, name, class_name):
        super().__init__(student_id, name)
        self.class_name = class_name

    def show_info(self):
        return f"{self.id} | {self.name} | {self.class_name}"