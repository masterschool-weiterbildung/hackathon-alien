import requests
import os

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("NASA_API_KEY")

def get_mars_weather():

    url = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sol_keys = data.get("sol_keys", [])
        if sol_keys:
            latest_sol = sol_keys[-1]
            weather = data[latest_sol]
            return {
                "sol": latest_sol,
                "temperature": weather["AT"],
                "wind": weather["HWS"],
                "pressure": weather["PRE"]
            }
        else:
            return "No recent weather data found for Mars"
    else:
        return f"Error: {response.status_code}"

# print(get_mars_weather())



def get_mars_weather_mock():
    return {
        "sol": "1000",
        "temperature": {"av": -65.0},
        "wind": {"av": 5.4},
        "pressure": {"av": 732.0},
    }


def main():
    mars_weather = get_mars_weather_mock()
    mars_weather = get_mars_weather()
    print("Mars Weather Report:")
    print(mars_weather)

if __name__ == "__main__":
    main()
