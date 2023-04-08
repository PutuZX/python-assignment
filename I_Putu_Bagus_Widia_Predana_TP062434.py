#I Putu Bagus Widia Predana
#TP062434

#Main Menu===========================================================================
def main_menu():
    print("=== Welcome to Real Champions Sport Academy ===\n")
    num = input("Who are you?\n"
                            "1. Admin\n"
                            "2. Student\n"
                            "3. Nothing\n"
                            "Answer: ")

    if(num == '1'):
        admin_menu()
    elif(num == '2'):
        student_menu()
    elif(num == '3'):
        exit_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry?(type 'Yes' to retry)\nAnswer: "))
        if(retry == 'Yes' or retry == 'yes'):
            main_menu()
        else:
            exit_menu()

#Exit Menu===========================================================================
def exit_menu():
        print("\n=== Thank You For Visiting and See You! ^_^  ===\n")

#Retry Menu
def retry_menu():
    print("\nSorry, your input is not valid."
          "\nPlease input the number that according with the list above!\n")
#====================================================================================

#Admin Function

#Admin Menu==========================================================================
def admin_menu():
    print("\n=== Sign-in to Admin Menu ===\n")
    UserID = str(input("Please enter your Username ID = "))
    Pass = str(input("Please Enter your password = "))

    if(UserID == "Admin462" and Pass == "12345"):
        admin_main_menu()

    else:
        retry = (input("\nSorry, your ID or Password are wrong.\n"
        "Do you want to try again? (Yes/No)"
        "\nAnswer: "))
        if(retry == "Yes" or retry == "yes"):
            admin_menu()
        else:
            exit_menu()

#Admin Main Menu=====================================================================
def admin_main_menu():
    print("\n=== Welcome Admin ===\n")
    records = input("What do you want to do?\n"
                        "1. Add Records\n"
                        "2. Display All Records\n"
                        "3. Search Specific Records\n"
                        "4. Sort and Display\n"
                        "5. Modify Records\n"
                        "6. Exit\n"
                        "Answer: ")

    if(records == '1'):
        add_records_menu()
    elif(records == '2'):
        display_all_records()
    elif(records == '3'):
        search_specific_records()
    elif(records == '4'):
        sort_display()
    elif(records == '5'):
        modify_records()
    elif(records == '6'):
        exit_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry?(type 'Yes' to retry)\nAnswer: "))
        if(retry == 'Yes' or retry == 'yes'):
            admin_main_menu()
        else:
            exit_menu()

#Add Records Menu====================================================================
def add_records_menu():
    add = input("\nWhich records that you want to add?\n"
                "1. Coach\n"
                "2. Sport\n"
                "3. Sport Schedule\n"
                "4. Nothing\n"
                "Answer: ")
    
    if(add == '1'):
        add_coach_records()
    elif(add == '2'):
        add_sport_records()
    elif(add == '3'):
        add_sport_schedule()
    elif(add == '4'):
        admin_main_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry or back?(type 'retry' to retry)\nAnswer: "))
        if(retry == 'retry'):
            add_records_menu()
        else:
            exit_menu()

#Add Coach Records===================================================================
def add_coach_records():
    adminfile = open("coach-records.txt","a")
    coach_id = str(input("\nEnter the Coach ID = "))
    coach_name = str(input("Enter the coach name = "))
    date_joined = str(input("Enter the date joined (dd/mm/yyyy) = "))
    termination_date = str(input("Enter the termination date (dd/mm/yyyy) = "))
    hourly_rate  = str(input("Enter the hourly rate in RM = "))
    phone = str(input("Enter the phone number = "))
    address = str(input("Enter the address = "))
    SC_code = str(input("Enter the sport center code = "))
    SC_name = str(input("Enter the sport center name = "))
    sport_code = str(input("Enter the sport code = "))
    sport_name = str(input("Enter the sport name = "))
    rating = str(input("Enter the rating = "))

    adminfile.write(coach_id+" | "+coach_name+" | "+date_joined+" | "+termination_date+" | "+hourly_rate+" | "+phone+" | "+address+" | "+SC_code+" | "+SC_name+" | "+sport_code+" | "+sport_name+" | "+rating+"\n")
    adminfile.close()

    ask = str(input("Do you want to add more? (Type 'Yes' if you want)\n"
                    "Answer: "))
    if(ask == 'Yes' or ask == 'yes'):
        add_coach_records()
    else:
        ask2 = str(input("type '0' or anything to save the records and go back to Admin Main Menu : "))
        if(ask2 == '0'):
            print("Save Successful!!")
            admin_main_menu()
        else:
            print("Save Successful!!")
            admin_main_menu()

