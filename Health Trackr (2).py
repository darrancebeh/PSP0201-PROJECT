import os;
import time;

#Clear Screen Function
def clear():
    os.system('cls' if os.name =='nt' else 'clear');

def logOrReg():
    opt = input("Would you like to login or register? \n\n[ 1 ] - Login.\n[ 2 ] - Register.\n\nEnter your Input: ");
    if(opt == '1'):
        login();
    elif(opt == '2'):
        register();

def login():
    clear();
    print("LOGIN INTERFACE\n\n");
    username = input("Enter Your Username: ");
    password = input("Enter Your Password: ");

    file = open("registry.txt", 'r');

    for info in file:
        a, b, status = info.split(" | ");
        a = a.strip();
        b = b.strip();
        status = status.strip();

        if(username == a and password == b):
            print(f"\nCongratulations! Login is Successful, Welcome Back {username}.");
            time.sleep(1);
            return username, password, status;

    print("Username or Password is Incorrect. Please Try Again.");
    print("Redirecting to Main Menu...");
    time.sleep(2);
    loginSys();

    file.close();
    

def register():
    clear();
    print("REGISTRATION INTERFACE\n\n");
    username = input("Enter Your Desired Username: ");

    if(checkUsername(username)):
        print("Username already exists. Please try a new name.");
        time.sleep(2);
        register();
    
    else:
        print("Congratulations! Your desired username is unique.\n");

    print(f"Your Desired Username: {username}\n");
    password = input("Enter Your Desired Password: ");

    file = open("registry.txt", "a");
    file.write(f"{username} | {password} | COACHEE\n");
    file.close();

    print(f"User Successfully Created. Welcome COACHEE {username}.")
    loginSys();

def checkUsername(username):
    file = open("registry.txt", 'r');

    for info in file:
        a = info.split(" | ")[0];
        if(username == a):
            return True;

    file.close();
    return False;

def loginSys():
    clear();
    print("_____________________________________________________________\n");
    opt = "";
    while(opt != '1' or opt != '2'):
        opt = input("Would you like to login or register? \n\n[ 1 ] - Login.\n[ 2 ] - Register.\n\nEnter your Input: ");
        if(opt == '1' or opt == '2'):
            break;
        else:
            print("Please Enter a Valid Input. [ 1 / 2 ]\n");
    
    if(opt == '1'):
        a, b, c = login();

        if(c == "COACHEE"):
            coachee(a,b,c);
        elif(c == "COACH"):
            coach(a,b,c);

    elif(opt == '2'):
        register();

def coachee(username, password, status):
    clear();

    print(f"Welcome, COACHEE {username}!\n\n");
    print("COACHEE INTERFACE");
    coachee_homepage()

def coach(username, password, status):
    clear();

    print(f"Welcome, COACH {username}!\n");
    print("COACH INTERFACE");

########################################################################################
########################################################################################
def coachee_homepage():
    print(" ")
    print("********************************")
    print(" ")
    print(" ")
    print("What Can We Help You Today?")
    print(" ")
    print("|    HEALTH    |            Enter 1\n"
          "|    COACH     |            Enter 2\n"
          "|   ABOUT US   |            Enter 3\n"
          "|   PROFILE    |            Enter 4\n"
          "|   SETTING    |            Enter 5\n"
          "|   LOG OUT    |            Enter 0")
    print(" ")
    print("********************************")
    print(" ")
    home_page = input(" ")
    if home_page == "1":
        coachee_health()
                                    
    elif home_page == "2":
        #coach()<-----------
        coachee_homepage()
                                    
    elif home_page == "3":       
        about_us()
        coachee_homepage()
    
    elif home_page == "4":       
        coachee_profile()

    elif home_page == "5":       
        coachee_setting()
                
    elif home_page == "0":
        print("\nLogging Out...")
        time.sleep(3)
        print("\n\nLogged Out Sucessfully.")

    else:
        print("Error! Please enter a correct number.")
        print("Redirecting to menu...")
        time.sleep(1)
        coachee_homepage()

