import discord
import keys
import chatto
import traceback
import asyncio
from time import sleep

client = discord.Client(intents=discord.Intents.all())

bot_token = keys.bot_token

garbage = keys.completion_opts.copy()["prompt"]

MAX_MESSAGE_LENGTH = 2000


@client.event
async def on_guild_available(guild):
    await guild.me.edit(nick=keys.data["nick"])


def get_message_reference_chain(chain: list[discord.Message]) -> list[discord.Message]:
    if len(chain) < 1:
        raise ValueError("chain too small")
    if isinstance(chain[0].reference, discord.MessageReference):
        chain.insert(0, chain[0].reference.resolved)
        chain = get_message_reference_chain(chain)
    return chain


@client.event
async def on_message(message: discord.Message):

    try:

        if (
            client.user.name in [mention.name for mention in message.mentions]
            and message.author.name != client.user.name
        ):
            selfmention = [
                mention.mention
                for mention in message.mentions
                if mention.name == client.user.name
            ][0]
            message.content = message.content.replace(selfmention, client.user.name)

            message_history = get_message_reference_chain([message])

            async with message.channel.typing():
                response = chatto.gen_response_history(
                    message_history, client.user, roleplay_prompt=garbage
                )
                i = 0
                while i < len(response):
                    await message.channel.send(response[i : i + MAX_MESSAGE_LENGTH])
                    i += MAX_MESSAGE_LENGTH
    except Exception:
        traceback.print_exc()
        await message.channel.send(f"```{traceback.format_exc()}```")


client.run(bot_token)
