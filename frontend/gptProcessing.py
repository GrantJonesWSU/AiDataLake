import os
import openai

openai.api_key = "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"

def GetGptResponse(gpt_input):
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=gpt_input,
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text
