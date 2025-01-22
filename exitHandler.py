def send_exit_message(message):
    """
    Generate an exit message when user sends 'exit'.
    
    Args:
        message (str): The message received from the user
        
    Returns:
        str: A farewell message if 'exit' is in the message, empty string otherwise
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
