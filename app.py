from fastapi import FastAPI, HTTPException
import psycopg2
import os
import logging
from pydantic import BaseModel

app = FastAPI()

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database Configuration
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD", "pass@123"),  # Use env variable
    "host": "db",
    "port": "5432",
}

# Function to establish database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_CONFIG["dbname"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
        )
        return conn
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

# Ensure table exists
def create_table():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reports (id SERIAL PRIMARY KEY,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Table 'reports' ensured.")
    except Exception as e:
        logger.error(f"Error creating table: {str(e)}")
        raise HTTPException(status_code=500, detail="Database setup failed")

# Run table creation on startup
create_table()

# Request model
class ReportRequest(BaseModel):
    message: str

# POST API to receive a report
@app.post("/report")
async def receive_report(data: ReportRequest):
    try:
        message = data.message
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into table and return the ID
        cursor.execute("INSERT INTO reports (message) VALUES (%s) RETURNING id;", (message,))
        report_id = cursor.fetchone()

        if not report_id:
            raise Exception("Failed to insert record.")
        conn.commit()
        cursor.close()
        conn.close()

        return {"status": "success", "report_id": report_id[0], "message": message}

    except Exception as e:
        logger.error(f"Error processing report: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing report: {str(e)}")

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}
