from manga_arab.getters import  Getter
from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
        g = Getter(session)
        re = await g.get_details('moekare-wa-orenjiiro')


import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(main())