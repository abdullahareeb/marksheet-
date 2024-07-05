marks =int(input("ENTER YOUR MARKS"))
rollnumber = int(input("ENTER YOUR ROLL NUMBER"))
grade = ""

if(marks >=90 ):
    grade = "your Grade is A1" 
    
elif(marks >=80):
    grade = "Your Grade is A"
    
elif(marks >=80):
    grade = "Your Grade is b"
    
elif(marks >=80):
    grade = "Your Grade is c"
    
elif(marks >=80):
    grade = "Your Grade is d"
    
else:
    "your are  fail"

print("rollnumber:",rollnumber)
print("marks:",marks)
print("grade:",grade)

# convert tempereture program


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


if __name__ == "__main__":
    print("Temperature Converter between Celsius and Fahrenheit")
    print("============================")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("============================")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")

    else:
        print("Invalid choice. Please enter either 1 or 2.")


# scalene Program


def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

if __name__ == "__main__":
    print("Triangle Type Checker")
    print("=====================")
    side1 = float(input("Enter length of side 1: "))
    side2 = float(input("Enter length of side 2: "))
    side3 = float(input("Enter length of side 3: "))

    triangle_type_result = triangle_type(side1, side2, side3)
    print(f"The triangle with sides {side1}, {side2}, {side3} is a {triangle_type_result}")



# is_leap_year  Program


def is_leap_year(year):
    # Leap year conditions:
    # 1. Divisible by 4
    # 2. Not divisible by 100 unless also divisible by 400

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    year = int(input("Enter a year to check if it is a leap year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")





