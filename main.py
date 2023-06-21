import os;
import time;
import string;
import random;
import re;

#Clear Screen Function
def clear():
    os.system('cls' if os.name =='nt' else 'clear');

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
    pwCheck = input("Enter Your Password Again: ");

    while(password != pwCheck):
        print("Passwords Do Not Match. Please Try Again.");
        password = input("Enter Your Desired Password: ");
        pwCheck = input("Enter Your Password Again: ");
    
    print("Congratulations! Passwords Match.\nProceeding...");
    time.sleep(2);

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

def aboutUs():
    clear();
    time.sleep(1)
    print(">>>>>>>>>>About Us<<<<<<<<<<")
    time.sleep(2)
    print("\nWelcome to FitTrackr. The only Health and Fitness Tracker You Need!\n")
    time.sleep(2)
    print("An app that stays with you and is made to assist you in achieving your wellness and health objectives.\n") 
    time.sleep(2)
    print("Our goals is to lead you to active lifestyles, make wise choices, and realise your full potential.\n")
    time.sleep(2)
    print("The original idea of our application is to allow users to track their daily health progress and to have an idea of their current state of health and fitness.\n\n")
    time.sleep(2)
    print("Our Founders:\n1. Darrance Beh Heng Shek\n2. Chan Hoi Siang\n3. Lai Chee Xiang\n4. Low Wan Jin\n")
    time.sleep(2)
    print("Thank You...\n")
    time.sleep(3)
    input("Press Any Key to return to Login Menu\n");
    print("Redirecting Back to Login Menu...")
    time.sleep(3)
    loginSys();

def checkUsername(username):
    file = open("registry.txt", 'r');

    for info in file:
        a = info.split(" | ")[0];
        if(username == a):
            return True;

    file.close();
    return False;

def changeLoginCredentials(username, password, id, status):
    clear();
    opt = "";
    while(opt != '1' or opt != '2' or opt != '3'):
        opt = input("What Would You Like to Change? \n\n[ 1 ] - Username.\n[ 2 ] - Password.\n[ 3 ] - Cancel.\n\nEnter your Input: ");
        if(opt == '1' or opt == '2' or opt == '3'):
            break;
        else:
            print("Please Enter a Valid Input. [ 1 / 2 / 3 ]\n");

    if(opt == '1'):
        loginChangeUsername(username, password, id, status);
    elif(opt == '2'):
        loginChangePassword(username, password, id, status);
    else:
        print("Operation Cancelled. Redirecting back to User Interface...");
        coachee(username, password, id, status);

def loginChangeUsername(username, password, id, status):
    clear();
    print("What would you like to change your username to?\n");
    print(f"Current Username: {username}");
    newUsername = input("New Username: ");

    while(checkUsername(newUsername)):
        print("User With That Name Already Exists! Please Enter Another Name.\n");
        newUsername = input("New Username: ");
    print("Congratulations! Your Username is Unique. Proceeding...");
    time.sleep(1);

    file = open("registry.txt", "r");
    lines = file.readlines();
    file.close();

    file = open("registry.txt", "w");
    for line in lines:
        info = line.split(" | ");
        if info[0] == username:
            info[0] = newUsername;
            file.write(" | ".join(info));
        else:
            file.write(line);
    file.close();
    
    print("Username change successful! Please login again.");
    print("Redirecting to first screen...\n");
    time.sleep(2)
    loginSys();

