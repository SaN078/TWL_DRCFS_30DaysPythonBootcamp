# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents

import random
import string

USER_PASSWORDS = r"Week 2\Assignments\Users-Pwds(10).txt"
USER_PASSWORDS_WRITE = r"Week 2\Assignments\Users-Pwds-chked.txt"


def rank(pwd: str) -> str:
    """
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as:
    a. Contains less than 3 from the above 4 items ( i – iv ).
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:
    a. Contains 3 from the above 4 items ( i – iv )
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:
    a. Meets all 4 of the above items ( i – iv )
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    """
    ## Start code here
    contains_uppercase = any(char in string.ascii_uppercase for char in pwd)
    contains_lowercase = any(char in string.ascii_lowercase for char in pwd)
    contains_digits = any(char in string.digits for char in pwd)
    contains_specials = any(char in string.punctuation for char in pwd)

    reqs_list = (
        contains_uppercase,
        contains_digits,
        contains_lowercase,
        contains_specials,
    )

    req_counter = 0
    for req in reqs_list:
        if req is True:
            req_counter += 1
    if req_counter < 3 or len(pwd) < 8:
        rank = "POOR"
    elif req_counter < 4 or len() < 10:
        rank = "MODERATE"
    else:
        rank = "STRONG"

    ## End code here
    return rank


def option1():
    """
    Helper function that will be executed when user selects option 1 in the initial case.
    """
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds.
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values.
    # 5. Close necessary files and print to terminal.

    ## START CODE HERE
    username_passwords = open(USER_PASSWORDS, "r").readlines()

    output_list = []
    for username_pwds in username_passwords:
        username, password = username_pwds.split(",")
        password_rank = rank(password)
        output_list.append([username, password, password_rank])

    with open(USER_PASSWORDS_WRITE, "w") as file:
        for val in output_list:
            val_str = ",".join(val)
            file.write(val_str)

    ## END CODE HERE

    print("#" * 80)
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print("[INFO] " + "Number of passwords checked:", str(len(username_passwords)))
    print("[INFO] " + "The given rankings can be found in Users-Pwds-Chked.txt")
    print("#" * 80)


def option2():
    """
    Function to be executed when the user selects option 2 (generate password) in the main loop.

    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    """

    def generate() -> str:
        """
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        """
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ""

        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.

        ## START CODE HERE
        selected_uppercase = [random.choice(Ualphabets) for i in range(5)]
        selected_lowercase = [random.choice(Lalphabets) for i in range(5)]
        selected_digits = [random.choice(digits) for i in range(5)]
        selected_specials = [random.choice(chars) for i in range(5)]

        pwd_list = (
            selected_uppercase
            + selected_lowercase
            + selected_digits
            + selected_specials
        )
        # Rearranging the values
        random.shuffle(pwd_list)

        # Converting to string from list
        pwd = "".join(pwd_list)
        ## END CODE HERE
        return pwd

    # Ask for username and check 20 character limits

    ## START CODE HERE
    username = input("What is your username")
    if len(username) >= 20:
        print("Invalid username")
        raise ValueError("Invalid Username")
    ## END CODE HERE

    # Generate the password using generate() and follow the steps as guided in the function header.
    ## START CODE HERE
    password = generate()
    password_rank = rank(password)

    user_wants_to_write = input(
        "Do you want to write username and password to file? (Y/N)"
    ).lower()
    if user_wants_to_write == "y":
        with open(USER_PASSWORDS_WRITE, "w") as file:
            val_str = ",".join(username, password, password_rank)
            file.write(val_str+"\n")
            
    elif user_wants_to_write == "n":
        print("The generated details are as follows:")
        print(username, password, password_rank)
    ## END CODE HERE


def main():

    print("Welcome to my password ranking program")
    while True:
        print("-" * 40)
        print("Please select one of 3 options")
        print(
            "option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program"
        )
        inp = input("Enter your option here:")

        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else.
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function

        ## START CODE HERE
        try:
            inp = int(inp)
            if inp == 1:
                option1()
            elif inp == 2:
                option2()
            elif inp == 3:
                print("Good Bye!!")
                break
            else:
                print("Enter a valid option pls")
                print("*" * 50)
        except Exception as e:
            print(f"Error was raised: {e}")
        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__ == "__main__":
    main()
