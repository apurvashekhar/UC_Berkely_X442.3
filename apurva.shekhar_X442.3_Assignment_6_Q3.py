numbers = [2,20,200,2000]
first_part = list(map(lambda x: x + 8, numbers))
print(first_part)

second_part = [number + 8 for number in numbers]
print(second_part)
