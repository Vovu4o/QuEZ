import asyncio
import time
from fastapi import UploadFile


async def parse_opinion_file(file: UploadFile):
    content = await file.read()
    await asyncio.sleep(1)

def get_keywords(content):
    time.sleep(3)
    return content
