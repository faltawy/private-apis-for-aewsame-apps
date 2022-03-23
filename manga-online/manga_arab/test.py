from manga_arab.getters import read_chapter
import asyncio

async def main():
    print(await read_chapter('hadashi-de-bara-wo-fume',1))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())