from utility import send_sms


# Function to show the menu to the user
def show_menu(number):
    menu = """
    ===========================
    🌌 **Welcome, Space Traveler!** 🌌
    ===========================

    Please choose an option:

    1️⃣ **Diplomatic Tips & Tricks**
        - Learn how to navigate space diplomacy with humor!

    2️⃣ **Weather on Mars**
        - Get the latest weather updates from the Red Planet.

    3️⃣ **Klingon Translator**
        - Ready to speak like a Klingon? Translate your message here.

    4️⃣ **API ISS Information**
        - Get real-time data about the International Space Station (ISS).

    5️⃣ **Exit ("I am OK")**
        - Leave the space adventure. We hope to see you again soon!

    ===========================
    """
    send_sms(number, menu)


def diplomatic_tips(number):
    tips = """
    🌟 **Diplomatic Tips & Tricks** 🌟

    1️⃣ **First Contact**: "Do not comment on their glowing eyes—it’s a sensitive topic."

    2️⃣ **On Ship**: "Don't touch glowing buttons, unless you enjoy space roulette."

    3️⃣ **Escape**: "Offer a shiny object as a distraction."

    4️⃣ **Space Etiquette**: "Never ask about their home planet’s food—unless you’re ready to try the unidentifiable stew."

    5️⃣ **In a Crisis**: "If they offer you a seat, always sit—unless it's an inflatable chair that might deflate under pressure."

    6️⃣ **Negotiation**: "When dealing with alien species, avoid talking about the weather—it's always a sensitive issue."

    ===========================
    """
    send_sms(number, tips)


def process_selection(number, selection):
    """Handle the user’s menu selection"""
    if selection == "1":
        send_sms(number, "You selected: Diplomatic Tips & Tricks.")
        # Call function to handle this option
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
        send_sms(number, "❌ Invalid selection. Please try again.")
