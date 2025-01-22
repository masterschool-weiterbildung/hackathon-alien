def send_exit_message(message: str) -> str:
    """
    Generate an exit message when user sends 'exit'

    :param message: input message
    :return: a farewell message if 'exit' is in the message, empty string otherwise
    """
    sms_text = ""
    if "exit" in message.lower():
        sms_text = (
            "👋 Thanks for exploring the *Alien Abduction Guide*! 🛸\n\n"
            "We hope you enjoyed your cosmic journey. Stay safe out there "
            "and remember - the truth is out there! ✨🌠\n\n" 
            "Text 'Hi' anytime to start a new adventure! 🚀"
        )
    return sms_text