#student records======================================================================================
def student_records():
    adminfile = open("student-records.txt","r")
    print("\n=== List of student records ===")

    for records in adminfile:
        records = records.strip("\n")
        records = records.split(" | ")

        print("\nStudent ID = "+records[0])
        print("Student name = "+records[1])
        print("Password = "+records[2])
        print("Date of birth = "+records[3])
        print("Email = "+records[4])
        print("Phone = "+records[5])
        print("Address = "+records[6])
        print("Sport Center name = "+records[7])
        print("Sport name = "+records[8])
    adminfile.close()

#Coach Records========================================================================
def coach_records():
    adminfile = open("coach-records.txt","r")
    print("\n=== List of coach records ===")
    for records in adminfile:
        records = records.strip("\n")
        records = records.split(" | ")

        print("\nCoach ID = "+records[0])
        print("Coach name = "+records[1])
        print("date joined = "+records[2])
        print("termination date = "+records[3])
        print("hourly rate in RM = "+records[4])
        print("Phone number = "+records[5])
        print("Address = "+records[6])
        print("Sport center code = "+records[7])
        print("Sport center name = "+records[8])
        print("Sport code = "+records[9])
        print("Sport name = "+records[10])
        print("Rating = "+records[11])
    adminfile.close()
#Sport Records========================================================================
def sport_records():
    adminfile = open("sport-records.txt","r")
    print("\n=== List of sport records ===")
    for records in adminfile:
        records = records.rstrip("\n")
        records = records.split(" | ")

        print("\nSport code = "+records[0])
        print("Sport name = "+records[1])
        print("Sport center code = "+records[2])
        print("Sport center name = "+records[3])
        print("Sport fees in RM = "+records[4])
    adminfile.close()

#Add Sport Records===================================================================
def add_sport_records():
    adminfile = open("sport-records.txt","a")
    sport_code = str(input("\nEnter the sport code = "))
    sport_name = str(input("Enter the sport name = "))
    SC_code = str(input("Enter the sport center code = "))
    SC_name = str(input("Enter the sport center name = "))
    sport_fees = str(input("Enter the sport fees in RM = "))

    adminfile.write(sport_code+" | "+sport_name+" | "+SC_code+" | "+SC_name+" | "+sport_fees+"\n")
    adminfile.close()

    ask = str(input("Do you want to add more? (Type 'Yes' if you want)\n"
                    "Answer: "))
    if(ask == 'Yes' or ask == 'yes'):
        add_sport_records()
    else:
        ask2 = str(input("type '0' or anything to save the records and go back to Admin Main Menu : "))
        if(ask2 == '0'):
            print("Save Successful!!")
            admin_main_menu()
        else:
            print("Save Successful!!")
            admin_main_menu()


#Add Sport Schedule==================================================================
def add_sport_schedule():
    adminfile = open("sport-schedule.txt", "a")
    sport_code = str(input("\nEnter the sport code = "))
    sport_name = str(input("Enter the sport name = "))
    SC_name = str(input("Enter the sport center name = "))
    print("\n(NOTE : each sport must have 2 differences training day a week!)\n")
    training_day = str(input("Enter the traning day (for example 'monday and friday') = "))
    training_hours = str(input("Enter the time (ends with AM/PM) = "))

    adminfile.write(sport_code+" | "+sport_name+" | "+SC_name+" | "+training_day+" | "+training_hours+"\n")
    adminfile.close()

    ask = str(input("Do you want to add more? (Type 'Yes' if you want)\n"
                    "Answer: "))
    if(ask == 'Yes' or ask == 'yes'):
        add_sport_schedule()
    else:
        ask2 = str(input("type '0' or anything to save the records and go back to Admin Main Menu : "))
        if(ask2 == '0'):
            print("Save Successful!!")
            admin_main_menu()
        else:
            print("Save Successful!!")
            admin_main_menu()

#Display All Records Menu============================================================
def display_all_records():
    display = input("\nWhich records that you want to display?\n"
                    "1. Coach\n"
                    "2. Sport\n"
                    "3. Registered Students\n"
                    "4. Nothing\n"
                    "Answer: ")
    
    if(display == '1'):
        coach_records()
        display_all_records()
    elif(display == '2'):
        sport_records()
        display_all_records()
    elif(display == '3'):
        student_records()
        display_all_records()
    elif(display == '4'):
        admin_main_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry or back?(type 'retry' to retry)\nAnswer: "))
        if(retry == 'retry'):
            display_all_records()
        else:
            exit_menu()


