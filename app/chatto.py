import openai
import keys

openai.api_key = keys.openai_token

def gen_response(query):

    opts = keys.completion_opts.copy()
    opts['prompt'] = query

    response = openai.Completion.create(**opts)

    return response["choices"][0]["text"]