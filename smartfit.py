#customer details
name = input("Enter Your Name:")
age = int(input("Enter Age:"))

if age<18:
    print("You are eligible for Teen Fitness Program.")

elif age>=18 and age<=40:
    print("You are eligible for the Regular Fitness Program.")

else:
    print("You are eligible for the Senior Wellness Program.")

#medical conditions details
medical_conditions = input("Do you have any medical condition(s) (yes or no)?:").strip().lower()

if medical_conditions not in ("yes","no"):
    print("Invalid input please enter yes or no.")

elif age>=40 and medical_conditions == "yes":
    print("Medical clearance required before joining.")

elif age<40 or medical_conditions == "no":
    print("You can proceed with registration.")

#Membership Details
membership = input("Choose Membership Type (Basic/Premium):")

if membership == "Basic":
    training = input("Do you want a personal training (Yes/No)?:")
    if training == "Yes":
        print("Basic plan with personal training: $45 per month")
    elif training == "No":
        print("Basic plan: $30 per month")
        if membership=="Basic" and training== "No":
            print("Consider upgrading to Premium for more benefits")

if membership == "Premium":
    print("Premium plan: $60 per month")
    if membership == "Premium" and age<30:
        print("You qualify for a youth discount! 10% off your plan.")
    if medical_conditions == "yes" and membership == "Premium":
        print("We recommend a free consultation before starting")        
