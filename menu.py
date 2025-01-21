from utility import send_sms

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

def diplomatic_tips(number):
    tips = """
    Diplomatic Tips & Tricks:
    1. **First Contact**: "Do not comment on their glowing eyes—it’s a sensitive topic."
    2. **On Ship**: "Don't touch glowing buttons, unless you enjoy space roulette."
    3. **Escape**: "Offer a shiny object as a distraction."
    4. **Space Etiquette**: "Never ask about their home planet’s food—unless you’re ready to try the unidentifiable stew."
    5. **In a Crisis**: "If they offer you a seat, always sit—unless it's an inflatable chair that might deflate under pressure."
    6. **Negotiation**: "When dealing with alien species, avoid talking about the weather—it's always a sensitive issue."
    """
    send_sms(number, tips)

def process_selection(number, selection):
    """Handle the user’s menu selection"""

    if selection == "1":
        send_sms(number, "You selected: Diplomatic Tips & Tricks.")
        diplomatic_tips(number)

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