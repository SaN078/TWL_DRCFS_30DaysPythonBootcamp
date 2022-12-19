import constant
import string

print("There are currently " + str(constant.STUDENT_COUNT) + " number of participants")
print("There are currently" + str(constant.CURRENT_MENTOR_COUNT) + "number of mentors")

# for importing variables

from constant import CURRENT_MENTOR_COUNT, STUDENT_COUNT

print("There are currently ", STUDENT_COUNT , " students.")

def add_one(num):
    print(num+1)

def greet(name):
    print(f"Hi {name}!")

naam = input("Hi what is your name?")
greet(naam)
#type hint
def square_number(number: int):
    return(number*number)

print(square_number(12))

def cube(numm):
    result = numm * numm * numm
    return result

variable = 'abc'

print(variable in string.ascii_uppercase)