from pydantic import BaseModel
from enum import Enum
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class PostType(str, Enum):
    news = "news"
    blog = "blog"
    tips = "tips"


class PostInfo(BaseModel):
    summary: str
    id: str
    title: str
    url: str
    siteName: str
    author: str
    publishDate: str
    type: PostType
    tags: List[str]
