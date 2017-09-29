# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, event

DB_DSN = 'postgresql+psycopg2://localhost/selftest'
DB_POOL_SIZE = 10
DB_MAX_OVERFLOW = -1
DB_POOL_RECYCLE = 1200



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# see https://stackoverflow.com/questions/29116718/how-to-mocking-created-time-in-sqlalchemy/46484795#46484795
