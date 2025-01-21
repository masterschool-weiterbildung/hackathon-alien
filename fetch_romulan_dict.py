import requests
from bs4 import BeautifulSoup

def fetch_romulan_translation(letter, target_word):
    BASE_URL = "http://www.rihannsu.org/arch/www.rihan.org/drupal/dictionary/"
    url = f"{BASE_URL}{letter}.html"

    response = requests.get(url)
    if response.status_code != 200:
        return f"Failed to fetch data. HTTP Status: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    dict_list = soup.find("div", {"id": "dictlist"})
    if not dict_list:
        return "No dictionary content found on the page."

    for term in dict_list.find_all("dt"):  # English word is in <dt>
        english_word = term.text.strip().lower()
        if english_word == target_word.lower():
            definition = term.find_next_sibling("dd")  # Romulan translation is in <dd>
            if definition:
                translation_span = definition.find("span", class_="rihan")  # Translation is in <span>
                if translation_span:
                    return translation_span.text.strip().capitalize()
            return f"No Romulan translation found for '{target_word}'."

    return f"No Romulan translation found for '{target_word}'."



def english_to_romulan(word: str) -> str:

    first_letter = word[0].lower()

    result = fetch_romulan_translation(first_letter, word)
    # Output formatting and decision-making
    if result.startswith("No Romulan translation") or "Failed to fetch" in result:
        if result == f"Romulan translation for '{word}': No dictionary content found on the page.":
            return f"{word} does not exist in Romulan - don't panic!"
        return result
    else:
        return f"Romulan translation for '{word}': {result}"


def main():
    while True:
        user_input = input("Enter an English word to translate (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Jolan'tru! Goodbye!")
            break

        if not user_input:
            print("Please enter a valid word ")
            continue
        print(english_to_romulan(word = user_input))


if __name__ == "__main__":
    main()
