from typing import Optional

from fastapi import Depends, Request
from fastapi_users import (BaseUserManager, IntegerIDMixin, exceptions, models, schemas)

from app.auth.models import User
from app.auth.utils import get_user_db
from config import SECRET

