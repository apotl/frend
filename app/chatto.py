import openai
import app.config as config

openai.api_key = config.openai_token

def gen_response(query):

    opts = config.completion_opts.copy()
    opts['prompt'] = query

    response = openai.Completion.create(**opts)

    return response["choices"][0]["text"]