########################################################################################
########################################################################################

def coachee_health():
    print("\n \n-----HEALTH PAGE-----\n")
    print("|   BMI Calculator   |     Enter 1\n"
          "|  Calories Tracker  |     Enter 2\n"
          "|       Return       |     Enter 3\n")
    
    a = input(" ")
    time.sleep(0.5)

    if a == "1":
        print("Directing to BMI Calculator...")
        time.sleep(1)
        bmi_calculator()

    elif a == "2":
        print("Directing to Calories Tracker...")
        time.sleep(1)
        calories_tracker()

    elif a == "3":
        print("Directing to Menu...")
        time.sleep(2)
        coachee_homepage()
        
    else:
        print("Error! Please enter a correct number.")
        print("Redirecting to menu...")
        time.sleep(1)
        coachee_health()


def bmi_calculator():
    
    print("\n\n*****Body Mass Index Calculator*****\n")
    print("\n Calculate your BMI: \n")
    weight = float(input("Enter your weight [kg]: "))
    time.sleep(1)
    height = float(input("Enter your height [m]: "))
    time.sleep(1)

    bmi = round((weight / height**2),2)
    
    if bmi <= 18.5:
        time.sleep(1)
        print("\n\nYour Index is", bmi)
        print("You are Underweight, Get Some Weight Now! \n\n")
        directing_to_health_menu()

    elif 18.5 < bmi < 25:
        time.sleep(1)
        print("\n\nYour Index is", bmi)
        print ("You are Normal, Good Job! \n\n")
        directing_to_health_menu()
    
    elif 25 <= bmi < 30:
        time.sleep(1)
        print("\n\nYour Index is", bmi)
        print ("You are Overweight, Get Workout Now! \n\n")
        directing_to_health_menu()

    else:
        time.sleep(1)
        print("\n\nYour Index is", bmi)
        print ("You are obese, Get Workout Now! \n\n")
        directing_to_health_menu()


def calories_tracker():
    print("\nRecord your calories intake")
    total_calories = 0
    food_list = []
    
    while True:
        time.sleep(1)
        food = input("\nWhat did you ate today?\n: ")
        time.sleep(1)
        food_calorie = float(input("\nHow many calories (kJ) does it contain?\n: "))
        time.sleep(1)
        
        food_list.append(food)
        total_calories += food_calorie
        
        a = "";
        while(a != '1' and a != '2'):
            a = input("\nDo you want to add more? [1] YES [2] NO\n: ")

        if a == "1":
            continue
        elif a == "2":
            print("\n-----------------------------------------------------------------------")
            print("| Recommended Daily Calorie Intake: 2,000 kJ [WOMEN]   2,500 kJ [MEN] |")
            print("-----------------------------------------------------------------------\n")
            print("Your Today's Food Intake:", food_list)
            print("\nYour Total Calories Intake:", total_calories,"\n")
            time.sleep(2)
            input("Press ENTER to return to Mainpage")
            
            print("Redirecting to menu...")
            time.sleep(2)
            coachee_homepage()
        else:
            print("Error! Please enter a valid number.\n")
            time.sleep(1)
            print("Redirecting to menu...")
            time.sleep(2)
            calories_tracker()


    os.system ('read -p "Press ENTER to return to Mainpage"')
    print("Redirecting to menu...")
    time.sleep(3)
    coachee_health()

########################################################################################
########################################################################################

def about_us():
    time.sleep(1)
    print(">>>>>>>>>>About Us<<<<<<<<<<")
    time.sleep(2)
    print("\nWelcome to FitTrackr.\n")
    time.sleep(2)
    print("An app that stays with you and is made to assist you in achieving your wellness and health objectives.\n") 
    time.sleep(2)
    print("Our goals is to lead you to active lifestyles, make wise choices, and realise your full potential.\n")
    time.sleep(2)
    print("Our The original idea of our application is to allow users to track their daily health progress and to have an idea of their current state of health and fitness.\n\n")
    time.sleep(2)
    print("Our Founders:\n1. Darrance Beh Heng Shek\n2. Chan Hoi Siang\n3. Lai Chee Xiang\n4. Low Wan Jin\n")
    time.sleep(2)
    print("Thank You...\n")
    time.sleep(3)
    os.system ('read -p "Press ENTER to to return to Mainpage"')
    print("Redirecting Back to Login Menu...")
    time.sleep(3)
    loginSys();

