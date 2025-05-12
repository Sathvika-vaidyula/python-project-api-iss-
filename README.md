# ISS Overhead Notifier

This Python script notifies you via email when the International Space Station (ISS) is overhead your location **and** it's currently night, so you can look up and possibly see it!

---

## 🚀 Features

- Fetches real-time ISS position using the Open Notify API.
- Checks if the ISS is within ±5° of your latitude and longitude.
- Uses sunrise-sunset API to determine if it’s currently night.
- Sends an email alert when both conditions are met.

---

## 🛠 Requirements

- Python 3.x
- Modules:
  - `requests`
  - `datetime`
  - `smtplib`

Install dependencies with:

```bash
pip install requests
