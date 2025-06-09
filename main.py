import requests
import psycopg2
from datetime import datetime, timezone

API_KEY = "d8c002434a617d91031beec1007c8bde"
DB_CONNECTION = "postgres://postgres:mCz%40saG8%40V7wBEM@db.mjjyjnnnyhmjeefhnsan.supabase.co:5432/postgres"

cities = ["Jakarta", "Bandung", "Surabaya", "Medan", "Bali"]

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"Error fetching data for {city}: {data.get('message')}")
        return None

    weather = {
        "city": city,
        "date": datetime.fromtimestamp(data["dt"], timezone.utc).date(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }
    return weather

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
    print(f"Saved data for {weather['city']} on {weather['date']}")

def main():
    for city in cities:
        weather = get_weather_data(city)
        if weather:
            save_to_db(weather)

if __name__ == "__main__":
    main()