#Search Specific Records=============================================================
def search_specific_records():
    spec = str(input("\nWhat do you want to search?\n"
                     "1. Coach by Coach ID\n"
                     "2. Coach by overall performance (Rating)\n"
                     "3. Sport by Sport ID\n"
                     "4. Student by Student ID\n"
                     "5. Nothing\n"
                     "Answer: "))
    
    if(spec == '1'):
        spec_coach_id()
    elif(spec == '2'):
        spec_coach_rating()
    elif(spec == '3'):
        spec_sport_id()
    elif(spec == '4'):
        spec_student_id()
    elif(spec == '5'):
        admin_main_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry or back?(type 'retry' to retry)\nAnswer: "))
        if(retry == 'retry'):
            search_specific_records()
        else:
            exit_menu()

#Student by Student ID==================================================================
def spec_student_id():
    data = input("\nEnter the student ID to search in file: ")
    adminfile = open("student-records.txt","r")
    for line in adminfile:
        line = line.rstrip("\n")
        if(line.startswith(data)):
            line = line.split(" | ")
            print("\n=== This the student record ===")
            print("\nStudent ID = "+line[0])
            print("Student name = "+line[1])
            print("Password = "+line[2])
            print("Date of birth = "+line[3])
            print("Email = "+line[4])
            print("Phone = "+line[5])
            print("Address = "+line[6])
            print("Sport Center name = "+line[7])
            print("Sport name = "+line[8])
    
    adminfile.close()
    print("\nNote: if there's nothing displayed, it means you put an invalid student ID")
    ask = str(input("\nDo you want to search again? (Type 'Yes' if you want)\nAnswer: "))
    if(ask == 'Yes' or ask == 'yes'):
        spec_student_id()
    else:
        search_specific_records()

#Sport by Sport ID======================================================================
def spec_sport_id():
    data = input("\nEnter the sport ID to search in file: ")
    adminfile = open("sport-records.txt","r")
    for line in adminfile:
        line = line.rstrip("\n")
        if(line.startswith(data)):
            line = line.split(" | ")
            print("\n=== This is the sport records ===")
            print("\nSport code = "+line[0])
            print("Sport name = "+line[1])
            print("Sport center code = "+line[2])
            print("Sport center name = "+line[3])
            print("Sport fees in RM = "+line[4])
    
    adminfile.close()
    print("\nNote: if there's nothing displayed, it means you put an invalid sport ID")
    ask = str(input("\nDo you want to search again? (Type 'Yes' if you want)\nAnswer: "))
    if(ask == 'Yes' or ask == 'yes'):
        spec_sport_id()
    else:
        search_specific_records()

#Coach by Coach rating===================================================================
def spec_coach_rating():
    data = input("\nEnter the coach rating search in file (1-5): ")
    adminfile = open("coach-records.txt","r")
    for line in adminfile:
        line = line.rstrip("\n")
        if(line.endswith(data)):
            line = line.split(" | ")
            print("\n=== This is the coach records ===")
            print("\nCoach ID = "+line[0])
            print("Coach name = "+line[1])
            print("date joined = "+line[2])
            print("termination date = "+line[3])
            print("hourly rate in RM = "+line[4])
            print("Phone number = "+line[5])
            print("Address = "+line[6])
            print("Sport center code = "+line[7])
            print("Sport center name = "+line[8])
            print("Sport code = "+line[9])
            print("Sport name = "+line[10])
            print("Rating = "+line[11])
    
    adminfile.close()
    print("\nNote: if there's nothing displayed, it means you put an invalid coach rating")
    ask = str(input("\nDo you want to search again? (Type 'Yes' if you want)\nAnswer: "))
    if(ask == 'Yes' or ask == 'yes'):
        spec_coach_rating()
    else:
        search_specific_records()

