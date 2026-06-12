from pydantic import BaseModel
from typing import List


class BlogOutline(BaseModel):
    blog_title: str
    outline_sections: List[str]
    target_audience: str
    writing_goal: str