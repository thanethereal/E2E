from typing import Optional
from pydantic import BaseModel
from datetime import time, datetime

class User(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    passcode: Optional[str] = None
    hashed_password: Optional[str] = None
    is_active: Optional[bool]