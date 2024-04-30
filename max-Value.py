def check_numbers(x,y):
    if x*y>100:
        return "100 kishi"
    else:
        return "100 den ulken"
print(check_numbers(50,51))

def find_max(list):
    max_value = float('-inf')
    for i in list:
        if i > max_value:
            max_value = i
    return max_value
print(find_max([1, 2, 3, 4, 5]))