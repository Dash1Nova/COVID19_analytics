from functools import lru_cache

from api.snowflake_service import (
    get_global_summary,
    get_country_analytics
)


@lru_cache(maxsize=100)
def cached_global_summary():
    return get_global_summary()



@lru_cache(maxsize=100)
def cached_country_analytics(country):
    return get_country_analytics(country)