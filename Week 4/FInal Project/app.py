#esssential constants
RESPONSE_FILE = r'Week 4/Final Project/response.txt'
OPTION1 = 'Followed the ancient map. \n Decided to follow the ancient map that you haveve obtained, you will need to navigate through treacherous terrain and decipher clues to find your way to the lost city. However, the map is old and faded, and you may encounter traps and other dangers along the way'
OPTION2 = 'Seeked help from the native inhabitants'
OPTION3 = 'Used technology to scan for the lost city'



def option1():
    print("You decide to follow the ancient map that you've obtained, you'll need to navigate through treacherous terrain and decipher clues to find your way to the lost city. However, the map is old and faded, and you may encounter traps and other dangers along the way.")
    
    
    
    
    
    exit()

def option2():
    print("If you decide to seek help from the native inhabitants of the planet, you'll need to establish communication and earn their trust. However, they may be hostile or have their own agendas, and you may have to make difficult compromises to gain their assistance.")
    
    
    
    exit()


def option3():
    print("If you decide to use your advanced technology to scan for the lost city, you'll need to calibrate your equipment and analyze the data to pinpoint its location. However, the planet's harsh environment may interfere with your scans and you may not be able to get a clear reading.")
    
    
    
    
    
    exit()

print("Hello there!!, Welcome to the world of endless possibilities. KHANREAH")
while True:
    print("-"*100)
    print("Before beginning may I register your name please?")
    print("-"*100)
    print("No matter what option you choose, your choices will determine your success or failure in finding the lost city. Will you be able to uncover its secrets and treasures, or will you be thwarted by the dangers of the alien planet? The choice is yours!")
    User_name = input("Name::")
    print(f"Hi, {User_name} You are a group of space explorers who have landed on a distant planet in search of a mysterious lost city rumored to hold unimaginable treasures and secrets. The planet is hostile and dangerous, with intense weather patterns and alien creatures that roam the surface.")
    print("As you embark on your quest, you come across a number of obstacles and challenges that require you to make tough decisions.")
    print("What do you do?")
    print("Option 1:  Follow the ancient map\n\n")
    print("Option 2: Seek help from the native inhabitants\n\n")
    print("Option 3:Use technology to scan for the lost city\n\n")
    user_picks = input("Option::")
    
    try:
        user_choice = int(user_picks)
        if user_choice == 1:
            option1()
            #with open(RESPONSE_FILE ,'w') as file:
                #file.write(OPTION1)

        elif user_choice == 2:
            option2()
            #with open(RESPONSE_FILE ,'w') as file:
                #file.write(OPTION2)
        elif user_choice == 3:
            option3()
            #with open(RESPONSE_FILE ,'w') as file:
                #file.write(OPTION3)
        else:
            print("Try choosing a correct option pls :)")
            break
    except Exception as error:
        print(f"An error was raised {error}")