def loginChangePassword(username, password, id, status):
    clear();
    print("Request to change password...\n");
    pw = input("Please enter your current password: ");
    if(pw == password):
        print(f"Username: {username}");
        print(f"Current password: {password}\n\n");

        newPassword = input("Enter Your Desired Password: ");
        pwCheck = input("Enter Your Password Again: ");

        while(newPassword != pwCheck):
            print("Passwords Do Not Match. Please Try Again.");
            newPassword = input("Enter Your Desired Password: ");
            pwCheck = input("Enter Your Password Again: ");

        print("\nCongratulations! Passwords Match.\n");
        time.sleep(3);

        file = open("registry.txt", "r");
        lines = file.readlines();
        file.close();

        file = open("registry.txt", "w");
        for line in lines:
            info = line.split(" | ");
            if info[0] == username:
                info[1] = newPassword;
                file.write(" | ".join(info));
            else:
                file.write(line);
        file.close();

        print("Password change successful! Please login again.\n");
        print("Redirecting to Login Menu...\n");
        time.sleep(3);
        loginSys();

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
    clear()
    print("Message Interface\n\n");
    time.sleep(1);
    print("Displaying User List...\n");
    file = open("registry.txt", 'r');

    for lines in file:
        info = lines.split(" | ");
        if(info[3].strip() == "COACHEE" or info[3].strip() == "COACH"):
            print(f"Username: {info[0]}  ||  UserID: {info[2]}  ||  Coach/Coachee: {info[3].strip()}");
            time.sleep(1);

    file.close();
    
    receive = input("\n\nTo who do you want to send a message to?\n( !Enter their Username/UserID! )");

    flag = False;
    file = open("registry.txt", 'r');
    for info in file:
        info.rstrip();

        if re.search(r"\b{}\b".format(receive), info):
            flag = True;
            break;
    file.close();


    if(flag):
        file = open("registry.txt", 'r');

        for info in file:
            a, b, id, status = info.split(" | ");
            a = a.strip();
            b = b.strip();
            id = id.strip();
            status = status.strip();

            name = "";

            if(receive == id or receive == a):
                name = a;
                break;
        file.close();
    else:
        print("That Username/UserID Does not Exist in Our Database.");
        print("Redirecting to Coachee Menu...");
        time.sleep(3);
        coachee(username, password, uid, ustatus);
    
    print(f"\nYou are sending a message to: {name}");
    content = input("Please Enter Your Message Below:\n");
    
    file = open("messageLog.txt", 'a');
    
    file.write(f"{name} | {username} | {content}\n");

    file.close();

    if(ustatus == "COACH"):
        print("\nMessage Successfully Sent.\nRedirecting to Coach Interface...");
        time.sleep(4);
        coach(username, password, uid, ustatus);
    
    else:
        print("\nMessage Successfully Sent.\nRedirecting to Coachee Interface...");
        time.sleep(4);
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

def bmiCalc(username, password, id, status):
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
        print ("You are Obese, You Should REALLY Start Working Out! \n\n")

    input("Press Any Key to Return to User Menu\n");
    print("Redirecting to User Menu...");
    time.sleep(2);
    coachee(username, password, id, status);

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
        name = input("Full Name: ")

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
        
        bmi = round((weight / height**2),2)
        print(f"Based on the Height and Weight you Inputted,\nYour BMI is: {bmi}\n");
        
        if(bmi <= 18.5):
            print("You are Underweight, You Should Gain More Weight!\n")
        elif(18.5 < bmi < 25):
            print ("Your BMI is Normal, Good Job! \n")
        
        elif(25 <= bmi < 30):
            print ("You are Overweight, You Should Start Losing Weight Now! \n")

        else:
            print ("You are Obese, You Should Really Start Losing Some Weight. \n\n")
            
        time.sleep(4);

        bmr = round((88.362 + (13.397 * weight) + (4.799 * (height*100)) - (5.677 * age)), 2)
        print(f"Your BMR, Basal Metabolic Rate is {bmr}kJ per day.\n");
        print(f"You Will Gain Weight if You Eat More Than {bmr}kJ Calories a Day.");
        print(f"You Will Lose Weight if You Eat Less Than {bmr}kJ Calories a Day.");

        time.sleep(4);

        f = open('coacheeProfile.txt','a')     
        f.write(f'{username} ; {id} // {name} | {age} | {contact_no} | {height} | {weight} | {bmi} | {bmr}\n');
        f.close()
        print("\nProcessing...")
        time.sleep(2)

        print("\n*** Dear",name, ", your profile has been successfully updated. ***\n")
        input("Press Any Key to Return to User Menu.\n");
        print("Redirecting to User Menu...");
        time.sleep(2);
        
        coachee(username, password, id, status);

    elif(opt == 'n'):
        print("Okay. Redirecting to Coachee Page...");
        time.sleep(2);
        coachee(username, password, id, status);