#Coach by Coach ID======================================================================
def spec_coach_id():
    data = input("\nEnter the coach ID to search in file: ")
    adminfile = open("coach-records.txt","r")
    for line in adminfile:
        line = line.rstrip("\n")
        if(line.startswith(data)):
            line = line.split(" | ")
            print("\n=== This is the coach file ===")
            print("\nCoach ID = "+line[0])
            print("Coach name = "+line[1])
            print("date joined = "+line[2])
            print("termination date = "+line[3])
            print("hourly rate in RM = "+line[4])
            print("Phone number = "+line[5])
            print("Address = "+line[6])
            print("Sport center code = "+line[7])
            print("Sport center name = "+line[8])
            print("Sport code = "+line[9])
            print("Sport name = "+line[10])
            print("Rating = "+line[11])
    
    adminfile.close()
    print("\nNote: if there's nothing displayed, it means you put an invalid coach ID")
    ask = str(input("\nDo you want to search again? (Type 'Yes' if you want)\nAnswer: "))
    if(ask == 'Yes' or ask == 'yes'):
        spec_coach_id()
    else:
        search_specific_records()

#Sort and Display Menu==================================================================
def sort_display():
    sort = str(input("\nSort and display records of: \n"
                     "1. Coaches in ascending order by names\n"
                     "2. Coaches Hourly Pay Rate in ascending order\n"
                     "3. Coaches Overall Performance (rating) in ascending order\n"
                     "4. Nothing\n"
                     "Answer: "))
    
    if(sort == '1'):
        sort_names()
    elif(sort == '2'):
        sort_payment()
    elif(sort == '3'):
        sort_rating()
    elif(sort == '4'):
        admin_main_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry or back?(type 'retry' to retry)\nAnswer: "))
        if(retry == 'retry'):
            sort_display()
        else:
            exit_menu()

#Sort coaches by hourly hours==================================================================
def sort_payment():
    adminfile = open("coach-records.txt","r")
    print("\n=== This is the coach records (sorted by hourly pay rate) ===")
    new_records = []
    for records in adminfile:
        records = records.split(" | ")
        
        temp = records[0]
        records[0] = records[4]
        records[4] = temp

        new = " | ".join(records)
        new_records.append(new)

    n = len(new_records)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if new_records[j]< new_records[minpos]:
                minpos = j

        temp = new_records[i]
        new_records[i] = new_records[minpos]
        new_records[minpos] = temp
    
    for last in new_records:
        last = last.rstrip("\n")
        last = last.split(" | ")

        temp = last[0]
        last[0] = last[4]
        last[4] = temp

        print("\nCoach ID = "+last[0])
        print("Coach name = "+last[1])
        print("date joined = "+last[2])
        print("termination date = "+last[3])
        print("hourly rate in RM = "+last[4])
        print("Phone number = "+last[5])
        print("Address = "+last[6])
        print("Sport center code = "+last[7])
        print("Sport center name = "+last[8])
        print("Sport code = "+last[9])
        print("Sport name = "+last[10])
        print("Rating = "+last[11])

    adminfile.close()
    print("\n=== That's all! Thank you! ===\n")
    sort_display()

#Sort coaches by names==================================================================
def sort_names():
    adminfile = open("coach-records.txt","r")
    print("\n=== This is the coach records (sorted by names) ===")
    new_records = []
    for records in adminfile:
        records = records.split(" | ")
        
        temp = records[0]
        records[0] = records[1]
        records[1] = temp

        new = " | ".join(records)
        new_records.append(new)

    n = len(new_records)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if new_records[j]< new_records[minpos]:
                minpos = j

        temp = new_records[i]
        new_records[i] = new_records[minpos]
        new_records[minpos] = temp
    
    for last in new_records:
        last = last.rstrip("\n")
        last = last.split(" | ")

        temp = last[0]
        last[0] = last[1]
        last[1] = temp

        print("\nCoach ID = "+last[0])
        print("Coach name = "+last[1])
        print("date joined = "+last[2])
        print("termination date = "+last[3])
        print("hourly rate in RM = "+last[4])
        print("Phone number = "+last[5])
        print("Address = "+last[6])
        print("Sport center code = "+last[7])
        print("Sport center name = "+last[8])
        print("Sport code = "+last[9])
        print("Sport name = "+last[10])
        print("Rating = "+last[11])

    adminfile.close()
    print("\n=== That's all! Thank you! ===\n")
    sort_display()

