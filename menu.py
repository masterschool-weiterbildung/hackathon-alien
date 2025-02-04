from api import send_sms_number
from exitHandler import send_exit_message
from request_iss_data import iss_tracker
from request_planet_info import give_planet_data
from scrape_ufo_sighting import fetch_ufo_data, format_ufo_data


def show_menu(number: str) -> None:
    """ Function to show the menu to the user """
    menu = ("Welcome, Space Traveler!\n\nPlease choose an option:\n\n"
            "1. **Planet Information**\n- Get information about planets in the solar system.\n\n"
            "2. **Romulan Dictionary**\n- Translate words into Romulan.\n\n"
            "3. **API ISS Information**\n- Get real-time data about the International Space Station (ISS).\n\n"
            "4. **UFO Sightings**\n- Get the latest UFO sightings data.\n\n"
            "5. **Klingon Translator**\n- Translate phrases into Klingon.\n\n"
            "9. **Exit ('I am OK')**\n- Leave the space adventure. We hope to see you again soon!\n\n\n"
            "DON'T PANIC!")

    send_sms_number([{number: menu}])


def diplomatic_tips(number: str) -> None:
    """ sends diplomatic tips to the number """
    tips = ("Diplomatic Tips:\n\n"
            "1. Don’t comment on glowing eyes.\n\n"
            "2. Avoid touching glowing buttons.\n\n"
            "3. Distract with shiny objects.\n\n"
            "4. Don’t ask about alien food.\n\n"
            "5. Sit if offered, unless inflatable.\n\n"
            "6. Skip weather talk—it’s touchy\n\n")

    send_sms_number([{number: tips}])


def process_selection(number: str, selection: str) -> None:
    """ Handle the user’s menu selection """
    if selection == "1":
        send_sms_number([{number: give_planet_data()}])

    elif selection == "2":
        send_sms_number([{number: "Type a message starting with 'Romulan'\n\nLike this: 'Romulan Hello'"}])

    elif selection == "3":
        # We should not send multiple SMS for one entry.
        # send_sms_number([{number: "You selected: API ISS Information."}])
        text = "Convince your alien abductors to drop you off at the nearest space station: \n"
        iss_data = iss_tracker()
        if "error" in iss_data:
            text += iss_data["error"]
        else:
            text += (
                f"The ISS is currently over {iss_data['location_name']} at Latitude: {iss_data['latitude']}, "
                f"Longitude: {iss_data['longitude']}"
            )
        send_sms_number([{number: text}])

    elif selection == "4":
        ufo_data = fetch_ufo_data()
        condensed_data = format_ufo_data(ufo_data)
        text = f"Prepare yourself! These UFO sightings are real:\n{condensed_data}"
        send_sms_number([{number: text}])

    elif selection == "5":
        send_sms_number([{number: "Type a message starting with 'Klingon'\n\nLike this: 'Klingon Thank you Warrior'"}])

    elif selection == "9":
        send_sms_number([{number: send_exit_message("exit")}])
    else:
        send_sms_number([{number: "Invalid selection. Please try again."}])


def main():
    show_menu("4915735156801")
    # diplomatic_tips("4915735156801")


if __name__ == "__main__":
    main()
