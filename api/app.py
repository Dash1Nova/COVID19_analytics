from fastapi import FastAPI, HTTPException

from api.models import CommentModel

from api.snowflake_service import (
    compare_countries,
    search_country
)

from api.cache import (
    cached_global_summary,
    cached_country_analytics
)

from api.mongodb_service import (
    get_comments,
    add_comment,
    get_external_information
)


app = FastAPI(
    title="COVID Analytics API"
)


@app.get("/")
def home():
    return {
        "message": "COVID Analytics API running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/summary")
def summary():
    return cached_global_summary()


@app.get("/compare")
def compare(
    country1: str,
    country2: str
):
    return compare_countries(
        country1,
        country2
    )


@app.get("/analytics/{country}")
def analytics(country: str):
    return cached_country_analytics(
        country.upper()
    )


@app.get("/search")
def search(
    country: str = None,
    date: str = None
):
    return search_country(
        country,
        date
    )


@app.get("/comments/{country}")
def comments(country: str):
    return get_comments(country)


@app.post("/comments")
def create_comment(
    comment: CommentModel
):
    comment_id = add_comment(
        comment.model_dump()
    )
    return {
        "message": "Comment added",
        "id": comment_id
    }


@app.get("/sources/{country}")
def sources(country:str):

    return get_external_information(country)