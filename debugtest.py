import time;

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
            if(a != '1' and a != '2'):
                print("Please Enter a Valid Input! [ 1 / 2]");

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

calories_tracker();