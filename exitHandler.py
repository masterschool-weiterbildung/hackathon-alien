async def send_exit_message(response):
    """
    Sends an exit/goodbye message to the provided phone number.
    
    Args:
        phone_number (str): The phone number to send the message to
        
    Returns:
        str: The goodbye message text
    """
    
    sms_text = ""
    if "exit" in response.lower():
        sms_text = (
            "👋 Thanks for exploring the *Alien Abduction Guide*! 🛸\n\n"
            "We hope you enjoyed your cosmic journey. Stay safe out there "
            "and remember - the truth is out there! ✨🌠\n\n" 
            "Text 'Hi' anytime to start a new adventure! 🚀"
        )
    return await sms_text
