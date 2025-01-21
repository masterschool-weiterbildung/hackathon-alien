async def get_response_text(response):
    """
    Extracts text content from an HTTP response.
    
    Args:
        response: The HTTP response object
        
    Returns:
        str: The text content of the response
    """
    
    if response == "x":
        sms_text = (
            "👽 Hi there, Earthling! Welcome to the *Alien Abduction Guide*! 🚀✨ "
            "Choose your path:\n\n"
            "1️⃣ General Tips & Diplomacy\n"
            "2️⃣ Alien Translator\n"
            "3️⃣ Space Weather Forecast\n"
            "4️⃣ ISS Drop-Off Tracker\n\n"
            "Reply with the number of your choice to begin your cosmic journey! 🌌"
        )
        return sms_text
    return None


