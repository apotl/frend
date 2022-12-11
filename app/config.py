import yaml

with open('config.yml') as token_f:
    data = yaml.safe_load(token_f)['frend']

    bot_token = data['secrets']['discord_token']
    openai_token = data['secrets']['openai_token']

    completion_opts = data['completion_opts']