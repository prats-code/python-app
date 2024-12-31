import time

def main_menu():
    print("\nWelcome to the Smart City Solutions App")
    print("Choose a category to explore:")
    print("1. Sustainability")
    print("2. Transportation")
    print("3. Technology")
    print("4. Search Solutions")
    print("5. Leave Feedback")
    print("6. Exit")
    
    choice = get_valid_choice("Enter your choice (1-6): ", ["1", "2", "3", "4", "5", "6"])
    
    if choice == "1":
        sustainability_menu()
    elif choice == "2":
        transportation_menu()
    elif choice == "3":
        technology_menu()
    elif choice == "4":
        search_solutions()
    elif choice == "5":
        feedback_menu()
    elif choice == "6":
        print("\nThank you for exploring Smart City Solutions!")
        exit()

def sustainability_menu():
    print("\n--- Sustainability Solutions ---")
    print("1. Solar Energy Integration")
    print("2. Smart Waste Management")
    print("3. Vertical Farming in Urban Areas")
    print("4. Rainwater Harvesting Systems")
    print("5. Return to Main Menu")
    
    choice = get_valid_choice("Enter your choice (1-5): ", ["1", "2", "3", "4", "5"])
    
    if choice == "1":
        print("Proposal: Integrate solar panels across all public buildings.")
    elif choice == "2":
        print("Proposal: Implement IoT-based smart bins to optimize waste collection.")
    elif choice == "3":
        print("Proposal: Establish vertical farms in cities to promote local food production.")
    elif choice == "4":
        print("Proposal: Implement rainwater harvesting systems in urban areas.")
    elif choice == "5":
        main_menu()

def transportation_menu():
    print("\n--- Transportation Solutions ---")
    print("1. Electric Vehicle Charging Stations")
    print("2. AI Traffic Management Systems")
    print("3. Autonomous Public Transport")
    print("4. Return to Main Menu")
    
    choice = get_valid_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    
    if choice == "1":
        print("Proposal: Build charging stations every 5 km within city limits.")
    elif choice == "2":
        print("Proposal: Use AI to monitor and optimize traffic flow in real-time.")
    elif choice == "3":
        print("Proposal: Implement autonomous buses to reduce traffic and pollution.")
    elif choice == "4":
        main_menu()

def technology_menu():
    print("\n--- Technology Solutions ---")
    print("1. Smart Sensors for Water and Air Quality")
    print("2. Citywide WiFi for Connectivity")
    print("3. AI-based Waste Sorting")
    print("4. Return to Main Menu")
    
    choice = get_valid_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    
    if choice == "1":
        print("Proposal: Deploy sensors to monitor water and air quality in real-time.")
    elif choice == "2":
        print("Proposal: Provide free citywide WiFi for enhanced connectivity.")
    elif choice == "3":
        print("Proposal: Implement AI-based waste sorting systems for better recycling.")
    elif choice == "4":
        main_menu()

def search_solutions():
    print("\n--- Search Solutions ---")
    query = input("Enter a keyword (e.g., solar, traffic, WiFi): ").lower()
    solutions = {
        "solar": "Integrate solar panels across all public buildings.",
        "waste": "Implement IoT-based smart bins to optimize waste collection.",
        "charging": "Build charging stations every 5 km within city limits.",
        "traffic": "Use AI to monitor and optimize traffic flow in real-time.",
        "sensors": "Deploy sensors to monitor water and air quality in real-time.",
        "wifi": "Provide free citywide WiFi for enhanced connectivity."
    }
    results = [v for k, v in solutions.items() if query in k]
    if results:
        print("\nSearch Results:")
        for result in results:
            print("- " + result)
    else:
        print("No matching solutions found.")
    main_menu()

def feedback_menu():
    print("\n--- Feedback Menu ---")
    feedback = input("Enter your feedback: ")
    print("Thank you for your feedback!")
    main_menu()

def get_valid_choice(prompt, valid_choices):
    choice = input(prompt)
    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input(prompt)
    return choice

# Start the app
main_menu()
