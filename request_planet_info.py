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


planets = get_all_planets()
print("\nPlan your escape. Where do you stuck? \n")
for planet in planets:
    print(f"Planet: {planet['englishName']}, Gravity: {planet['gravity']} m/s², Avg Temp: {planet['avgTemp']} K")


# print("SEARCH PLANET")
# def search_planet(planet_name):
#     planets = get_all_planets()
#     for planet in planets:
#         if planet['englishName'].lower() == planet_name.lower():
#             return planet
#     return f"Planet {planet_name} not found."



# mars_data = get_solar_system_body({"mars"})
# if mars_data:
#     print(f"Name: {mars_data['englishName']}")
#     print(f"Mass: {mars_data['mass']['massValue']} x 10^{mars_data['mass']['massExponent']} kg")
#     print(f"Gravity: {mars_data['gravity']} m/s²")
#     print(f"Gravity: {mars_data['gravity']} m/s²")
    # print(f"Discovered by: {mars_data.get('discoveredBy', 'Unknown')}")
    # print(f"Discovery date: {mars_data.get('discoveryDate', 'Unknown')}")


# return moon .. not highly useful
# print("additional query")
# earth_data = get_solar_system_body("earth")
# if earth_data:
#     moons = earth_data.get("moons", [])
#     if moons:
#         print("Moons of Earth:")
#         for moon in moons:
#             print(f"- {moon['moon']}")
#     else:
#         print("Earth has no moons listed.")


# DISPLAYS ALL PLANETS"

