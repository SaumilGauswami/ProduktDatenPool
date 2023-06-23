from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, text, JSON, DateTime, Text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, ENUM, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user


Base = declarative_base()
metadata = Base.metadata


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    api_key = Column(String(255))
    is_deleted = Column(TINYINT(1), server_default=text("'0'"))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SolarTable(Base):

    __tablename__ = 'Solar'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    link = Column(String(255))
    manufacturer_no = Column(String(255))
    articleNumber = Column(String(255))
    title = Column(String(255))
    breadcrums = Column(String(255))
    description = Column(Text)
    image = Column(Text)
    sitename = Column(String(255))
    is_deleted = Column(TINYINT(1), server_default=text("'0'"))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
