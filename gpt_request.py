import os
import openai

def run_query(api_key, query, temperature=0.5):
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=temperature,
        max_tokens=1000,
        top_p=1,
    )
    return response["choices"][0]["text"], api_key