########################################################################################
########################################################################################
def coachee_profile():
    time.sleep(2)
    print("\n\n__________Profile__________\n")
    print("View   Profile   [1]\nUpdate Profile   [2]\nEdit   Profile   [3]\n    Return       [4]\n")
    a = input("What would you like to do?\n: ")

    if a == "1":
        coachee_profile_view()
    
    elif a == "2":
       coachee_profile_update()
    
    elif a == "3":
        coachee_profile_edit()

    elif a == "4":
        time.sleep(2)
        print("\nRedirecting to Menu...")
        time.sleep(1)
        coachee_homepage()

    else:
        print("Error! Please enter a correct number.")
        time.sleep(1)
        print("Redirecting to profile...")
        time.sleep(2)
        coachee_profile()


def coachee_profile_view():

    time.sleep(2)
    file = open("coacheeProfile.txt", "r")
    file_content = file.read().strip().split(" | ")
    file.close()

    if len(file_content) == 5:

        print("\n   Name    :", file_content[0])
        print("   Age     :", file_content[1])
        print("Contact.no :", file_content[2])
        print("  Weight   :", file_content[3])
        print("  Height   :", file_content[4], "\n")
        time.sleep(3)
        os.system ('read -p "Press ENTER to return to Profile"')
        time.sleep(2)
        print("Redirecting to profile...")
        coachee_profile()
        
    else:
        print("\nNo data found...\n")
        time.sleep(1)
        print("Please update your profile.")
        time.sleep(2)
        coachee_profile()


def coachee_profile_update():

    time.sleep(2)
    file = open("coacheeProfile.txt", "r")
    file_content = file.read().strip().split(" | ")
    file.close()

    if len(file_content) == 5:
        print("\nProfile already exists. Updating is not allowed.")
        time.sleep(2)
        print("\nRedirecting to profile...")
        time.sleep(2)
        coachee_profile()
    
    else:
        time.sleep(1)
        print("\nTell us about yourself. \n")
        name = input("Name: ")
        age = input("Age: ")
        contact_no = input("Contact.no: ")
        weight = input("Weight [kg]: ")
        height = input("Height [m]: ")
 
        f = open('coacheeProfile.txt','a')     
        f.write(f'\n{name} | {age} | {contact_no} | {weight} | {height}\n')
        f.close()
        time.sleep(1)
        print("\nProcessing...")
        time.sleep(3)

        print("\n*** Dear",name, ", your profile had been successfully updated. ***\n")
        time.sleep(1)
        os.system ('read -p "Press ENTER to return to Profile"')
        time.sleep(2)
        print("Redirecting to profile...")
        coachee_profile()


