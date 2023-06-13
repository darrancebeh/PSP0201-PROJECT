import os;
import time;
import string;
import random;
import re;

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
            return(username, password, id, status);

    print("\n\nIncorrect Username or Password.");
    print("Redirecting to Login Page...");
    file.close();
    time.sleep(2);
    loginSys();

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

def message(username, password, uid, ustatus):
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

    if(ustatus == "COACH"):
        print("Message Successfully Sent.\nRedirecting to Coach Interface...");
        time.sleep(2);
        coach(username, password, uid, ustatus);
    
    else:
        print("Message Successfully Sent.\nRedirecting to Coachee Interface...");
        time.sleep(2);
        coachee(username, password, uid, ustatus);

def clearMsg(username):
    file = open("messageLog.txt", "r");
    lines = file.readlines();
    file.close();

    file = open("messageLog.txt", "w");
    for line in lines:
        info = line.split(" | ");
        if(info[0] != username):
            file.write(line);
    file.close();


# COACHEE FUNCTIONS start

def bmiCalc():
    print("\n\nBody Mass Index Calculator Interface\n\n")
    print("Calculate your BMI!\n")
    weight = float(input("Enter your weight, in kg: "))
    height = float(input("Enter your height, in m: "))

    bmi = round((weight / height**2),2)
    
    if(bmi <= 18.5):
        print(f"Your BMI is {bmi}");
        print("You are Underweight, You Should Gain More Weight!\n\n")

    elif(18.5 < bmi < 25):
        print(f"Your BMI is {bmi}");
        print ("Your BMI is Normal, Good Job! \n\n")
    
    elif(25 <= bmi < 30):
        print(f"Your BMI is {bmi}");
        print ("You are Overweight, You Should Start Working-out Now! \n\n")

    else:
        print(f"Your BMI is {bmi}");
        print ("You are obese, Get Workout Now! \n\n")


def coacheeProfile(username, password, id, status):
    print("Coachee Profile Interface");

    print("\n\n__________Profile__________")
    opt = "";
    while(opt != 'y' or opt != 'n'):
        opt = input("Would you like to create a profile?\n[ (Y)es / (N)o ]\n").lower();
        if(opt == 'y' or opt == 'n'):
            break;
        else:
            print("Please Enter a Valid Input. [ Y / N ]\n");
    
    if(opt == 'y'):
        print("\nTell us about yourself. \n\n")
        name = input("Name: ")

        age = "";
        while not(isinstance(age, int)):
            try:
                age = int(input("Age, in years: "));
            except:
                print("Please enter a valid NUMBER.");
                age = int(input("Age, in years: "));
        
        contact_no = "";
        while not(isinstance(contact_no, int)):
            try:
                contact_no = int(input("Contact.no: "))
            except:
                print("Please enter a valid NUMBER.");
                contact_no = int(input("Contact.no: "))

        height = "";
        while not(isinstance(height, float)):
            try:
                height = float(input("Height, in meters: "));
            except:
                print("Please enter a valid NUMBER.");
                height = float(input("Height, in meters: "));
        
        weight = "";
        while not(isinstance(weight, float)):
            try:
                weight = float(input("Weight, in kilograms: "));
            except:
                print("Please enter a valid NUMBER.");
                weight = float(input("Weight, in kilograms: "));

        f = open('coacheeProfile.txt','a')     
        f.write(f'{username} ; {id} || {name} | {age} | {contact_no} | {weight} | {height}')
        f.close()
        print("\n\nProcessing...")
        time.sleep(2)

        print("\n*** Dear",name, ", your profile has been successfully updated. ***\n")
        
        print("Redirecting back to Coachee Page...\n");
        time.sleep(2);
        coachee(username, password, id, status);

    elif(opt == 'n'):
        print("Okay. Redirecting to Coachee Page...");
        time.sleep(2);
        coachee(username, password, id, status);

