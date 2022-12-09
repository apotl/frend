import openai
import keys

openai.api_key = keys.openai_token

def gen_response(query):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=512,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["text"]