import os
from pathlib import Path
from rich import print

BASE_DIR = Path("__file__").resolve().parent


UPLOAD_DIR = BASE_DIR / "uploads"


# Create upload path is not exist.
if not os.path.exists(UPLOAD_DIR):
    print("\n\t[italic red]Upload didn't exists :([/italic red]")
    print("\t[italic yellow]Creating the Upload[/italic yellow]")
    os.mkdir(UPLOAD_DIR)
    print("\t[bold green]Upload Created  :)[/bold green]\n")
else:
    print("\n\t[bold green]Upload found :)[/bold green]\n")

ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:9000",
    "http://127.0.0.1:9000",
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]


ALLOWED_METHODS = [
    "GET",
    # "POST",
    "OPTIONS"
]

ALLOWED_HEADERS = [
    "text/json",
    "application/json",
    'multipart/form-data',
    "text/plain",
]