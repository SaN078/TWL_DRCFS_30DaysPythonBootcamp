# fizz buzz is a program that returns 
# fizz if divisible by 3
# buzz if divisible by 5
# fizzbuzzz if divisible by both 3 and 5



for i in range(100):
    #checking if the number is divisible by both 3 and 5
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    #checking if the number is divisible by 3
    elif i%3==0:
        print("Fizz")
    #checking if the number is divisible by 5
    elif i%5==0:
        print("Buzz")
    #if none then it returns i
    else:
        print(i)