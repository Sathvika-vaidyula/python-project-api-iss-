import requests
from datetime import datetime
import smtplib
import time

# Your location
MY_LAT = 20.593683
MY_LNG = 78.962883

# Your email credentials (use App Password for Gmail)
MY_EMAIL = "practise@gmail.com"
MY_PASSWORD = "sathvika@12345"  # WARNING: Don't share real passwords!

def is_iss_overhead():
    """Check if the ISS is currently overhead (within ±5 degrees)."""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and \
       (MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5):
        return True
    return False

def is_night():
    """Check if it is currently night at your location."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_time = datetime.fromisoformat(sunrise)
    sunset_time = datetime.fromisoformat(sunset)
    time_now = datetime.utcnow()

    return time_now < sunrise_time or time_now > sunset_time
while True:
    # Run check once
    if is_iss_overhead() and is_night():
        time.sleep(60)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
            )


