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
            print(f"\nCongratulations! Login is Successful, welcome back {username}.");
            time.sleep(2);
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

def coach(username, password, status):
    clear();

    print(f"Welcome, COACH {username}!\n");
    print("COACH INTERFACE");


#Function that runs first
# MAIN FUNCTION START
def main():
    clear();
    loginSys();

# MAIN FUNCTION END 
main();