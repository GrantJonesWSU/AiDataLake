import os
import openai

def gpt3(stext):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt="Create an SQL request to find all users who live in California and have over 1000 credits:\n\nSELECT first_name, last_name, credits FROM users WHERE state = 'CA' AND credits > 1000\n\nCreate an SQL request to find all users who live in Michigan and have under 500 credits\n\nSELECT ids FROM users WHERE state = 'MI' AND credits < 500\n\nCreate an SQL request to find all users who live in Detroit\n\nSELECT ids FROM users WHERE city = 'Detroit'\n\nCreate an SLQ request to find the address of users who have a pet dog\n\nSELECT ids FROM users WHERE pet_type = 'dog'\n\nCreate an SQL request to find all users who have more than 1 pet\n\nSELECT ids FROM users WHERE pet_type IN ( 'dog', 'cat', 'bird' )\n\nCreate an SQL request to find all users who live in Royal Oak SELECT ids FROM users WHERE city = 'Royal Oak'\n\nCreate an SQL request to find all users who have ordered products in February SELECT ids FROM users WHERE month = 'February' AND order_date > '2014-01-01' AND order_date < '2014-02-01'\n\nCreate an SQL request to find all users who live in Detroit SELECT ids FROM users WHERE city = 'Detroit'",
        temperature=0.0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text


query = input('Statement: ')
response = gpt3(query)
print(response)

