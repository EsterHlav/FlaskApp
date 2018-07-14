import os
from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from flask_session import Session
import sqlalchemy
from sqlalchemy.sql.expression import cast
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

# Set up database
dbSQLA = SQLAlchemy()
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

class UserLogin(dbSQLA.Model):
    __tablename__ = "userlogin"
    id = dbSQLA.Column(dbSQLA.Integer, primary_key=True)
    name = dbSQLA.Column(dbSQLA.String, nullable=False)
    password = dbSQLA.Column(dbSQLA.String, nullable=False)

class ZIPS(dbSQLA.Model):
    __tablename__ = "zips"
    id = dbSQLA.Column(dbSQLA.Integer, primary_key=True)
    zipcode = dbSQLA.Column(dbSQLA.Integer, nullable=False)
    city = dbSQLA.Column(dbSQLA.String, nullable=False)
    state = dbSQLA.Column(dbSQLA.String, nullable=False)
    latitude = dbSQLA.Column(dbSQLA.Numeric(precision=2), nullable=False)
    longtitude = dbSQLA.Column(dbSQLA.Numeric(precision=2), nullable=False)
    population = dbSQLA.Column(dbSQLA.Integer, nullable=False)
    checkins = dbSQLA.Column(dbSQLA.Integer, nullable=False)

class Comments(dbSQLA.Model):
    __tablename__ = "comments"
    id = dbSQLA.Column(dbSQLA.Integer, primary_key=True)
    idlocation = dbSQLA.Column(dbSQLA.Integer, nullable=False)
    location = dbSQLA.Column(dbSQLA.String, nullable=False)
    userid = dbSQLA.Column(dbSQLA.Integer, nullable=False)
    comment = dbSQLA.Column(dbSQLA.String, nullable=False)
