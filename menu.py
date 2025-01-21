import request_iss_data
from api import send_sms_number


# Function to show the menu to the user
# Only this version work

def show_menu(number):
    menu = ("Welcome, Space Traveler!\n\nPlease choose an option:\n\n"
            "1. **Diplomatic Tips & Tricks**\n- Learn how to navigate space diplomacy with humor!\n\n"
            "2. **Klingon Translator**\n- Ready to speak like a Klingon? Translate your message here.\n\n"
            "3. **API ISS Information**\n- Get real-time data about the International Space Station (ISS).\n\n"
            "4. **Exit ('I am OK')**\n- Leave the space adventure. We hope to see you again soon!")

    send_sms_number([{number: menu}])


def diplomatic_tips(number):
    tips = ("Diplomatic Tips:\n\n"
            "1. Don’t comment on glowing eyes.\n\n"
            "2. Avoid touching glowing buttons.\n\n"
            "3. Distract with shiny objects.\n\n"
            "4. Don’t ask about alien food.\n\n"
            "5. Sit if offered, unless inflatable.\n\n"
            "6. Skip weather talk—it’s touchy\n\n")

    send_sms_number([{number: tips}])


def process_selection(number, selection):
    """Handle the user’s menu selection"""
    if selection == "1":
        send_sms_number([{number: "You selected: Diplomatic Tips & Tricks."}])
        diplomatic_tips(number)

    elif selection == "2":
        send_sms_number([{number: "You selected: Klingon Translator."}])


    elif selection == "3":
        send_sms_number([{number: "You selected: API ISS Information."}])


    elif selection == "4":
        send_sms_number([{number: "You selected: Exit. Goodbye!"}])
    else:
        send_sms_number([{number: "❌ Invalid selection. Please try again."}])


def main():
    # show_menu("491795213992")
    diplomatic_tips("491795213992")


if __name__ == "__main__":
    main()
