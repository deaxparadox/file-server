
import os
from binascii import hexlify

from core import settings

def generate_id() -> str:
    return hexlify(os.urandom(36)).decode('utf-8')

def generate_filename(file: str) -> str:
    return os.path.join(settings.UPLOAD_DIR, file)