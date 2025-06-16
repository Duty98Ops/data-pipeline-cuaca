# Weather Data Pipeline Automation

An automated data pipeline that retrieves, processes, and stores daily weather information for key Indonesian cities using the OpenWeatherMap API. The data is securely saved in a cloud PostgreSQL database hosted on Supabase. The entire process is fully automated via GitHub Actions, ensuring reliable, hands-off daily updates.

---

## 🚀 Key Features

- **Multi-city data fetching:** Retrieves up-to-date weather info for Jakarta, Bandung, Surabaya, Medan, and Bali.  
- **Data cleaning & formatting:** Standardizes temperature (°C) and humidity (%) values for consistency.  
- **Reliable storage:** Inserts data into Supabase PostgreSQL with conflict handling to avoid duplicates.  
- **Automated scheduling:** Runs daily via GitHub Actions for seamless, maintenance-free operation.  
- **Local execution:** Supports manual runs locally to facilitate testing and debugging.

---

## 🛠️ Technology Stack

- Python: requests, psycopg2, python-dotenv  
- API: OpenWeatherMap  
- Database: PostgreSQL (hosted on Supabase)  
- Automation: GitHub Actions (CI/CD)

---

## 🔧 Setup & Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Duty98Ops/data-pipeline-cuaca.git
    cd data-pipeline-cuaca
    ```

2. **Create and activate a Python virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create `.env` file in the project root with your credentials:**

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