def coacheeProfileEdit(username, password, id, status):
    clear();
    
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
            print("Tell us about yourself. \n\n")
            name = input("Full Name: ")

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
        time.sleep(2);
        bmi = round((weight / height**2),2)
        print(f"Based on the Height and Weight you Inputted,\nYour BMI is: {bmi}\n");
        time.sleep(2);

        if(bmi <= 18.5):
            print("You are Underweight, You Should Gain More Weight!\n\n")
        elif(18.5 < bmi < 25):
            print ("Your BMI is Normal, Good Job! \n\n")
        
        elif(25 <= bmi < 30):
            print ("You are Overweight, You Should Start Losing Weight Now! \n\n")

        else:
            print ("You are Obese, You Should Really Start Losing Some Weight. \n\n")
        
        bmr = round((88.362 + (13.397 * weight) + (4.799 * (height*100)) - (5.677 * age)), 2)
        print(f"Your BMR, Basal Metabolic Rate is {bmr}kJ per day.\n");
        print(f"You Will Gain Weight if You Eat More Than {bmr}kJ Calories a Day.");
        print(f"You Will Lose Weight if You Eat Less Than {bmr}kJ Calories a Day.");
        
        time.sleep(4);

        print("\n\nEditing Currently Existing Entry...\n");
        time.sleep(2);

        file = open("coacheeProfile.txt", "r");
        lines = file.readlines();
        file.close();

        file = open("coacheeProfile.txt", "w");
        for line in lines:
            info = line.split(" | ");
            if(info[0] != username):
                file.write(line);
        
        file.write(f'{username} ; {id} // {name} | {age} | {contact_no} | {height} | {weight} | {bmi} | {bmr}\n');
        file.close();

        print("\n*** Dear",name, ", your profile has been successfully updated. ***\n")
        input("Press Any Key to Return to User Menu.\n");
        print("Redirecting to User Menu...");
        time.sleep(2);
        coachee(username, password, id, status);
    
    else:
        print("You Currently Do Not Have a Profile.");
        print("Initializing Profile User Details Creation...");
        time.sleep(2);
        coacheeProfile(username, password, id, status);

def caloriesCalc(username, password, id, status):
    clear();
    print("\nRecord Your Food and Calories Intake!");
    total_calories = 0
    food_list = []
    flag = True;
    
    while flag:
        food = input("\n\n\nWhat Did You Eat Today?\n: ")
        food_calorie = float(input("\nHow many calories (kJ) does it contain?\n: "))
        
        food_list.append(food)
        total_calories += food_calorie
        
        a = "";
        while(a != '1' and a != '2'):
            a = input("\nDo you want to add more? | [1] YES [2] NO\n: ")
            if(a != '1' and a != '2'):
                print("Please Enter a Valid Input! [ 1 / 2 ]");

        if a == "1":
            continue;
        elif a == "2":
            flag = False;
            print("\n-----------------------------  -----------------------------------------")
            print("| Recommended Daily Calorie Intake: 2,000 kJ [WOMEN]   2,500 kJ [MEN] |")
            print("-----------------------------------------------------------------------\n")
            print("Your Food Intake Today:", food_list)
            print("\nYour Total Calories Intake:", round(total_calories,2),"kJ\n")
            time.sleep(3);
            print("\nEstimations State 1 kcal = 0.00013kg");
            time.sleep(2);
            print(f"\nYou Have Gained {round(total_calories * 0.00013,2)} Kilograms of Weight from Your Food Intake Today.");
            time.sleep(2);

            flag2 = False;

            file = open("coacheeProfile.txt", 'r');

            for info in file:
                info.rstrip();

                if re.search(r"\b{}\b".format(username), info):
                    flag2 = True;
                    break;
            
            file.close();

            if(not flag2):
                print("\nYou Have Not Initialized Your Profile.");
                time.sleep(1);
                print("Please Setup Your Profile so That More Information and Statistics can Be Viewed Based on Your Health.");
                input("Press Any Key to Return to User Menu.\n");

                print("Redirecting to User Menu...");
                time.sleep(2);
                coachee(username, password, id, status);
            else:
                mBmr = 0.00;
                file = open("coacheeProfile.txt", 'r');
                for lines in file:
                    split = lines.split(" // ");
                    info = split[1];

                    cred = split[0].split(" ; ");
                    bmr = split[1].split(" | ")[6].strip()

                    if(cred[0] == username):
                        mBmr = float(bmr);
                        print(f"\nYour BMR, Basal Metabolic Rate is: {mBmr}kJ per Day.");
                        time.sleep(2);
                        print(f"\nBased on The Data You Entered, Your Calorie Intake is {total_calories}kJ for Today.");
                        time.sleep(2);
                        print(f"\nYour Net Calorie Output Today is: {mBmr - total_calories}kJ.");
                        time.sleep(2);
                        print(f"\n...Which Approximately Means...");
                        time.sleep(2);
                        if(mBmr - total_calories > 0):
                            print(f"\nYou Have Lost {round((mBmr-total_calories)*0.00013, 2)} Kilograms of Weight Today.");
                        elif(mBmr - total_calories < 0):
                            print(f"\nYou Have Gained {round((mBmr-total_calories) * -1,2)} Kilograms of Weight Today.");
                        else:
                            print(f"\nWow! It is a Break Even! No Weight Gained or Lost Today.");
                file.close();
        break;

    input("Press Any Key to Return to User Menu.\n");
    print("Redirecting to User Menu...");
    coachee(username, password, id, status);

