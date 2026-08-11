import json
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.marks = []
    def add_mark(self, mark):
        self.marks.append(mark)
    def average(self):
        sum(self.marks)
        len(self.marks)
        return sum(self.marks) / len(self.marks)       
student1 = Student("Александр", "10")
student2 = Student("Олег", "10")
for i in range(3):
    mark = int(input("Какую оценку хотите поставить?: "))
    student1.add_mark(mark)
for i in range(3):
    mark = int(input("Какую оценку хотите поставить?: "))
    student2.add_mark(mark)
print(student1.average())
print(student2.average())
students = [student1, student2]
def save_students():
    all_data = []
    for student in students: 
        student_data = {"name": student.name, "grade": student.grade, "marks": student.marks}
        all_data.append(student_data)
    file = open("students.json", "w")
    json.dump(all_data, file, ensure_ascii=False)
    file.close()
save_students()
file = open("students.json", "r")
data = json.load(file)
file.close()
print(data)
loaded_students = []
for item in data:
    new_student = Student(item["name"], item["grade"])
    new_student.marks = item["marks"]
    loaded_students.append(new_student)