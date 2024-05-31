from pathlib import Path
from typing import NamedTuple

API_V1_PREFIX = "/api/v1"
SESSIONS_PATH = Path("sessions")


class Status(NamedTuple):
    waiting_qr_login = "waiting_qr_login"
    logged = "logged"
    error = "error"
