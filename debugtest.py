import time;


def coacheeProfile():
    print("Coachee Profile Interface");

    print("\n\n__________Profile__________")
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
                weight = float(input("Height, in meters: "));
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
        

        f = open('coachee_profile.txt','a')     
        f.write(f'lol || {name} | {age} | {contact_no} | {weight} | {height}')
        f.close()
        print("\n\nProcessing...")
        time.sleep(2)

        print("\n*** Dear",name, ", your profile has been successfully updated. ***\n")
        
        print("Redirecting back to Coachee Page...\n");

    elif(opt == 'n'):
        print("Okay. Redirecting to Coachee Page...");

coacheeProfile()