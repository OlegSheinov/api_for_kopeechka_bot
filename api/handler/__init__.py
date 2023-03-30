import os

from aiohttp import ClientSession


async def get_email_id_handler(email: str):
    url = f"https://api.kopeechka.store/mailbox-get-fresh-id?token={os.getenv('TOKEN')}" \
          f"&site={os.getenv('SITE')}" \
          f"&email={email}" \
          f"&type=json&api=2.0"
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    return int(data['id'])


async def get_code_from_id_handler(email_id: int):
    url = f"https://api.kopeechka.store/mailbox-get-message?full=0&id={email_id}&token={os.getenv('TOKEN')}" \
          f"&type=json&api=2.0"
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    if not data.get("fullmessage", None):
        return data['value']
    else:
        return data['fullmessage']
