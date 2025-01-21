import requests
from bs4 import BeautifulSoup
import csv

def fetch_ufo_data():
    url = "https://nuforc.org/subndx/?id=all"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch data (status code {response.status_code})")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")

    if not table:
        print("Error: Unable to locate the sightings table on the page")
        return []

    rows = table.find_all("tr")[1:]
    data = []

    for row in rows:
        cells = row.find_all("td")
        if cells:
            data.append([cell.text.strip() for cell in cells])

    return data


def display_ufo_data(data):
    if not data:
        print("No data to display.")
        return

    headers = [
        "Status", "Date/Time", "City", "State", "Country",
        "Shape", "Description", "Reported Date", "Media", "Explanation"
    ]

    # Print formatted table header
    print(f"{headers[0]:<10}{headers[1]:<20}{headers[2]:<15}{headers[3]:<5}{headers[4]:<10}{headers[5]:<10}{headers[6]:<50}{headers[7]:<15}{headers[8]:<10}{headers[9]:<10}")
    print("-" * 130)

    # Print each row of data
    for row in data[:3]:  # <- CHOSE HOW MANY ROWS TO DISPLAY .. MAYBE 1 FOR SMS
        print(f"{row[0]:<10}{row[1]:<20}{row[2]:<15}{row[3]:<5}{row[4]:<10}{row[5]:<10}{row[6]:<50}{row[7]:<15}{row[8]:<10}{row[9]:<10}")


def save_to_csv(data, filename="ufo_sightings.csv"):
    headers = [
        "Status", "Date/Time", "City", "State", "Country",
        "Shape", "Description", "Reported Date", "Media", "Explanation"
    ]

    # with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(headers)
    #     writer.writerows(data)
    # print(f"Data successfully saved to {filename}")


def main():
    # print("Fetching UFO sightings data...")
    ufo_data = fetch_ufo_data()

    print("\nHide! Latest UFO sightings: \n")
    display_ufo_data(ufo_data)

    # save_to_csv_choice = input("\nDo you want to save the data to a CSV file? (yes/no): ").lower()
    # if save_to_csv_choice in ["yes", "y"]:
    #     save_to_csv(ufo_data)


if __name__ == "__main__":
    main()