#Sort coaches by rating==================================================================
def sort_rating():
    adminfile = open("coach-records.txt","r")
    print("\n=== This is the coach records (sorted by rating) ===\n")
    new_records = []
    for records in adminfile:
        records = records.split(" | ")
        
        temp = records[0]
        records[0] = records[11]
        records[11] = temp

        new = " | ".join(records)
        new_records.append(new)

    n = len(new_records)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if new_records[j]< new_records[minpos]:
                minpos = j

        temp = new_records[i]
        new_records[i] = new_records[minpos]
        new_records[minpos] = temp
    
    for last in new_records:
        last = last.rstrip("\n")
        last = last.split(" | ")

        temp = last[0]
        last[0] = last[11]
        last[11] = temp

        print("Coach ID = "+last[0])
        print("Coach name = "+last[1])
        print("date joined = "+last[2])
        print("termination date = "+last[3])
        print("hourly rate in RM = "+last[4])
        print("Phone number = "+last[5])
        print("Address = "+last[6])
        print("Sport center code = "+last[7])
        print("Sport center name = "+last[8])
        print("Sport code = "+last[9])
        print("Sport name = "+last[10])
        print("Rating = "+last[11])

    adminfile.close()
    print("=== That's all! Thank you! ===\n")
    sort_display()

#Modify Records Menu====================================================================
def modify_records():
    add = input("\nWhich records that you want to modify?\n"
                "1. Coach\n"
                "2. Sport\n"
                "3. Sport Schedule\n"
                "4. Nothing\n"
                "Answer: ")
    
    if(add == '1'):
        coach_records()
        mod_coach_records()
        mod_coach_engine()
    elif(add == '2'):
        sport_records()
        mod_sport_records()
        mod_sport_engine()
    elif(add == '3'):
        sport_schedule()
        mod_sport_schedule()
        mod_schedule_engine()
    elif(add == '4'):
        admin_main_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry or back?(type 'retry' to retry)\nAnswer: "))
        if(retry == 'retry'):
            modify_records()
        else:
            exit_menu()

#Modify Coach Records===================================================================
def mod_coach_records():
    adminread = open("coach-records.txt", "r+")
    adminwrite = open("temp.txt", "w+")
    line2 = []
    new = []
    modify = []
    data = input("Pick the file by filling the coach ID: ")
    for line in adminread:
        line = line.rstrip("\n")
        if(not line.startswith(data)):
            line = line.split(" | ")
            line2 = " | ".join(line)
            new.append(line2)
    new_str = "\n".join(new)

    question = str(input("Are you want to modify this file? (Type 'Yes' if it correct!)\nAnswer: "))
    if(question == 'Yes' or question == 'yes'):
            
        coach_id = str(input("\nModify the Coach ID = "))
        coach_name = str(input("Modify the coach name = "))
        date_joined = str(input("Modify the date joined (dd/mm/yyyy) = "))
        termination_date = str(input("Modify the termination date (dd/mm/yyyy) = "))
        hourly_rate  = str(input("Modify the hourly rate in RM = "))
        phone = str(input("Modify the phone number = "))
        address = str(input("Modify the address = "))
        SC_code = str(input("Modify the sport center code = "))
        SC_name = str(input("Modify the sport center name = "))
        sport_code = str(input("Modify the sport code = "))
        sport_name = str(input("Modify the sport name = "))
        rating = str(input("Modify the rating = "))

        modify.append(coach_id+" | "+coach_name+" | "+date_joined+" | "+termination_date+" | "+hourly_rate+" | "+phone+" | "+address+" | "+SC_code+" | "+SC_name+" | "+sport_code+" | "+sport_name+" | "+rating+"\n")
        new_modify = "".join(modify)
        adminwrite.write(new_str+"\n"+new_modify)
        adminwrite.close()
        adminread.close()

        ask2 = str(input("type '0' or anything to save the record and go back to Admin Main Menu : "))
        if(ask2 == '0'):
            print("Save Successful!!")
        else:
            print("Save Successful!!")

    else:
        mod_coach_records()

def mod_coach_engine():
    adminread = open("coach-records.txt", "w+")
    adminwrite = open("temp.txt", "r+")       
    for x in adminwrite.readlines():
        adminread.write(x)

    adminwrite.close()
    adminread.close()
    modify_records()

