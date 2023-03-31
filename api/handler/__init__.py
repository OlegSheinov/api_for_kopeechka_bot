import os
import re

from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def get_email_id_handler(email: str):
    url = f"https://api.kopeechka.store/mailbox-reorder?site={os.getenv('SITE')}" \
          f"&email={email}&regex=&" \
          f"token={os.getenv('TOKEN')}" \
          f"&type=json&subject=&api=2.0"
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
        soup = BeautifulSoup(data['fullmessage'], "lxml")
        all_md_text = soup.find_all('span', class_="mb_text")
        match = [re.search(r"( \d{5})", text.text) for text in all_md_text]
        code = list(filter(lambda x: x is not None, match))
        return int(code[0].group(1))
