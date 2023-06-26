import os
from typing import List

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text: str) -> List[float]:
    embedding = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text,
    )
    try:
        return embedding['data'][0]['embedding']
    except Exception as e:
        raise e # TODO: Handle API response