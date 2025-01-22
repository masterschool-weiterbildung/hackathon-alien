import requests
from bs4 import BeautifulSoup
import random


def fetch_ufo_data():
    url = "https://nuforc.org/subndx/?id=all"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error: Unable to fetch data (status code {response.status_code}) - don't panic!"

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    if not table:
        return "Error: Unable to locate the sightings table on the page - don't panic!"

    rows = table.find_all("tr")[1:]
    data = []
    count = 0
    for row in rows:
        cells = row.find_all("td")
        if cells:
            for cell in cells:
                if "href" in str(cell):
                    link_tag = cell.find('a')
                    href_value = link_tag.get('href')
                    data.append(
                        ["https://nuforc.org" + href_value, cells[6].text])
                    break
    return data


def format_ufo_data(data, max_sightings=3, randomize=True):
    """Formatting reports with random data"""
    if not data:
        return "No UFO sightings data available - don't panic!"

    if randomize:
        random.shuffle(data)

    print(data)
    formatted_sightings = []

    for row in data[:max_sightings]:
        formatted_sighting = f"{row[0]} : {row[1]}"
        formatted_sightings.append(formatted_sighting)

    return "\n".join(formatted_sightings)

    # def format_ufo_data(data, max_sightings=3):
    """Classic Format of Reports from data"""
    # if not data:
    #     return "No UFO sightings data available - don't panic!"
    #
    # formatted_sightings = []
    # for row in data[:max_sightings]:
    #     date_time = row[1]
    #     city = row[2]
    #     shape = row[5]
    #     description = row[6]
    #
    #     formatted_sighting = f"Date/Time: {date_time}, City: {city}, Shape: {shape}, Description: {description}"
    #     formatted_sightings.append(formatted_sighting)
    #
    # return "\n".join(formatted_sightings)


def main():
    # print("Fetching UFO sightings data...")
    ufo_data = fetch_ufo_data()

    condensed_data = format_ufo_data(ufo_data)
    print("\nPrepare yourself! These UFO sightings are real: \n")
    print(condensed_data)


if __name__ == "__main__":
    main()
