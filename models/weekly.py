from pydantic import BaseModel
from enum import Enum
from models.post import PostInfo
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class WeeklyType(str, Enum):
    AppCoda = "AppCoda"
    OldDriver = "OldDriver"


class WeeklyInfo(BaseModel):
    summary: str
    id: str
    title: str
    url: str
    publishDate: str
    type: WeeklyType
    postArray: [PostInfo]