def coacheeViewCoach(username, password, id, status):
    clear();
    print("Viewing Coach List Interface\n\n");

    print("Displaying all Registered Coaches...\n");
    n = 1;
    time.sleep(3);

    file = open("registry.txt", 'r');

    for info in file:
        name, b, uid, uStatus = info.split(" | ");
        uStatus = uStatus.strip();
        if(uStatus) == "COACH":
            print(f"{n} | Username: {name} | UserID: {uid} | Status: {uStatus}");
            time.sleep(1);
    file.close();
    print("All Coaches Displayed.\n");

    input("Press Any Key to Return to User Menu.\n");
    print("Redirecting to User Menu...");
    time.sleep(2);
    coachee(username, password, id, status);

# COACHEE FUNCTIONS end


# COACH FUNCTIONS start

def banUser(username, password, id, status):
    print("Listing all Coachee Usernames and UserIDs...\n");
    time.sleep(2);

    file = open("registry.txt", 'r');
    n = 1

    for lines in file:
        info = lines.split(" | ");
        if(info[3].strip() == "COACHEE"):
            print(f"[{n}] | Username: {info[0]} | UserID: {info[1]}");
            n += 1;
            time.sleep(1);

    file.close();

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
        coach(username, password, id, status);

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
                    info[3] = "BANNED\n";
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

def viewCoacheeDetails(username, password, id, status):
    clear();
    print("Coachee Details Viewing Interface");
    print("\nListing all Coachee Usernames and UserIDs...");
    time.sleep(2);

    file = open("registry.txt", 'r');

    n = 0;

    for lines in file:
        info = lines.split(" | ");
        if(info[3] == "COACHEE\n"):
            print(f"Username: {info[0]}  ||  UserID: {info[2]}");
            n += 1;

    file.close();
    if(n == 0):
        print("No Coachees Registered.\n");
        print("Redirecting to User Menu...");
        time.sleep(3);
    else:
        user = input("\nInput the Username/UserID of the user you want to view details of: ");

        file = open("registry.txt", 'r');

        flag = False;

        for info in file:
            info.rstrip();

            if re.search(r"\b{}\b".format(user), info):
                flag = True;
                break;
        
        file.close();

        if(flag):
            flag2 = False
            file = open("coacheeProfile.txt", 'r');

            for info in file:
                info.rstrip();

                if re.search(r"\b{}\b".format(user), info):
                    flag2 = True;
                    break;
            file.close();
            
            if(flag2):
                file = open("coacheeProfile.txt", 'r');
                for lines in file:
                    split = lines.split(" // ");
                    info = split[1];

                    uName, uId = split[0].split(" ; ");
                    name, age, con, height, weight, bmi, bmr = split[1].split(" | ")

                    if(uName == user or uId == user):
                        print("User Details:\n");
                        print(f"Username: {uName}, UserID: {uId}\n");
                        print(f"Full Name: {name}\nAge: {age}\nContact Number: {con}\nHeight, in Meters: {height}\nWeight, in Kilograms: {weight}\nBMI: {bmi}");
                file.close();
            
            else:
                file.close();
                print("\nThe User has not Initialized their Profile Yet.");
                opt = input("Input any Key to Continue.");
                print("Redirecting to Coach Interface...");
                time.sleep(2);
                coach(username, password, id, status);

            file.close();
        else:
            print("Invalid Input Detected. Please Enter a Valid Username/UserID.\n")
            opt = "";
            while(opt != 'y' or opt != 'n'):
                opt = input("Would you like to Try Again?\n[ (Y)es / (N)o ]\n").lower();
                if(opt == 'y' or opt == 'n'):
                    break;
                else:
                    print("Please Enter a Valid Input. [ Y / N ]\n");

            if(opt == 'y'):
                print("Retrying...\n");
                time.sleep(2);
                viewCoacheeDetails(username, password, id, status);
            else:
                print("Redirecting back to Coach Interface...\n");
                time.sleep(2);
                coach(username, password, id, status);

