from api import send_sms_number


# Function to show the menu to the user

def show_menu(number):
    menu = "Welcome, Space Traveler!\n\n1. Diplomacy Tips\n2.Klingon Translator\n3.ISS Data\n4.Exit"

    send_sms_number([{number: menu}])
#
def diplomatic_tips(number):
    tips = ("Diplomatic Tips:\n1.Don’t comment on glowing eyes.\n2.Avoid touching glowing buttons."
            "\n3.Distract with shiny objects.\n4.Don’t ask about alien food.\n5.Sit if offered, unless inflatable."
            "\n6.Skip weather talk—it’s touchy")

    send_sms_number([{number: tips}])


def process_selection(number, selection):
    """Handle the user’s menu selection"""
    if selection == "1":
        send_sms_number([{number: "You selected: Diplomatic Tips & Tricks."}])
        # Call function to handle this option

    elif selection == "2":
        send_sms_number([{number:  "You selected: Klingon Translator."}])
        # Call function to translate messages

    elif selection == "3":
        send_sms_number([{number:  "You selected: API ISS Information."}])

    elif selection == "4":
        send_sms_number([{number: "You selected: Exit. Goodbye!"}])
    else:
        send_sms_number([{number: "❌ Invalid selection. Please try again."}])

def main():
    # show_menu("4915735156801")
    diplomatic_tips("4915735156801")

if __name__ == "__main__":
    main()