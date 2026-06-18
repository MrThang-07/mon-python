# class Animal:
#     def __init__(self, name ,type):
#         self.name = name
#         self.type = type
#     def breed(self):
#         print("Đây là 1 loaij động vật")
# class Dog(Animal):
#     def __init__(self, name, type, sound):
#         super().__init__(name, type)
#         self.sound = sound

# dog_1 = Dog("Chó corgi", "Chân ngắn", "Ẳng Ẳng")

#  Đa kế thừa
class A:
    def __init__(self):
        pass
    def show(self):
        print("Đây là lớp A")
class B(A):
    def __init__(self):
        super().__init__()
    def show(self):
        print("Đây là lớp B")
class C(A):
    def __init__(self):
        super().__init__()
    def show(self):
        print("Đây là lớp c")
class D(B,C):
    pass

obj_d = D()
print(D.mro())
obj_d.show()

from abc import ABC, abstractmethod
class ThanhToan():
    def xy_ly_tien(self , sotien):
        pass
class ThanhToanMomo(ThanhToan):
    def xu_ly_money(self, so_tien):
        print(f"Momo đang xử lý {so_tien}")

momo_1 = ThanhToanMomo()
momo_1.xu_ly_money(10000)
    