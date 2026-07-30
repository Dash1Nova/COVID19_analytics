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
USE DATABASE COVID_PROJECT
""")

cursor.execute("""
USE SCHEMA PUBLIC
""")

cursor.execute("""
PUT file://data/world_pop_mig_186_countries.csv
@demographics_stage
AUTO_COMPRESS=TRUE
""")

cursor.execute("""
COPY INTO DEMOGRAPHICS
FROM @demographics_stage/world_pop_mig_186_countries.csv.gz
FILE_FORMAT = (
    TYPE = CSV,
    SKIP_HEADER = 1,
    FIELD_OPTIONALLY_ENCLOSED_BY='"'
)
ON_ERROR='CONTINUE'
""")

conn.commit()

cursor.close()
conn.close()