def greet():
    print("----------Medical Expert System----------")
    print("I can help you with basic health advice.")
    print("Please answer the following questions with yes/no.\n")


def get_yes_no(question):
    while True:
        ans = input(question + " (yes/no): ").lower()
        if ans in ["yes", "no"]:
            return ans
        print("Please enter 'yes' or 'no'.")


def diagnose():
    print("\nAnswer a few questions:")

    fever = get_yes_no("Do you have fever?")
    cough = get_yes_no("Do you have cough?")
    headache = get_yes_no("Do you have headache?")
    fatigue = get_yes_no("Do you feel tired/fatigue?")
    stomach_pain = get_yes_no("Do you have stomach pain?")
    vomiting = get_yes_no("Do you have vomiting?")
    cold = get_yes_no("Do you have cold/runny nose?")

    print("\nDiagnosis Result:\n")

    # Rules (Expert System)
    if fever == "yes" and cough == "yes" and fatigue == "yes":
        print("Possible Disease: Flu or Viral Infection")
        print("Recommended Doctor: General Physician")
        print("Advice: Take rest, stay hydrated, and consult a doctor.")

    elif fever == "yes" and headache == "yes" and cold == "yes":
        print("Possible Disease: Common Cold")
        print("Recommended Doctor: General Physician")
        print("Advice: Drink warm fluids and take rest.")

    elif stomach_pain == "yes" and vomiting == "yes":
        print("Possible Disease: Food Poisoning")
        print("Recommended Doctor: Gastroenterologist")
        print("Advice: Avoid solid food and drink fluids.")

    elif headache == "yes" and fatigue == "yes":
        print("Possible Disease: Stress or Migraine")
        print("Recommended Doctor: Neurologist")
        print("Advice: Take rest and avoid screen time.")

    elif fever == "yes":
        print("Possible Disease: Infection")
        print("Recommended Doctor: General Physician")
        print("Advice: Monitor temperature and consult doctor.")

    else:
        print("No major illness detected.")
        print("Advice: Maintain a healthy lifestyle.")

    print("\n  Note: This is a basic expert system. Please consult a real doctor for accurate diagnosis.")


def hospital_facility():
    print("\nHospital Facility Recommendation:\n")

    emergency = get_yes_no("Is it an emergency?")
    if emergency == "yes":
        print("Go to nearest Emergency Room immediately!")
        return

    need_specialist = get_yes_no("Do you need a specialist doctor?")
    if need_specialist == "yes":
        print("Visit a multi-specialty hospital.")
    else:
        print("Visit a nearby clinic or general physician.")


def main():
    greet()
   
    while True:
        print("\nChoose an option:")
        print("1. Get Medical Diagnosis")
        print("2. Hospital Recommendation")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            diagnose()
        elif choice == "2":
            hospital_facility()
        elif choice == "3":
            print("Thank you! Stay healthy.")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()
