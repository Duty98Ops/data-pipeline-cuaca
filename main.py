import os
import requests
import psycopg2
from datetime import datetime, timezone

API_KEY = os.getenv("API_KEY")
DB_CONNECTION = os.getenv("DB_CONNECTION")

cities = ["Jakarta", "Bandung", "Surabaya", "Medan", "Bali"]

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"Error fetching data for {city}: {data.get('message')}")
        return None

    return {
        "city": city,
        "date": datetime.fromtimestamp(data["dt"], timezone.utc).date(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }

def save_to_db(weather):
    conn = psycopg2.connect(DB_CONNECTION)
    cursor = conn.cursor()
    insert_query = """
        INSERT INTO weather_data (city, date, temperature, humidity)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (city, date) DO NOTHING;
    """
    cursor.execute(insert_query, (weather["city"], weather["date"], weather["temperature"], weather["humidity"]))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Saved: {weather['city']} on {weather['date']}")

def main():
    for city in cities:
        data = get_weather_data(city)
        if data:
            save_to_db(data)

if __name__ == "__main__":
    main()