def coacheeProfileEdit(username, password, id, status):
    
    file = open("coacheeProfile.txt", 'r');

    flag = False;

    for info in file:
        info.rstrip();

        if re.search(r"\b{}\b".format(username), info):
            flag = True;
            break;
    
    file.close();

    
    if(flag):
        print("You Already have an Existing Profile.\n");
        opt = "";
        
        while(opt != 'y' or opt != 'n'):
            opt = input("Would you like to update your profile?\n[ (Y)es / (N)o ]\n").lower();
            if(opt == 'y' or opt == 'n'):
                break;
            else:
                print("Please Enter a Valid Input. [ Y / N ]\n");

        if(opt == 'y'):
            print("\nTell us about yourself. \n\n")
            name = input("Name: ")

            age = "";
            while not(isinstance(age, int)):
                try:
                    age = int(input("Age, in years: "));
                except:
                    print("Please enter a valid NUMBER.");
                    age = int(input("Age, in years: "));
            
            contact_no = "";
            while not(isinstance(contact_no, int)):
                try:
                    contact_no = int(input("Contact.no: "))
                except:
                    print("Please enter a valid NUMBER.");
                    contact_no = int(input("Contact.no: "))

            height = "";
            while not(isinstance(height, float)):
                try:
                    height = float(input("Height, in meters: "));
                except:
                    print("Please enter a valid NUMBER.");
                    height = float(input("Height, in meters: "));
            
            weight = "";
            while not(isinstance(weight, float)):
                try:
                    weight = float(input("Weight, in kilograms: "));
                except:
                    print("Please enter a valid NUMBER.");
                    weight = float(input("Weight, in kilograms: "));
    
        print("All Inputs Received.");
        print("Editing Currently Existing Entry...\n");
        time.sleep(2);

        file = open("coacheeProfile.txt", "r");
        lines = file.readlines();
        file.close();

        file = open("coacheeProfile.txt", "w");
        for line in lines:
            info = line.split(" | ");
            if(info[0] != username):
                file.write(line);
        
        file.write(f'{username} ; {id} || {name} | {age} | {contact_no} | {weight} | {height}');
        file.close();
        print("Profile Details Successfully Updated.\n\nReturning to User Interface...");
        time.sleep(2);
        coachee(username, password, id, status);
    
    else:
        print("You Currently Do Not Have a Profile.");
        print("Initializing Profile User Details Creation...");
        time.sleep(2);
        coacheeProfile(username, password, id, status);


def coacheeAssignCoach(username, id):
    clear();
    print(f"Your Username: {username}\nYour UserID: {id}");
    print("Coach Assignment Interface...\n");


# COACHEE FUNCTIONS end


# COACH FUNCTIONS start

def removeUser(username, password, id, status):
    print("\nInput '!' to return to previous interface.");
    user = input("Input the Username/UserID of the user you want to ban: ");

    file = open("registry.txt", 'r');

    flag = False;

    for info in file:
        info.rstrip();

        if re.search(r"\b{}\b".format(user), info):
            flag = True;
            break;
    
    file.close();

    if(user == '!'):
        print("Okay. Redirecting to Coach Interface...");
        time.sleep(2);
        coachee(username, password, id, status);

    if(flag):
        file = open("registry.txt", 'r');
    
        for info in file:
            name, b, uid, d = info.split(" | ");
            name = name.strip();
            b = b.strip();
            uid = uid.strip();
            d = d.strip();
        
        if(user == name or user == uid):
            print(f"\n\nThe Details of the User:- \nUsername: {name} | UserID: {uid} | STATUS: {d}");

        file.close();
    
        opt = "";
        while(opt != 'y' or opt != 'n'):
            opt = input(("\n\nAre You Sure That You Want to Ban The User? [ Y \ N ]\n")).lower();
            if(opt == 'y' or opt == 'n'):
                break;
            else:
                print("Please Enter a Valid Input. [ Y / N ]\n");
    
        if(opt == 'y'):
            reason = input("\nPlease Provide a Reason to The Ban: ");
        
            file = open("registry.txt", "r");
            lines = file.readlines();
            file.close();

            file = open("registry.txt", "w");
            for line in lines:
                info = line.split(" | ");

                if info[0] == name:
                    info[3] = "BANNED";
                    info[2] = reason;
                    file.write(" | ".join(info));
                else:
                    file.write(line);

            file.close();
            print("User Successfully Banned.");

            print("Redirecting to Coach Interface...");
            time.sleep(2);
            coachee(username, password, id, status);
        
        else:
            print("Okay. Returning to Coach Interface...");
            time.sleep(2);
            coachee(username, password, id, status);
            
    else:
        print("Invalid Input Detected. Redirecting to Coach Interface...");
        time.sleep(2);
        coachee(username, password, id, status);


