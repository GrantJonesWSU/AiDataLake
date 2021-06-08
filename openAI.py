import os
import openai

def gpt3(stext):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
            temperature=0.1,
            max_tokens=1000,
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

