from .mongodb_connection import (
    comments_collection,
    external_collection
)

def get_comments(country):
    data=list(
        comments_collection.find(
            {
                "country":country
            },
            {
                "_id":0
            }
        )
    )
    return data

def add_comment(comment):
    result = comments_collection.insert_one(
        comment
    )
    return str(result.inserted_id)

def get_external_information(country):
    return list(
        external_collection.find(
            {
                "country":country
            },
            {
                "_id":0
            }
        )
    )