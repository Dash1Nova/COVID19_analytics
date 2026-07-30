import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    role=os.getenv("SNOWFLAKE_ROLE")
)

cursor = conn.cursor()

cursor.execute("""
CREATE DATABASE IF NOT EXISTS COVID_PROJECT
""")

cursor.execute("""
USE DATABASE COVID_PROJECT
""")

cursor.execute("""
USE SCHEMA PUBLIC
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS DEMOGRAPHICS(
    COUNTRY STRING,
    YEAR NUMBER,
    POPULATION NUMBER,
    NET_MIGRATION FLOAT,
    POPULATION_IN_MILLIONS FLOAT
)
""")

cursor.execute("""
CREATE STAGE IF NOT EXISTS demographics_stage
""")


conn.commit()

cursor.close()
conn.close()