#Modify Sport Schedule===================================================================
def mod_sport_schedule():
    adminread = open("sport-schedule.txt", "r+")
    adminwrite = open("temp.txt", "w+")
    line2 = []
    new = []
    modify = []
    data = input("Pick the file by filling the sport ID: ")
    for line in adminread:
        line = line.rstrip("\n")
        if(not line.startswith(data)):
            line = line.split(" | ")
            line2 = " | ".join(line)
            new.append(line2)
    new_str = "\n".join(new)

    question = str(input("Are you want to modify this file? (Type 'Yes' if it correct!)\nAnswer: "))
    if(question == 'Yes' or question == 'yes'):
            
        sport_code = str(input("\nModify the sport code = "))
        sport_name = str(input("Modify the sport name = "))
        SC_name = str(input("Modify the sport center name = "))
        print("\n(NOTE : each sport must have 2 differences training day a week!)\n")
        training_day = str(input("Modify the traning day (for example 'monday and friday') = "))
        training_hours = str(input("Modify the time (ends with AM/PM) = "))

        modify.append(sport_code+" | "+sport_name+" | "+SC_name+" | "+training_day+" | "+training_hours+"\n")
        new_modify = "".join(modify)
        adminwrite.write(new_str+"\n"+new_modify)
        adminwrite.close()
        adminread.close()

        ask2 = str(input("type '0' or anything to save the records and go back to Admin Main Menu : "))
        if(ask2 == '0'):
            print("Save Successful!!")
        else:
            print("Save Successful!!")

    else:
        mod_sport_schedule()

def mod_schedule_engine():
    adminread = open("sport-schedule.txt", "w+")
    adminwrite = open("temp.txt", "r+")       
    for x in adminwrite.readlines():
        adminread.write(x)

    adminwrite.close()
    adminread.close()
    modify_records()

#Modify Sport Records===================================================================
def mod_sport_records():
    adminread = open("sport-records.txt", "r+")
    adminwrite = open("temp.txt", "w+")
    line2 = []
    new = []
    modify = []
    data = input("Pick the file by filling the coach ID: ")
    for line in adminread:
        line = line.rstrip("\n")
        if(not line.startswith(data)):
            line = line.split(" | ")
            line2 = " | ".join(line)
            new.append(line2)
    new_str = "\n".join(new)

    question = str(input("Are you want to modify this file? (Type 'Yes' if it correct!)\nAnswer: "))
    if(question == 'Yes' or question == 'yes'):
            
        sport_code = str(input("\nModify the sport code = "))
        sport_name = str(input("Modify the sport name = "))
        SC_code = str(input("Modify the sport center code = "))
        SC_name = str(input("Modify the sport center name = "))
        sport_fees = str(input("Modify the sport fees in RM = "))

        modify.append(sport_code+" | "+sport_name+" | "+SC_code+" | "+SC_name+" | "+sport_fees+"\n")
        new_modify = "".join(modify)
        adminwrite.write(new_str+"\n"+new_modify)
        adminwrite.close()
        adminread.close()

        ask2 = str(input("type '0' or anything to save the records and go back to Admin Main Menu : "))
        if(ask2 == '0'):
            print("Save Successful!!")
        else:
            print("Save Successful!!")

    else:
        mod_sport_records()

def mod_sport_engine():
    adminread = open("sport-records.txt", "w+")
    adminwrite = open("temp.txt", "r+")       
    for x in adminwrite.readlines():
        adminread.write(x)

    adminwrite.close()
    adminread.close()
    modify_records()

#Sport Schedule ========================================================================
def sport_schedule():
    adminfile = open("sport-schedule.txt","r")
    print("\n=== This is the sport schedule ===")
    for records in adminfile:
        records = records.strip("\n")
        records = records.split(" | ")

        print("\nSport code = "+records[0])
        print("Sport name = "+records[1])
        print("Sport center = "+records[2])
        print("Training day = "+records[3])
        print("Time = "+records[4])
    adminfile.close()

#Student main menu======================================================================
def student_menu():
    print("=== Student Menu ===")
    ask = input("\nHello!\nWhat do you want to do?\n"
                "1. Register\n"
                "2. Login\n"
                "3. Enter as unregistered student\n"
                "4. Exit\n"
                "Asnwer: ")
    
    if(ask == '1'):
        student_register()
    elif(ask == '2'):
        student_login()
    elif(ask == '3'):
        all_student()
    elif(ask == '4'):
        exit_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry?(type 'Yes' to retry)\nAnswer: "))
        if(retry == 'Yes' or retry == 'yes'):
            student_menu()
        else:
            exit_menu()
        
