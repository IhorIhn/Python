# 0. Початковий список кортежів
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1. Нова людина
new_person = ('Ihor', 'Ihnatenko', 32, 'QA', 'Kharkiv')
people_records = [new_person] + people_records

# 2. Обмінюємо індекси 1 і 5
people_records[1], people_records[5] = people_records[5], people_records[1]
print("Перелік данних зі змінними індексами:")
for person in people_records:
    print(person)

# 3. Перевірити, чи всі з індексами 6, 10, 13 мають вік ≥ 30
indices_to_check = [6, 10, 13]
all_age_ok = True
for idx in indices_to_check:
    if idx >= len(people_records) or people_records[idx][2] < 30:
        all_age_ok = False

# Вивід результатів
print("Modified list:")
for person in people_records:
    print(person)

print("\nAll people at indexes 6, 10, 13 have age >= 30:", all_age_ok)
