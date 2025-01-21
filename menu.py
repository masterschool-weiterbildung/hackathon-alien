from main import send_sms

# Function to show the menu to the user

def show_menu(number):
    menu = """
    1. Diplomatic Tips & Tricks
    2. Weather on Mars
    3. Klingon Translator
    4. API ISS Information
    5. Exit ("I am OK")
    """
    send_sms(number, "Welcome! Please select an option:\n" + menu)

def process_selection(number, selection):
    """Handle the user’s menu selection"""

    if selection == "1":
        send_sms(number, "You selected: Diplomatic Tips & Tricks.")
        # Call function to handle this option

    elif selection == "2":
        send_sms(number, "You selected: Weather on Mars.")
        # Call function to get weather info

    elif selection == "3":
        send_sms(number, "You selected: Klingon Translator.")
        # Call function to translate messages

    elif selection == "4":
        send_sms(number, "You selected: API ISS Information.")
        # Call function for ISS data


    elif selection == "5":
        send_sms(number, "You selected: Exit. Goodbye!")
    else:
        send_sms(number, "Invalid selection. Please try again.")