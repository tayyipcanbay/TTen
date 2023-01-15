import requests

# import os
# import dotenv
import openai


def gptRequest(_apiKey, _maxTokens, _prompt):
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = _apiKey
    response = openai.Completion.create(
        model="text-davinci-003", prompt=_prompt, temperature=0, max_tokens=_maxTokens
    )
    return response


def returnAnswerToClient(_answer):
    # payload = dict(key1='value1', key2='value2')

    # TODO answer type check. try catch

    r = requests.post("https://httpbin.org/post", data=_answer)
    # print("Answer sent to client: " + r.text)
    return r.text


def run_query(prompt=None, apiKey=None, maxTokens=5):
    if not apiKey:
        apiKey = "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"
    if not prompt:
        requestBody = "whats the meaning of 31?"
    else:
        requestBody = prompt
    gptResponse = gptRequest(apiKey, maxTokens, requestBody)
    return returnAnswerToClient(gptResponse)
