import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langfuse import Langfuse


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)


langfuse = Langfuse(
    public_key=os.getenv(
        "LANGFUSE_PUBLIC_KEY"
    ),

    secret_key=os.getenv(
        "LANGFUSE_SECRET_KEY"
    ),

    host=os.getenv(
        "LANGFUSE_HOST"
    )
)