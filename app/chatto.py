import keys
import requests
import traceback
import json
import discord
import logging


def gen_response(query) -> str:

    opts = keys.completion_opts.copy()

    resp = requests.post(
        f"{keys.ollama_url}/api/chat",
        json={
            "model": opts["engine"],
            "messages": [{"role": "user", "content": query}],
            "options": {
                "temperature": 1,
            },
            "stream": False,
        },
    )

    try:
        return resp.json()["message"]["content"]
    except KeyError:
        traceback.print_exc()
        return (
            f"```{traceback.format_exc()}``````{json.dumps(resp.json(), indent=4)}```"
        )


def gen_response_history(
    history: list[discord.Message], client_user: discord.User, roleplay_prompt=""
):
    opts = keys.completion_opts.copy()

    messages = []
    prompt_set = False
    for message in history:
        new_entry = {}
        if message.author.name == client_user.name:
            new_entry["role"] = "assistant"
            new_entry["content"] = message.content
        else:
            new_entry["role"] = "user"
            if not prompt_set:
                new_entry["content"] = roleplay_prompt + "\n\n" + message.content
            else:
                new_entry["content"] = message.content

        messages += [new_entry]
    logging.error(messages)

    resp = requests.post(
        f"{keys.ollama_url}/api/chat",
        json={
            "model": opts["engine"],
            "messages": messages,
            "options": {
                "temperature": 1,
            },
            "stream": False,
        },
    )

    try:
        return resp.json()["message"]["content"]
    except KeyError:
        traceback.print_exc()
        return (
            f"```{traceback.format_exc()}``````{json.dumps(resp.json(), indent=4)}```"
        )
