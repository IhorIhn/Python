import sqlite3
import random

# -----------------------------
# 1. Підключення до бази
# -----------------------------
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# -----------------------------
# 2. Створення таблиць
# -----------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_course (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
''')

# -----------------------------
# 3. Додавання курсів
# -----------------------------
course_titles = ["Math", "Physics", "Chemistry", "Biology", "History"]
for title in course_titles:
    cursor.execute("INSERT INTO courses (title) VALUES (?)", (title,))
conn.commit()

# -----------------------------
# 4. Додавання 20 студентів
# -----------------------------
student_names = [f"Student{i}" for i in range(1, 21)]
for name in student_names:
    cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
conn.commit()

# -----------------------------
# 5. Рандомне розподілення студентів по курсах
# -----------------------------
cursor.execute("SELECT id FROM students")
student_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM courses")
course_ids = [row[0] for row in cursor.fetchall()]

for student_id in student_ids:
    selected_courses = random.sample(course_ids, k=random.randint(1,3))
    for course_id in selected_courses:
        cursor.execute("INSERT INTO student_course (student_id, course_id) VALUES (?, ?)",
                       (student_id, course_id))
conn.commit()

# -----------------------------
# 6. Додавання нового студента
# -----------------------------
cursor.execute("INSERT INTO students (name) VALUES (?)", ("Ihor",))
new_student_id = cursor.lastrowid

# Додаємо на курс "Math"
cursor.execute("SELECT id FROM courses WHERE title = ?", ("Math",))
math_course_id = cursor.fetchone()[0]

cursor.execute("INSERT INTO student_course (student_id, course_id) VALUES (?, ?)",
               (new_student_id, math_course_id))
conn.commit()

# -----------------------------
# 7. Запити до бази даних
# -----------------------------
# Студенти на курсі "Physics"
cursor.execute('''
SELECT s.name 
FROM students s
JOIN student_course sc ON s.id = sc.student_id
JOIN courses c ON c.id = sc.course_id
WHERE c.title = ?
''', ("Physics",))
physics_students = [row[0] for row in cursor.fetchall()]
print("Students in Physics:", physics_students)

# Курси для "Student1"
cursor.execute('''
SELECT c.title
FROM courses c
JOIN student_course sc ON c.id = sc.course_id
JOIN students s ON s.id = sc.student_id
WHERE s.name = ?
''', ("Student1",))
student1_courses = [row[0] for row in cursor.fetchall()]
print("Student1 courses:", student1_courses)

# -----------------------------
# 8. Оновлення даних
# -----------------------------
# Зміна назви курсу "History" на "World History"
cursor.execute("UPDATE courses SET title = ? WHERE title = ?", ("World History", "History"))

# Зміна імені студента
cursor.execute("UPDATE students SET name = ? WHERE name = ?", ("John Doe", "Student1"))
conn.commit()

# -----------------------------
# 9. Видалення студента "Alex"
# -----------------------------
cursor.execute("DELETE FROM student_course WHERE student_id = ?", (new_student_id,))
cursor.execute("DELETE FROM students WHERE id = ?", (new_student_id,))
conn.commit()

# -----------------------------
# 10. Підсумковий вивід всіх студентів та курсів
# -----------------------------
cursor.execute('''
SELECT s.name, GROUP_CONCAT(c.title)
FROM students s
LEFT JOIN student_course sc ON s.id = sc.student_id
LEFT JOIN courses c ON sc.course_id = c.id
GROUP BY s.id
''')
all_students = cursor.fetchall()
for name, courses in all_students:
    print(f"{name}: {courses}")

# -----------------------------
# Закриваємо з'єднання
# -----------------------------
conn.close()