def coachee_profile_edit():
    time.sleep(2)
    a = input("\nWould you like to edit your profile?   YES[1]   NO[2]\n: ")
    
    if a == "1":
        time.sleep(1)
        print("Which would you like to edit?\n")
        print("1. Name")
        print("2. Age")
        print("3. Contact.no")
        print("4. Weight")
        print("5. Height\n")

        b = input('\nEnter Your Choice: \n')
        time.sleep(1) 

        file = open('coacheeProfile.txt','r')
        content = file.read().strip().split(" | ")
        file.close()
        
        if b == "1":    

            new_name = input("Enter your new name\n: ")
            content[0] = new_name
            f = open('coacheeProfile.txt', 'w')
            f.write(" | ".join(content))
            f.close()
            print("\nName updated successfully.")
            update_success()
        
        elif b == "2":
            new_age = input("Enter your new age\n: ")
            content[1] = new_age
            f = open('coacheeProfile.txt', 'w')
            f.write(" | ".join(content))
            f.close()
            print("\nAge updated successfully.")
            update_success()
        
        elif b == "3":
            new_contact_no = input("Enter your new contact.no\n: ")
            content[2] = new_contact_no
            f = open('coacheeProfile.txt', 'w')
            f.write(" | ".join(content))
            f.close()
            print("\nContact.no updated successfully.")
            update_success()
        
        elif b == "4":
            new_weight = input("Enter your new weight [kg]: ")
            content[3] = new_weight
            f = open('coacheeProfile.txt', 'w')
            f.write(" | ".join(content))
            f.close()
            print("\nWeight updated successfully.")
            update_success()

        elif b == "5":
            new_height = input("Enter your new height [m]: ")
            content[4] = new_height
            f = open('coacheeProfile.txt', 'w')
            f.write(" | ".join(content))
            f.close()
            print("\nHeight updated successfully.")
            update_success()
        
        else:
            print("Error! Please enter a correct number.")
            time.sleep(2)
            coachee_profile_edit()

def update_success():
    time.sleep(1)
    os.system ('read -p "Press ENTER to return to Profile"')
    time.sleep(2)
    print("\nRedirecting to profile...")
    coachee_profile()
    
########################################################################################
########################################################################################

def coachee_setting():
    print("\n********** Setting **********\n")
    print("1. Change Password")
    print("2. Return\n")

    a = input("What would you like to do?\n: ")
    time.sleep(1)

    if a == "1":
        b = input("\nWould you like to change your password? [1] YES  [2] NO\n: ")

        if b == "1":
            time.sleep(2)
            c = input("\nPlease enter your current password\n: ")
            time.sleep(1)
            print("\nPlease Wait...")
            time.sleep(2)
            file = open("registry.txt", "r")

            found = False
            new_password = ""

            for line in file:
                username, password, status = line.strip().split(" | ")
                if password == c:
                    found = True
                    new_password = input("\nPlease enter your NEW password\n: ")
                    print("\nPlease Wait...")
                    time.sleep(2)
                    confirm_password = input("\nRe-enter your NEW password\n: ")
                    time.sleep(2)
                    if new_password == confirm_password:
                        break
                    else:
                        print("\nPasswords do not match!")
                        time.sleep(1)
                        print("\nPlease try again...")
                        time.sleep(1)
                        coachee_setting()
            
            file.close()

            if found:
                file = open("registry.txt", "r")
                new_file = open("registry.txt.tmp", "w")

                for line in file:
                    username, password, status = line.strip().split(" | ")
                    if password == c:
                        password = new_password
                    new_file.write(f"{username} | {password} | {status}\n")

                file.close()
                new_file.close()

                os.remove("registry.txt")
                os.rename("registry.txt.tmp", "registry.txt")

                time.sleep(2)
                print("\nCongratulations! Your password had successfully changed.")
                time.sleep(1)
                print("\nRedirecting to settings...")
                time.sleep(2)
                coachee_setting()

            else:
                print("\nIncorrect password!")
                time.sleep(1)
                print("\nPlease try again...")
                time.sleep(1)
                coachee_setting()

        elif b == "2":
            time.sleep(2)
            os.system ('read -p "Press ENTER to to return to Setting"')
            time.sleep(1)
            print("\nRedirecting to settings...")
            coachee_setting()

        else:
            time.sleep(1)
            print("\nError! Please enter a correct number.")
            print("\nRedirecting to settings...")
            time.sleep(1)
            coachee_setting()

    elif a == "2":
        time.sleep(2)
        print("\nRedirecting to Menu...")
        time.sleep(1)
        coachee_homepage()

    else:
        time.sleep(1)
        print("Error! Please enter a correct number.")
        print("Redirecting to menu...")
        time.sleep(1)
        coachee_setting()

########################################################################################
########################################################################################
 
#Function that runs first
# MAIN FUNCTION START
def main():
    clear();
    loginSys();

# MAIN FUNCTION END 
main();