# Geolocation related tools

import requests
import json
import re


def my_ip() -> str:
    return requests.get("https://api64.ipify.org?format=json").text


def my_coordinates() -> str:
    ip_addr = json.loads(requests.get("https://api64.ipify.org?format=json").text)["ip"]

    my_loc = requests.get(
        "https://api.hostip.info/get_html.php?ip=" + ip_addr + "&position=true"
    ).text

    lat = float(re.search(r'Latitude:\s*([\d.-]+)', my_loc).group(1))
    lon = float(re.search(r'Longitude:\s*([\d.-]+)', my_loc).group(1))

    # print(lat, lon)

    return json.dumps({
        "latitude": lat,
        "longitude": lon,
    })


def weather(lat: float, lon: float) -> str:
    weather_report = json.loads(requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m").text
    )
    # print(json.dumps(weather_report))
    return json.dumps(weather_report)


__all__ = ["weather", "my_ip", "my_coordinates"]

# if __name__ == "__main__":
    # lat, lon = my_coordinates()
    # weather(lat,lon)
