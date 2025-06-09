import os
import requests
import psycopg2
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()  # ini hanya untuk running lokal, aman di Actions

API_KEY = os.getenv("OPENWEATHER_API_KEY")
DB_CONNECTION = os.getenv("SUPABASE_DB_CONNECTION")


cities = ["Jakarta", "Bandung", "Surabaya", "Medan", "Bali"]

def get_weather_data(city):
    try:
        print(f"[INFO] Fetching weather data for {city}...")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise ValueError(f"[ERROR] API Error for {city}: {data.get('message')}")

        return {
            "city": city,
            "date": datetime.fromtimestamp(data["dt"], timezone.utc).date(),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }
    except Exception as e:
        print(f"[ERROR] Failed to fetch data for {city}: {e}")
        return None

def save_to_db(weather):
    try:
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
        print(f"[SUCCESS] Data saved for {weather['city']} on {weather['date']}")
    except Exception as e:
        print(f"[ERROR] Failed to save data for {weather['city']}: {e}")

def main():
    for city in cities:
        data = get_weather_data(city)
        if data:
            save_to_db(data)

if __name__ == "__main__":
    main()
