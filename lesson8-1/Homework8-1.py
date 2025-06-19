data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def sum_from_string(s):
    try:
        parts = s.split(',')
        numbers = [int(p) for p in parts]
        return sum(numbers)
    except:
        return "Не можу це зробити"
for element in data:
       print(sum_from_string(element))