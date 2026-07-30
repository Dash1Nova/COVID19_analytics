import requests

API_URL = "http://localhost:8000"


def get_summary():
    response = requests.get(
        f"{API_URL}/summary"
    )
    return response.json()


def get_country_analytics(country):
    response = requests.get(
        f"{API_URL}/analytics/{country}"
    )
    return response.json()


def compare_countries(country1, country2):
    response = requests.get(
        f"{API_URL}/compare",
        params={
            "country1": country1,
            "country2": country2
        }
    )
    return response.json()


def get_comments(country):
    response = requests.get(
        f"{API_URL}/comments/{country}"
    )
    return response.json()


def add_comment(data):
    response = requests.post(
        f"{API_URL}/comments",
        json=data
    )
    return response.json()