def coachComment(username, password, id, status):
    file = open("coachComment.txt", 'r');

    contents = file.read();

    file.close();

    print(f"The Current Universal Comment for Coachees is '{contents}'.");
    
    opt = "";
    while(opt != 'y' or opt != 'n'):
        opt = input("Do You Want to Edit It?\n[ (Y)es / (N)o ]\n").lower();
        if(opt == 'y' or opt == 'n'):
            break;
        else:
            print("Please Enter a Valid Input. [ Y / N ]\n");
    
    if(opt == 'y'):
        comment = input("Enter your NEW desired Universal Comment for Coachees: ");
    
        with open("coachComment.txt", "w") as file:
            pass;

        file.close();

        file = open("coachComment.txt", 'w');
    
        file.write(comment);

        file.close();
    
        print(f"Universal Comment for Coachees has been Successfully Edited to: '{comment}'");
        print("Coachees Will See the Comment When They Log-In.\n");
        time.sleep(3);
        print("Redirecting to Coach Interface...");
        time.sleep(2);
        coach(username, password, id, status);
    
    else:
        print("Okay. Redirecting back to Coach Interface...");
        time.sleep(2);
        coach(username, password, id, status);

def coachViewCoachee(username, password, id, status):
    print("View Coachee Interface\n\n");
    print("Displaying All Registered Coachees...\n");

    n = 1;
    file = open("registry.txt", 'r');

    for lines in file:
        info = lines.split(" | ");
        if(info[3] == "COACHEE\n"):
            print(f"{n} | Username: {info[0]} | UserID: {info[2]}");
            n += 1;
            time.sleep(1);

    file.close();

    input("Enter ANY key to Return to User Menu.");
    print("Redirecting to User Menu...");
    time.sleep(2);

    coach(username, password, id, status);

def coachRegister(uUsername, pPassword, iId, sStatus):
    clear();
    print("COACH REGISTRATION INTERFACE\n\n");
    username = input("Enter Your Desired Username: ");

    while(checkUsername(username)):
        print("Username already exists. Please try a new name.");
        time.sleep(2);
        username = input("Enter Your Desired Username: ");
    
    else:
        print("Congratulations! Your desired username is unique.\n");

    print(f"Your Desired Username: {username}\n");
    password = input("Enter Your Desired Password: ");
    pwCheck = input("Enter Your Password Again: ");

    while(password != pwCheck):
        print("Passwords Do Not Match. Please Try Again.");
        password = input("Enter Your Desired Password: ");
        pwCheck = input("Enter Your Password Again: ");
    
    print("Congratulations! Passwords Match.\nProceeding...");
    time.sleep(2);

    idGen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5));

    file = open("registry.txt", "r");

    if(idGen in file):
        while(idGen in file):
            idGen = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5));

    file.close();

    file = open("registry.txt", "a");
    file.write(f"{username} | {password} | {idGen} | COACH\n");
    file.close();

    clear();
    print(f"User Successfully Created. Welcome COACH {username}.\n");
    print(f"Your uniquely generated UserID is [ {idGen} ] ");
    print(f"\n\nReturning to Login Screen...");

    time.sleep(2);
    loginSys();

# COACH FUNCTIONS end


# MAIN COACH AND COACHEE FUNCTIONS start 

