import requests

def translate_to_klingon(text, api_key):
    url = f"https://api.funtranslations.com/translate/klingon.json?text={text}"
    headers = {"X-Funtranslations-Api-Secret": api_key}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data["contents"]["translated"]
        elif response.status_code == 429:  # Too many requests (rate limit)
            return "Error: Rate limit exceeded. Please wait a while and try again."
        else:
            error_message = response.json().get("error", {}).get("message", "Unknown error occurred.")
            return f"Error {response.status_code}: {error_message}"
    except requests.RequestException as e:
        return f"Request failed: {e}"


def process_translation_request(input_text, api_key):
    input_text = input_text.strip()
    if not input_text:
        return "No need to be nervous just because they are huge armed warriors - please enter a text"

    if input_text.isdigit():
        return "Klingon warriors aren't impressed by numbers. Rather enter some words!"

    translation = translate_to_klingon(input_text, api_key)
    if translation:
        return f"Original: {input_text}\nKlingon: {translation}"
    else:
        return "Translation failed. Please try again later. Dont panic!"


if __name__ == "__main__":

    api_key = "X-Funtranslations-Api-Secret"  # Official key - no need to .env
    user_input = input("Enter your text - keep smiling while doing it: ")
    result = process_translation_request(user_input, api_key)
    print(result)
