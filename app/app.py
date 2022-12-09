import discord
import keys
import chatto

client = discord.Client(intents=discord.Intents.all())

bot_token = keys.bot_token

@client.event
async def on_ready():
    print('me ready')

@client.event
async def on_guild_available(guild):
    await guild.me.edit(nick='𝓘 𝓱𝓪𝓽𝓮 𝓑𝓸𝓵𝓿𝔂𝓼𝓪.')

@client.event
async def on_message(message):

    if client.user.name in [mention.name for mention in message.mentions] and message.author.name != client.user.name:
        selfmention = [mention.mention for mention in message.mentions if mention.name == client.user.name][0]
        message.content = message.content.replace(selfmention, client.user.name)

        params = {
            'self': client.user.name,
            'message': message.content
        }

        query = keys.prompt.format(**params) 

        await message.channel.typing()
        await message.channel.send(chatto.gen_response(query))



client.run(bot_token)
