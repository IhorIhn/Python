#Task 1
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break  # зупиняємо цикл, якщо результат > 25

        print(f"{number}x{multiplier}={result}")

        multiplier += 1  # збільшуємо лічильник
multiplication_table(3)

#Task2

def suma(a, b):
    result = a + b
    return result

print(suma(3, 5))

#Task 3

def average_number(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

print(average_number([1, 2, 3, 4, 5]))

#Task 4

def reverse_string(text):
    reversed_text = text[::-1]
    return reversed_text
print(reverse_string("Hallilujah"))

#Task 5

def longest_word(word_list):
    longest = max(word_list, key=lambda word: len(word))
    return longest
print(longest_word(["apple", "banana", "blueberry", "watermelon"]))

#Task 6

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

#Task 7

def replace_dots(text):
    return text.replace("...", ".")

text = "Hello... This is my text for this homework... I need to use functions to practice here..."

print(replace_dots(text))

#Task 8

def count_letters(text):
    return text.count('h')
text = "Hello hubba-bubba. This is honesty the highest house there"
print(count_letters(text))

# Task 9

def find_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def count_sentences(text):
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count

def text_analysis(text):
    words = text.split()
    word_count = len(words)
    unique_words = len(set(words))
    longest_word = find_longest_word(words)
    sentence_count = count_sentences(text)
    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "longest_word": longest_word,
        "sentence_count": sentence_count
    }

sample_text = "Hello world! This is a test. Test your code. We all need peace and love in this life."
print(text_analysis(sample_text))

#Task 10

def get_best_student(students):
    best_student = ""
    best_average = 0
    for i in students:
        average = sum(students[i]) / len(students[i])
        if average > best_average:
            best_average = average
            best_student = i
    return best_student, best_average

students = {
    "Max": (10, 11, 9),
    "Ihor": (12, 10, 10),
    "Cherry": (9, 8, 10),
    "Ewa": (11, 12, 12)
}

name, avg = get_best_student(students)
print(f"Найкращий студент: {name} з середнім балом {avg:.2f}")

