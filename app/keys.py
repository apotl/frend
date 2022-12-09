import yaml

bot_token = ''
openai_token = ''

with open('config.yml') as token_f:
    data = yaml.safe_load(token_f)
    bot_token = data['discord_token']
    openai_token = data['openai_token']
    prompt = data['prompt']