#Student login===========================================================================
def student_login():
    studentfile = open("student-records.txt","r")
    print("\n=== Sign-in to your account ===\n")
    UserID = str(input("Please enter your name = "))
    Pass = str(input("Please Enter your password = "))

    for line in studentfile:
        line = line.rstrip("\n")
        line = line.split(" | ")
        if(UserID == line[1] and Pass == line[2]):
            Sport = line[8]
            print("\nHello "+line[1]+"!")
            student_account(UserID, Pass, Sport)
            UserID = False
            Pass = False
    
    if(UserID and Pass != False):
        retry = (input("\nSorry, your ID or Password are wrong.\n"
                   "Do you want to try again? (Yes/No)"
                   "\nAnswer: "))
        if(retry == 'Yes' or retry == 'yes'):
            student_login()
        else:
            exit_menu()

#Student account=========================================================================
def student_account(username, password, sport):
    ask = input("What do you want to do?\n"
                "1. View details of coach\n"
                "2. View details of self-records\n"
                "3. Check the sport schedule\n"
                "4. Modify self-records\n"
                "5. Give feedback and star to coach\n"
                "6. exit\n"
                "Answer: ")
    
    if(ask == '1'):
        student_coach_details(username, password, sport)
        student_account(username, password, sport)
    elif(ask == '2'):
        self_records(username, password, sport)
        student_account(username, password, sport)
    elif(ask == '3'):
        student_sport_schedule(username, password, sport)
        student_account(username, password, sport)
    elif(ask == '4'):
        mod_self_records(username, password, sport)
        mod_SL_engine(username, password, sport)
    elif(ask == '5'):
        feedback(username, password, sport)
        student_account(username, password, sport)
    elif(ask == '6'):
        student_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry?(type 'Yes' to retry)\nAnswer: "))
        if(retry == 'Yes' or retry == 'yes'):
            student_account(username, password, sport)
        else:
            exit_menu()

#All Student============================================================================
def all_student():
    ask = input("\nHello!\nWhat do you want to do?\n"
                "1. View details of sport\n"
                "2. View details of sport schedule\n"
                "3. Register to gain full access\n"
                "4. Nothing\n"
                "Answer: ")
    
    if(ask == '1'):
        sport_records()
        all_student()
    elif(ask == '2'):
        sport_schedule()
        all_student()
    elif(ask == '3'):
        student_register()
        all_student()
    elif(ask == '4'):
        student_menu()
    else:
        retry_menu()
        retry = str(input("Invalid input!! Do you want to retry?(type 'Yes' to retry)\nAnswer: "))
        if(retry == 'Yes' or retry == 'yes'):
            all_student()
        else:
            exit_menu()
    
#Student register======================================================================
def student_register():
    studentfile = open("student-records.txt","a")
    student_id = str(input("Fill your student ID's number (the number is up to you)= Student"))
    student_name = str(input("Fill your name = "))
    password = str(input("Fill your password for your account = "))
    dob = str(input("Fill your date of birth(dd/mm/yyyy) = "))
    email = str(input("Fill your email address = "))
    phone = str(input("Fill your phone number = "))
    address = str(input("Fill your address = "))
    SC_name = str(input("Fill the sport center that you want to join = "))
    sport_name = str(input("Fill the sport name = "))

    studentfile.write("Student"+student_id+" | "+student_name+" | "+password+" | "+dob+" | "+email+" | "+phone+" | "+address+" | "+SC_name+" | "+sport_name+"\n")
    save = str(input("type '0' or anything to save the records and go back to all student menu : "))
    if(save == '0'):
        print("Save Successful!!")
    else:
        print("Save Successful!!")
    studentfile.close()

#self-records of students==================================================================================
def self_records(username, password, sport):
    data = username
    studentfile = open("student-records.txt","r")
    for line in studentfile:
        line = line.rstrip("\n")
        line = line.split(" | ")
        if(data == line[1]):
            print("\n=== This is your record ===")
            print("\nStudent ID = "+line[0])
            print("Student name = "+line[1])
            print("Password = "+line[2])
            print("Date of birth = "+line[3])
            print("Email = "+line[4])
            print("Phone = "+line[5])
            print("Address = "+line[6])
            print("Sport Center name = "+line[7])
            print("Sport name = "+line[8]+"\n")
    studentfile.close()

