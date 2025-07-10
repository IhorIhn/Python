class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def display_info(self):
        print(f"Студент: {self.name} {self.surname}, вік: {self.age}, середній бал: {self.average_grade}")


student1 = Student("Ivan", "Shevchenko", 20, 91.5)
print("Початкове значення середнього балу:")
student1.display_info()

student1.update_average_grade(95.0)
print("Після зміни середнього балу:")
student1.display_info()
