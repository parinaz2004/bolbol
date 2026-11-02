# name = input("enter your name")
# print(f"hello {name}")


class student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
s1 = student("par", 3924820948, 19)
print(s1.name)
print(s1.student_id)
print(vars(s1))