class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def get_students_money(student):
    return student.fives * 5 + student.tens * 10 + student.twenties * 20


def most_money(students):
    result = []

    for student in students:
        students_money = get_students_money(student)
        result.append(students_money)

    if min(result) == max(result) and len(students) > 1:
        return "all"

    return students[result.index(max(result))].name


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

print(most_money([cam, geoff, phil]))
print(most_money([cam, geoff]))
print(most_money([geoff]))