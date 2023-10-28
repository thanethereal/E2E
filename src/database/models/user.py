from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql
from sqlalchemy import (FLOAT, Boolean, Column, DateTime, ForeignKey, Integer,
                        String, Time)

from database.common.base import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    # Create Primary Key
    user_id = Column(Integer, primary_key=True)

    # Create attributes in table
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    passcode = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=True, default=True)