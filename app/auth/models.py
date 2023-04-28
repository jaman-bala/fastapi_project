from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String
from app.utils.mixin import UserMixin
from database import Base
from sqlalchemy.orm import relationship
