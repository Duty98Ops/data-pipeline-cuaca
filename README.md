Berikut contoh README.md lengkap dan profesional untuk project Weather Data Pipeline kamu:

````markdown
# Weather Data Pipeline Automation

Automated pipeline to fetch, clean, and store daily weather data from OpenWeatherMap API for multiple Indonesian cities, with data saved in a cloud PostgreSQL database (Supabase). The pipeline runs automatically every day using GitHub Actions for seamless hands-free updates.

---

## 🚀 Features

- Fetches current weather data for Jakarta, Bandung, Surabaya, Medan, and Bali.
- Cleans and formats temperature (°C) and humidity (%) data.
- Stores data in Supabase PostgreSQL with unique constraints to prevent duplicates.
- Scheduled daily automation via GitHub Actions.
- Supports local manual run for testing or debugging.

---

## 🛠️ Tech Stack

- Python (requests, psycopg2, python-dotenv)
- OpenWeatherMap API
- PostgreSQL (Supabase)
- GitHub Actions (CI/CD Automation)

---

## 🔧 Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/Duty98Ops/data-pipeline-cuaca.git
cd data-pipeline-cuaca
````

2. **Create and activate Python virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create `.env` file in project root with your credentials**

```
OPENWEATHER_API_KEY=your_openweathermap_api_key_here
SUPABASE_DB_CONNECTION=your_supabase_db_connection_string_here
```

---

## ⚙️ Usage

* **Run manually**

```bash
python main.py
```

* **Test database connection**

```bash
python test_db_connection.py
```

* **GitHub Actions**

The pipeline is automatically triggered daily via GitHub Actions. Workflow file is located at `.github/workflows/run-pipeline.yml`.

Make sure you add the following GitHub Secrets in your repo:

* `OPENWEATHER_API_KEY`
* `SUPABASE_DB_CONNECTION` (use pooler connection string for GitHub Actions)

---

## 📈 Data Schema

Table: `weather_data`

| Column      | Type    | Description                |
| ----------- | ------- | -------------------------- |
| city        | VARCHAR | City name                  |
| date        | DATE    | Date of data               |
| temperature | VARCHAR | Temperature with unit (°C) |
| humidity    | VARCHAR | Humidity percentage (%)    |

Unique constraint on `(city, date)` to avoid duplicates.

---

## ⚠️ Common Issues & Solutions

| Issue                              | Cause                               | Solution                                    |
| ---------------------------------- | ----------------------------------- | ------------------------------------------- |
| Connection to Supabase fails       | Wrong connection string or network  | Use correct direct/pooler connection        |
| API returns error 401 Unauthorized | Invalid or inactive API key         | Verify API key in `.env` and GitHub secrets |
| Module not found (python-dotenv)   | Dependency not installed            | Run `pip install -r requirements.txt`       |
| Duplicate data entries             | Missing `ON CONFLICT` in insert SQL | Check SQL insert statement                  |

---

## 🔗 Links

* [Live Web App (Streamlit)](https://app-cuaca-rc7qst53mnvsvvbtwfca9b.streamlit.app/)

