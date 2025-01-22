import requests


def get_solar_system_body(body_id):
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{body_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def get_all_planets():
    url = "https://api.le-systeme-solaire.net/rest.php/bodies"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        planets = [body for body in data["bodies"] if body["isPlanet"]]
        return planets
    else:
        print(f"Error: {response.status_code}")
        return []

def give_planet_data():
    planets = get_all_planets()

    planet_info = []
    for planet in planets:
        info = (
            f"Planet: {planet['englishName']}, "
            f"Gravity: {planet['gravity']} m/s², "
            f"Avg Temp: {planet['avgTemp']} K"
        )
        planet_info.append(info)

    return "Plan your escape based on that data:\n" + "\n".join(planet_info)


if __name__ == "__main__":
    result = give_planet_data()
    print(result)