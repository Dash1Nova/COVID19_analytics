from pydantic import BaseModel
from datetime import date

class CommentModel(BaseModel):
    country: str
    date: date
    comment: str
    created_by: str
    tags: list[str] = []

class ExternalInformationModel(BaseModel):
    country: str
    source_name: str
    title: str
    url: str
    description: str
    related_metrics: list[str] = []