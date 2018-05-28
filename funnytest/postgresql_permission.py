# -*- coding: utf-8 -*-

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    text,
    ForeignKey,
    DateTime,
)

DB_DSN = 'postgresql+psycopg2://localhost/dev_test'
DB_POOL_SIZE = 10
DB_MAX_OVERFLOW = -1
DB_POOL_RECYCLE = 1200


engine = create_engine(DB_DSN, pool_size=DB_POOL_SIZE,
                       max_overflow=DB_MAX_OVERFLOW,
                       pool_recycle=DB_POOL_RECYCLE)


DBSession = scoped_session(sessionmaker(bind=engine, autocommit=False,
                                        expire_on_commit=False))
Base = declarative_base()


class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)


class GroupPermission(Base,):
    __tablename__ = 'group_permission'

    id = Column(Integer, primary_key=True)
    permission_id = Column(Integer, ForeignKey('permission.id'))
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.now)


if __name__ == '__main__':

    for table in Base.metadata.sorted_tables:
        print(table.name)
        sql = text('DROP TABLE IF EXISTS {};'.format(table.name))
        DBSession().execute(sql)
        DBSession().commit()
