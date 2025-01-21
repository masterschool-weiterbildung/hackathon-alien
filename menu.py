import request_iss_data
from api import send_sms_number


# Function to show the menu to the user
# Only this version work

def show_menu(number):
    menu = "Welcome, Space Traveler!\n\n1. Diplomacy Tips\n2.Klingon Translator\n3.ISS Data\n4.Exit"
    send_sms_number([{number: menu}])


# def show_menu(number):
#     menu = ("Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit"
#             "Welcome, Space Traveler!\nReply with:\n1. Diplomacy Tips\n2. Klingon Translator\n3. ISS Data\n4. Exit")

    # send_sms_number([{number: menu}])

# def show_menu(number):
#     menu = "===========================\n🌌**Welcome, Space Traveler!** 🌌\n===========================\nPlease choose an option:\n1️⃣ **Diplomatic Tips & Tricks**\n- Learn how to navigate space diplomacy with humor!\n2️⃣ **Weather on Mars**\n- Get the latest weather updates from the Red Planet.\n3️⃣ **Klingon Translator**\n- Ready to speak like a Klingon? Translate your message here.\n4️⃣ **API ISS Information**\n- Get real-time data about the International Space Station (ISS).\n5️⃣ **Exit ('I am OK')**\n- Leave the space adventure. We hope to see you again soon!"
#
#     send_sms_number([{number: menu}])

# def show_menu(number):
#     menu = ("===========================\n"
#         "🌌**Welcome, Space Traveler!** 🌌\n"
#         "===========================\n"
#         "Please choose an option:\n"
#         "1️⃣ **Diplomatic Tips & Tricks**\n"
#         "- Learn how to navigate space diplomacy with humor!\n"
#         "2️⃣ **Weather on Mars**\n"
#         "- Get the latest weather updates from the Red Planet.\n"
#         "3️⃣ **Klingon Translator**\n"
#         "- Ready to speak like a Klingon? Translate your message here.\n"
#         "4️⃣ **API ISS Information**\n"
#         "- Get real-time data about the International Space Station (ISS).\n"
#         "5️⃣ **Exit ('I am OK')**\n"
#         "- Leave the space adventure. We hope to see you again soon!")
#
#     send_sms_number([{number: menu}])

def diplomatic_tips(number):
    tips = ("Diplomatic Tips:\n1.Don’t comment on glowing eyes.\n2.Avoid touching glowing buttons."
            "\n3.Distract with shiny objects.\n4.Don’t ask about alien food.\n5.Sit if offered, unless inflatable."
            "\n6.Skip weather talk—it’s touchy")

    send_sms_number([{number: tips}])


def process_selection(number, selection):
    """Handle the user’s menu selection"""
    if selection == "1":
        send_sms_number([{number: "You selected: Diplomatic Tips & Tricks."}])
        diplomatic_tips(number)

    elif selection == "2":
        send_sms_number([{number:  "You selected: Klingon Translator."}])


    elif selection == "3":
        send_sms_number([{number:  "You selected: API ISS Information."}])


    elif selection == "4":
        send_sms_number([{number: "You selected: Exit. Goodbye!"}])
    else:
        send_sms_number([{number: "❌ Invalid selection. Please try again."}])

def main():
    show_menu("4915735156801")
    # diplomatic_tips("4915735156801")

if __name__ == "__main__":
    main()