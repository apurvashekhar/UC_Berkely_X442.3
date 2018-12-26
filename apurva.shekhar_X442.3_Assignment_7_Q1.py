def convert_to_number(string):
    try:
        num = float(string)
        print(num)
    except ValueError:
        print("Text can't be converted into a number.")

#alternate way
def convert_to_number_alternate(string):
    if string.isdigit():
        number = float(string)
        print(number)
    else:
        print("Text can't be converted into a number.")

string = input("Enter here:")
convert_to_number(string)
convert_to_number_alternate(string)
