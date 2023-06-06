import os;
import time;
import string;
import random;

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
        a, b, id, status = info.split(" | ");
        a = a.strip();
        b = b.strip();
        id = id.strip();
        status = status.strip();

        if(username == a and password == b):
            print(f"\nCongratulations! Login is Successful, welcome back {username}.");
            time.sleep(2);
            return(username, password, id, status);

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

    idGen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5));

    file = open("registry.txt", "r");

    if(idGen in file):
        while(idGen in file):
            idGen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5));

    file.close();

    file = open("registry.txt", "a");
    file.write(f"{username} | {password} | {idGen} | COACHEE\n");
    file.close();

    clear();
    print(f"User Successfully Created. Welcome COACHEE {username}.\n");
    print(f"Your uniquely generated UserID is [ {idGen} ] ");
    print(f"\n\nReturning to Login Screen...");

    time.sleep(2);
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
        a, b, c, d = login();

        if(d == "COACHEE"):
            coachee(a,b,c,d);
        elif(d == "COACH"):
            coach(a,b,c,d);

    elif(opt == '2'):
        register();

def coachee(username, password, id, status):
    clear();

    print(f"Welcome, COACHEE {username}!");
    print(f"Your UserID is: {id}\n");
    print("COACHEE INTERFACE\n");

    print("_________________________________________________________\n");
    allMsg = getMsg(username, id);
    if len(allMsg) == 0:
        print(f"Dear {username}, you do not have any unread notifications.");
    else:
        print(f"Dear {username}, you have unread notifications.\n");
        print(f"Unread Messages ({len(allMsg)})");
        count = 1;
        for msg in allMsg:
            a, b, c = msg.split(" | ");
            a = a.strip();
            b = b.strip();
            c = c.strip();

            print(f"[{count}] | From: {b} | Message: {c}");
            count += 1;
    
        opt = "";
        while(opt != 'y' or opt != 'n'):
            opt = input(("\n\nDo you want to clear your messages? [ Y \ N ]\n")).lower();
            if(opt == 'y' or opt == 'n'):
                break;
            else:
                print("Please Enter a Valid Input. [ Y / N ]\n");

        if(opt == 'y'):
            file = open("messageLog.txt", "r");
            lines = file.readlines();
            file.close();

            file = open("messageLog.txt", "w");
            for line in lines:
                info = line.split(" | ");
                if(info[0] != username):
                    file.write(line);
            file.close();

        print("Your Messages have Been Successfully Cleared!\n");

    print(f"Dear Coachee, What Would you Like to Do?\n");

def coach(username, password, id, status):
    clear();

    print(f"Welcome, COACH {username}!\n");
    print("COACH INTERFACE");

    print("testing messaging system");
    message(username);

def getMsg(username, id):
    file = open("messageLog.txt", 'r');

    allMsg = [];

    for info in file:
        recipient, sender, content = info.split(" | ");
        recipient = recipient.strip();
        sender = sender.strip();
        content = content.strip();

        if(recipient == username):
            allMsg.append(info);

    file.close();
    return allMsg;

def message(username):

    receive = input("To who do you want to send a message to?\n( !Enter their UserID! )");

    file = open("registry.txt", 'r');

    for info in file:
        a, b, id, status = info.split(" | ");
        a = a.strip();
        b = b.strip();
        id = id.strip();
        status = status.strip();

        name = "";

        if(receive == id):
            name = a;
            break;

    file.close();
    print(f"You are sending a message to: {name}");
    content = input("Please Enter Your Message Below:\n");
    
    file = open("messageLog.txt", 'a');
    
    file.write(f"{name} | {username} | {content}\n");

    file.close();

def clearMsg(username):
    pass;    

#Function that runs first
# MAIN FUNCTION START
def main():
    clear();
    loginSys();

# MAIN FUNCTION END 
main();