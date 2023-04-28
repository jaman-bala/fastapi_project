from datetime import datetime
from database import Base
from sqlalchemy import Column, DateTime



class UserMixi:
    data_created = Column(DataTime, default=datetime.utcnow)
    data_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)