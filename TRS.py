user = ""

def airways():
    a_user = ""
    name_l = []
    age_l = []
    gender_l = []
    print("\n Flight Ticket Booking System\n")
    while a_user != "4":
        print("\nWelcome to flight Ticket Reservation\n")
        print("1. Book Ticket\n2. Display ticket\n3. Confirmation\n4. Go back to Home Page\n")
        a_user = input("\nPlease select from above options: ")
        if a_user == "1":
            loc = input("Choose Destination: ")
            print("\nChoose Flight type: ")
            print("1. Business Class\n2. Economic Class\n3. First Class\n")
            fc = input("Choose your flight class: ")
            if fc == "1":
                fc = "Business Class"
            if fc == "2":
                fc = "Economic Class"
            if fc == "3":
                fc == "First Class"
            people = int(input("Enter the number of people travelling: "))
            for p in range(people):
                name = str(input("\nName: "))
                name_l.append(name)
                age = str(input("\nAge: "))
                age_l.append(age)
                gender = str(input("\nGender: "))
                gender_l.append(gender)
            print("Your ticket is booked")
        if a_user == "2":
            x = 0
            print("\nTickets Booked: ", people)
            for p in range(1,people+1):
                print("\nTicket: ", p)
                print("Destination: ", loc)
                print("Flight type: ", fc)
                print("Name: ", name_l[x])
                print("Age: ", age_l[x])
                print("Gender: ", gender_l[x])
                x += 1 
        if a_user == "3":
            conf = input("\nConfirm your reservation(y/n): ")
            conf = conf.lower()
            if conf == "y":
                print("Thank you for confirming your reservation. Have a safe journey.")
            else:
                print("Your reservation is not confirmed yet!")
        if a_user == "4":
            print("Thank you for visiting. Have a good day!")

def bus():
    b_user = ""
    name_l = []
    age_l = []
    gender_l = []
    print("\n Bus Ticket Booking System\n")
    while b_user != "4":
        print("\nWelcome to Bus Ticket Reservation\n")
        print("1. Book Ticket\n2. Display ticket\n3. Confirmation\n4. Go back to Home Page\n")
        b_user = input("\nPlease select from above options: ")
        if b_user == "1":
            loc = input("Choose Destination: ")
            print("\nChoose Bus type: ")
            print("1. AC\n2. Non-AC")
            fc = input("Choose your bus: ")
            if fc == "1":
                fc = "AC"
            if fc == "2":
                fc = "Non-AC"
            people = int(input("Enter the number of people travelling: "))
            for p in range(people):
                name = str(input("\nName: "))
                name_l.append(name)
                age = str(input("\nAge: "))
                age_l.append(age)
                gender = str(input("\nGender: "))
                gender_l.append(gender)
            print("Your ticket is booked")
        if b_user == "2":
            x = 0
            print("\nTickets Booked: ", people)
            for p in range(1,people+1):
                print("\nTicket: ", p)
                print("Destination: ", loc)
                print("Bus type: ", fc)
                print("Name: ", name_l[x])
                print("Age: ", age_l[x])
                print("Gender: ", gender_l[x])
                x += 1 
        if b_user == "3":
            conf = input("\nConfirm your reservation(y/n): ")
            conf = conf.lower()
            if conf == "y":
                print("Thank you for confirming your reservation. Have a safe journey.")
            else:
                print("Your reservation is not confirmed yet!")
        if b_user == "4":
            print("Thank you for visiting. Have a good day!")

def railways():
    r_user = ""
    name_l = []
    age_l = []
    gender_l = []
    print("\n Railway Ticket Booking System\n")
    while r_user != "4":
        print("\nWelcome to Railway Ticket Reservation\n")
        print("1. Book Ticket\n2. Display ticket\n3. Confirmation\n4. Go back to Home Page\n")
        r_user = input("\nPlease select from above options: ")
        if r_user == "1":
            loc = input("Choose Destination: ")
            print("\nChoose Bus type: ")
            print("1. AC First Class\n2. AC Second Class\n3. First Class\n4. Second Class")
            fc = input("Enter your train class: ")
            if fc == "1":
                fc = "AC First Class"
            if fc == "2":
                fc = "AC Second Class"
            if fc == "3":
                fc = "First Class"
            if fc == "4":
                fc = "Second Class"
            
            people = int(input("Enter the number of people travelling: "))
            for p in range(people):
                name = str(input("\nName: "))
                name_l.append(name)
                age = str(input("\nAge: "))
                age_l.append(age)
                gender = str(input("\nGender: "))
                gender_l.append(gender)
            print("Your ticket is booked")
        if r_user == "2":
            x = 0
            print("\nTickets Booked: ", people)
            for p in range(1,people+1):
                print("\nTicket: ", p)
                print("Destination: ", loc)
                print("Train type: ", fc)
                print("Name: ", name_l[x])
                print("Age: ", age_l[x])
                print("Gender: ", gender_l[x])
                x += 1 
        if r_user == "3":
            conf = input("\nConfirm your reservation(y/n): ")
            conf = conf.lower()
            if conf == "y":
                print("Thank you for confirming your reservation. Have a safe journey.")
            else:
                print("Your reservation is not confirmed yet!")
        if r_user == "4":
            print("Thank you for visiting. Have a good day!")

while user != "4":
    print("\n\nTicket Reservation System\n")
    print("1. Airways\n2. Bus\n3. Railways\n4. Exit")
    user = input("\nPlease select from above options: ")
    if user == "1":
        airways()
    if user == "2":
        bus()
    if user == "3":
        railways()
    if user == "4":
        print("Thank you! Have a great day.")
