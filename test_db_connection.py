import psycopg2

# Ganti <connection_string> dengan connection string Supabase kamu yang benar
CONNECTION_STRING = "postgresql://postgres:mCz%40saG8%40V7wBEM@db.mjjyjnnnyhmjeefhnsan.supabase.co:5432/postgres"

try:
    conn = psycopg2.connect(CONNECTION_STRING)
    print("✅ Connection success!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