#modify self-records of students======================================================================
def mod_self_records(username, password, sport):
    studentread = open("student-records.txt", "r+")
    studentwrite = open("temp.txt", "w+")
    line2 = []
    new = []
    modify = []
    data = username
    for line in studentread:
        line = line.rstrip("\n")
        line = line.split(" | ")
        if(not data == line[1]):
            line2 = " | ".join(line)
            new.append(line2)
    new_str = "\n".join(new)

    question = str(input("Type '0' to continue.\nAnswer: "))
    if(question == '0'):
            
        student_id = str(input("Modify your student ID's number (the number is up to you)= Student"))
        student_name = str(input("Modify your name = "))
        password = str(input("Modify your password for your account = "))
        dob = str(input("Modify your date of birth(dd/mm/yyyy) = "))
        email = str(input("Modify your email address = "))
        phone = str(input("Modify your phone number = "))
        address = str(input("Modify your address = "))
        SC_name = str(input("Modify the sport center that you want to join = "))
        sport_name = str(input("Modify the sport name = "))

        modify.append("Student"+student_id+" | "+student_name+" | "+password+" | "+dob+" | "+email+" | "+phone+" | "+address+" | "+SC_name+" | "+sport_name+"\n")
        new_modify = "".join(modify)
        studentwrite.write(new_str+"\n"+new_modify)
        studentwrite.close()
        studentread.close()

        ask2 = str(input("type '0' or anything to save the records and restart your account : "))
        if(ask2 == '0'):
            print("Save Successful!!")
        else:
            print("Save Successful!!")

    else:
        mod_self_records(username, password, sport)

def mod_SL_engine(username, password, sport):
    studentread = open("student-records.txt", "w+")
    studentwrite = open("temp.txt", "r+")       
    for x in studentwrite.readlines():
        studentread.write(x)

    studentwrite.close()
    studentread.close()
    student_login()

#feedback and star============================================================================================
def feedback(username, password, sport):
    data = input("\nPick the coach by coach ID: ")
    studentfile = open("coach-records.txt","r")
    for line in studentfile:
        line = line.rstrip("\n")
        if(line.startswith(data)):
            line = line.split(" | ")
            print("\n=== This is the coach file ===")
            print("\nCoach ID = "+line[0])
            print("Coach name = "+line[1])
            print("date joined = "+line[2])
            print("termination date = "+line[3])
            print("hourly rate in RM = "+line[4])
            print("Phone number = "+line[5])
            print("Address = "+line[6])
            print("Sport center code = "+line[7])
            print("Sport center name = "+line[8])
            print("Sport code = "+line[9])
            print("Sport name = "+line[10])
            print("Rating = "+line[11])
            coach = line[1]
    
    print("\nNote: if there's nothing displayed, it means you put an invalid coach ID")
    ask = str(input("\nDo you want to search for another coach? (Type 'Yes' if you want)\nAnswer: "))
    if(ask == 'Yes' or ask == 'yes'):
        feedback(username, password, sport)
    else:
        feedbackfile = open("Feedback.txt","a")
        star = input("Give star for coach (in number, 1-5) = ")
        Feedback = input("Give feedback for coach = ")

        feedbackfile.write("From: "+username+"\n"+"To: "+coach+"\n"+"Star: "+star+"\n"+"Comment: "+Feedback+"\n"+60*"-"+"\n")
        studentfile.close()
        feedbackfile.close()
        print("Thank you for your feedback!\n")

#Specific Sport Schedule for student ========================================================================
def student_sport_schedule(username, password, sport):
    studentfile = open("sport-schedule.txt","r")
    data = sport
    print("\n=== This is your sport schedule ===")
    for records in studentfile:
        records = records.strip("\n")
        records = records.split(" | ")
        if(data == records[1]):
            print("\nSport code = "+records[0])
            print("Sport name = "+records[1])
            print("Sport center = "+records[2])
            print("Training day = "+records[3])
            print("Time = "+records[4]+"\n")
    studentfile.close()

#Details of coach for registered student ========================================================================
def student_coach_details(username, password, sport):
    studentfile = open("coach-records.txt","r")
    data = sport
    print("\n=== This is your coach details ===")
    for records in studentfile:
        records = records.strip("\n")
        records = records.split(" | ")
        if(data == records[10]):
            print("\nCoach ID = "+records[0])
            print("Coach name = "+records[1])
            print("date joined = "+records[2])
            print("termination date = "+records[3])
            print("hourly rate in RM = "+records[4])
            print("Phone number = "+records[5])
            print("Address = "+records[6])
            print("Sport center code = "+records[7])
            print("Sport center name = "+records[8])
            print("Sport code = "+records[9])
            print("Sport name = "+records[10])
            print("Rating = "+records[11]+"\n")
    studentfile.close()

main_menu()