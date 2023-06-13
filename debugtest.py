import re;

def removeUser():
    print("\nInput '!' to return to previous interface.");
    user = input("Input the Username/UserID of the user you want to ban: ");

    file = open("registry.txt", 'r');

    flag = False;

    for info in file:
        info.rstrip();

        if re.search(r"\b{}\b".format(user), info):
            flag = 'y';
            break;
    
    file.close();

    if(user == '!'):
        print("Okay. Redirecting to Coach Interface...");
        # time.sleep(2);
        # coachee(username, password, id, status);

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
            # time.sleep(2);
            # coachee(username, password, id, status);
        
        else:
            print("Okay. Returning to Coach Interface...");
            # time.sleep(2);
            # coachee(username, password, id, status);
            
    else:
        print("Invalid Input Detected. Redirecting to Coach Interface...");
        # time.sleep(2);
        # coachee(username, password, id, status);