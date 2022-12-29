#importing random module

import random



def option1():
    ...

def option2():
    ...



def option3():
    ...


def option4():
    option =  random.randint(1,3)
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    
























































































def main():
    print("Hello there!!, Welcome to the world of endless possibilities. KHANREAH")
    while True:
        print("-"*100)
        print("Before beginning may I register your name please?")
        print("-"*100)
        User_name = input("Name::")
        print(f"Hi, {User_name} please choose the time you would like to go to?")
        print("The options are \n 1.1999 \t 2.1000 \n 3.500 \t 4.Random age.")
        user_picks = input("Option::")
    
        try:
            user_choice = int(user_picks)
            if user_choice == 1:
                option1()
            elif user_choice == 2:
                option2()
            elif user_choice == 3:
                option3()
            elif user_choice == 4:
                option4()
            else:
                print("Try choosing a correct option pls :)")
                break
        except Exception as error:
            print(f"An error was raised {error}")

        









if __name__ == "__main__":
    main()