# COACH FUNCTIONS end




# MAIN COACH AND COACHEE FUNCTIONS start 

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
            clearMsg(username);
            print("Your Messages have Been Successfully Cleared!\n\n");
        else:
            print("Messages Not Cleared.\n\n")

        time.sleep(2);

    print(f"Dear Coachee, What Would you Like to Do?\n");
    option = input("Function Options\n[ 1 ] - Send a Message.[ 2 ] - Edit Profile Details.\nPlease Enter the Respective Function Number ONLY.\n\n");

    while not(option.isdigit() and int(option) < 3 and int(option) > 0):
        print("\nInvalid Input Detected.\n");
        print("Please Enter a Valid Prompt.\n\n");
        option = input("Function Options\n[ 1 ] - Send a Message.[ 2 ] - Edit Profile Details.\n\nPlease Enter the Respective Function Number ONLY.\n\n");

    funcDict = {
        '1' : message,
        '2' : coacheeProfileEdit,
    };

    funcDict[option](username, password, id, status);

def coach(username, password, id, status):
    clear();

    print(f"Welcome, COACH {username}!");
    print(f"Your UserID is: {id}\n");
    print("COACH INTERFACE");

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
            clearMsg(username);
            print("Your Messages have Been Successfully Cleared!\n\n");
        else:
            print("Messages Not Cleared.\n\n")

        time.sleep(2);

    print(f"Dear Coachee, What Would you Like to Do?\n");
    option = input("Function Options\n[ 1 ] - Send a Message.\n[ 2 ] - Ban a User.\nPlease Enter the Respective Function Number ONLY.\n\n");

    while not(option.isdigit() and int(option) < 2 and int(option) > 0):
        print("\nInvalid Input Detected.\n");
        print("Please Enter a Valid Prompt.\n\n");
        option = input("Function Options\n[ 1 ] - Send a Message.\nPlease Enter the Respective Function Number ONLY.\n\n");

    funcDict = {
        '1' : message,
        '2' : removeUser,
    };

    funcDict[option](username, password, id, status);

# MAIN COACH AND COACHEE FUNCTIONS end 


#Function that runs first
# MAIN FUNCTIONS START
def loginSys():
    clear();
    print("_____________________________________________________________\n");
    opt = "";
    a, b, c, d = "", "", "", "";
    while(opt != '1' or opt != '2'):
        opt = input("Would you like to login or register? \n\n[ 1 ] - Login.\n[ 2 ] - Register.\n\nEnter your Input: ");
        if(opt == '1' or opt == '2'):
            break;
        else:
            print("Please Enter a Valid Input. [ 1 / 2 ]\n");
    
    if(opt == '1'):
        a, b, c, d = login();

        if(d == "COACHEE"):
            print(f"\nCongratulations! Login is Successful, welcome back {a}.");
            time.sleep(1);
            coachee(a,b,c,d);
        elif(d == "COACH"):
            print(f"\nCongratulations! Login is Successful, welcome back {a}.");
            time.sleep(1);
            coach(a,b,c,d);
        elif(d == "BANNED"):
            print(f"\nThis Account has been Banned.\nReason for Ban: {c}\n");
            print("Redirecting back to Login Screen...");
            time.sleep(3);
            loginSys();

    elif(opt == '2'):
        register();

def main():
    clear();
    loginSys();

# MAIN FUNCTION END 
main();