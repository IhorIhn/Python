while True:
    word = input("Enter the word: ")
    if "h" in word.lower():
        break
    else:
        print("You have entered the word without the letter H")

print("Thank you, you have entered the word with the letter H")
