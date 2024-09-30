import asyncio
import time
from fastapi import UploadFile

from .processing import kw_from_file

async def get_keywords(content):
    ans_json = kw_from_file(content)
    return ans_json


