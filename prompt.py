from langchain_core.prompts import PromptTemplate


def get_prompt():

    return PromptTemplate.from_template(
        """
You are a professional blog content analyst.

Generate:

1. Blog Title
2. Outline Sections (5-6)
3. Target Audience
4. Writing Goal


Topic:
{topic}


Audience:
{audience}


Return only valid JSON:

{{
"blog_title": "string",
"outline_sections": [
    "string"
],
"target_audience": "string",
"writing_goal": "string"
}}

"""
    )