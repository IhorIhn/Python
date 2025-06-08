text = input("Please enter a new phrase: ")
unique_letters = set(text)
count = len(unique_letters)
if count > 10:
    print(True)
else:
    print(False)
