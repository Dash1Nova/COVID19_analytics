from .snowflake_connection import get_connection

def get_global_summary():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        COUNT(DISTINCT COUNTRY),
        SUM(CONFIRMED),
        SUM(DEATHS),
        SUM(RECOVERED),
        SUM(ACTIVE)
    FROM COVID_PROJECT.PUBLIC.COVID_DAILY
    WHERE DATE = (
        SELECT MAX(DATE)
        FROM COVID_PROJECT.PUBLIC.COVID_DAILY
    )
    """

    cursor.execute(query)

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "countries": row[0],
        "confirmed": row[1],
        "deaths": row[2],
        "recovered": row[3],
        "active": row[4]
    }

def compare_countries(country1, country2):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        COUNTRY,
        CONFIRMED,
        DEATHS,
        RECOVERED,
        ACTIVE
    FROM COVID_PROJECT.PUBLIC.COVID_DAILY
    WHERE COUNTRY IN (%s, %s)
      AND DATE = (
            SELECT MAX(DATE)
            FROM COVID_PROJECT.PUBLIC.COVID_DAILY
      )
    ORDER BY COUNTRY
    """

    cursor.execute(
        query,
        (
            country1.upper(),
            country2.upper()
        )
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    result = []

    for row in rows:
        result.append(
            {
                "country": row[0],
                "confirmed": row[1],
                "deaths": row[2],
                "recovered": row[3],
                "active": row[4]
            }
        )
    return result

def get_country_analytics(country):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        d.CONFIRMED,
        d.DEATHS,
        d.RECOVERED,
        d.ACTIVE,
        p.POPULATION
    FROM COVID_PROJECT.PUBLIC.COVID_DAILY d
    JOIN COVID_PROJECT.PUBLIC.DEMOGRAPHICS_CLEAN p
        ON d.COUNTRY = p.COUNTRY
       AND d.YEAR = p.YEAR
    WHERE d.COUNTRY = %s
      AND d.DATE = (
            SELECT MAX(DATE)
            FROM COVID_PROJECT.PUBLIC.COVID_DAILY
      )
    """

    cursor.execute(
        query,
        (country.upper(),)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return {
            "error": "Country not found"
        }

    confirmed = row[0]
    deaths = row[1]
    recovered = row[2]
    active = row[3]
    population = row[4]

    mortality_rate = 0
    recovery_rate = 0
    active_rate = 0
    cases_per_million = 0

    if confirmed > 0:

        mortality_rate = round(
            deaths / confirmed * 100,
            2
        )

        recovery_rate = round(
            recovered / confirmed * 100,
            2
        )

        active_rate = round(
            active / confirmed * 100,
            2
        )

    if population > 0:

        cases_per_million = round(
            confirmed / population * 1000000,
            2
        )

    return {

        "country": country.upper(),

        "confirmed": confirmed,

        "deaths": deaths,

        "recovered": recovered,

        "active": active,

        "population": population,

        "mortality_rate": mortality_rate,

        "recovery_rate": recovery_rate,

        "active_rate": active_rate,

        "cases_per_million": cases_per_million

    }

def search_country(country=None, date=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        COUNTRY,
        DATE,
        CONFIRMED,
        DEATHS,
        RECOVERED,
        ACTIVE

    FROM COVID_PROJECT.PUBLIC.COVID_DAILY

    WHERE 1=1
    """

    params = []
    if country:
        query += """
        AND COUNTRY ILIKE %s
        """
        params.append(
            f"%{country.upper()}%"
        )
    if date:
        query += """
        AND DATE = %s
        """
        params.append(date)
    query += """
    ORDER BY DATE
    """
    cursor.execute(
        query,
        params
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
    {
        "country": row[0],
        "date": str(row[1]),
        "confirmed": row[2],
        "deaths": row[3],
        "recovered": row[4],
        "active": row[5]
    }
    for row in rows
    ]