def coachee(username, password, id, status):
    clear();

    print(f"Welcome, COACHEE {username}!");
    print(f"Your UserID is: {id}\n");
    print("COACHEE INTERFACE\n");

    print("_________________________________________________________\n");
    allMsg = getMsg(username, id);
    file = open("coachComment.txt", 'r');

    contents = file.read();

    file.close();

    print(f"Universal Comment for Coachees: '{contents}'.");

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
    option = input("Function Options\n[ 1 ] - Send a Message.\n[ 2 ] - Edit Profile Details.\n[ 3 ] - Edit Login Credentials.\n[ 4 ] - Calculate Your BMI!\n[ 5 ] - Calculate Your Calories for Today!\n[ 6 ] - View Coach List.\n\n[ 0 ] - Log Out.\n\nPlease Enter the Respective Function Number ONLY.\n\n");

    while not(option.isdigit() and int(option) < 7 and int(option) >= 0):
        print("\nInvalid Input Detected.\n");
        print("Please Enter a Valid Prompt.\n\n");
        option = input("Function Options\n[ 1 ] - Send a Message.\n[ 2 ] - Edit Profile Details.\n[ 3 ] - Edit Login Credentials.\n[ 4 ] - Calculate Your BMI!\n[ 5 ] - Calculate Your Calories for Today!\n[ 6 ] - View Coach List.\n\n[ 0 ] - Log Out.\n\nPlease Enter the Respective Function Number ONLY.\n\n");

    funcDict = {
        '1' : message,
        '2' : coacheeProfileEdit,
        '3' : changeLoginCredentials,
        '4' : bmiCalc,
        '5' : caloriesCalc,
        '6' : coacheeViewCoach,
        '0' : loginSys,
    };

    if(option == '0'):
        print("Redirecting back to Login Interface...");
        time.sleep(2);
        funcDict[option]();
    else:
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
    option = input("Function Options\n[ 1 ] - Send a Message.\n[ 2 ] - Ban a User.\n[ 3 ] - View Coachee Details.\n[ 4 ] - Edit Universal Comment for Coachees.\n[ 5 ] - View Coachee List.\n[ 6 ] - Create Another Coach Account.\n[ 7 ] - Edit Login Credentials.\n\n[ 0 ] - Log Out.\n\nPlease Enter the Respective Function Number ONLY.\n\n");

    while not(option.isdigit() and int(option) < 8 and int(option) >= 0):
        print("\nInvalid Input Detected.\n");
        print("Please Enter a Valid Prompt.\n\n");
        option = input("Function Options\n[ 1 ] - Send a Message.\n[ 2 ] - Ban a User.\n[ 3 ] - View Coachee Details.\n[ 4 ] - Edit Universal Comment for Coachees.\n[ 5 ] - View Coachee List.\n[ 6 ] - Create Another Coach Account.\n[ 7 ] - Edit Login Credentials.\n\n[ 0 ] - Log Out.\n\nPlease Enter the Respective Function Number ONLY.\n\n");

    funcDict = {
        '1' : message,
        '2' : banUser,
        '3' : viewCoacheeDetails,
        '4' : coachComment,
        '5' : coachViewCoachee,
        '6' : coachRegister,
        '7' : changeLoginCredentials,
        '0' : loginSys,
    };

    if(option == '0'):
        funcDict[option]();
    else:
        funcDict[option](username, password, id, status);

# MAIN COACH AND COACHEE FUNCTIONS end 


#Function that runs first
# MAIN FUNCTIONS START
def loginSys():
    clear();
    print("_____________________________________________________________\n");
    print("                   Welcome to FitTrackr!                       ");
    print("            The Only Fitness Tracker You Need.                 \n\n");
    opt = "";
    a, b, c, d = "", "", "", "";
    while(opt != '1' or opt != '2' or opt != 'a' or opt != 'A'):
        opt = input("Would you like to login or register? \n\n[ 1 ] - Login.\n[ 2 ] - Register.\n[ A ] - About Us.\n\n[ X ] - Exit Program.\n\nEnter your Input: ");
        if(opt != '1' and opt != '2' and opt != 'a' and opt != 'A' and opt != 'x' and opt != 'X'):
            clear();
            print("\n\nPlease Enter a Valid Input.\n[ 1 / 2 / A ]\n");
            time.sleep(2);
            clear();
        else:
            break;
    
    if(opt == '1'):
        a, b, c, d = login();

        if(d == "COACHEE"):
            print(f"\nCongratulations! Login is Successful, welcome back {a}.");
            time.sleep(2);
            coachee(a,b,c,d);
        elif(d == "COACH"):
            print(f"\nCongratulations! Login is Successful, welcome back {a}.");
            time.sleep(2);
            coach(a,b,c,d);
        elif(d == "BANNED"):
            print(f"\nThis Account has been Banned.\nReason for Ban: {c}\n");
            print("Redirecting back to Login Screen...");
            time.sleep(4);
            loginSys();

    elif(opt == '2'):
        register();

    elif(opt == 'a' or opt == 'A'):
        aboutUs();

    elif(opt == 'x' or opt == 'X'):
        clear();
        print("Thank You For Using FitTrackr!");
        print("We Look Forward to Welcoming You Back!");
        time.sleep(3);

def main():
    clear();
    loginSys();

# MAIN FUNCTION END 
main();