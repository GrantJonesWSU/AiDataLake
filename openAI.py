import os
import openai

def gpt3(stext):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
        temperature=0.0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text


query = input('Question: ')
response = gpt3(query)
print(response)

