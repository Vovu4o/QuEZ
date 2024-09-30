import asyncio
import io
import time
from fastapi import UploadFile

from .processing import kw_from_file

async def get_keywords(content, navec):
    csv = io.BytesIO(content)
    ans_json = kw_from_file(content, navec)
    return ans_json


